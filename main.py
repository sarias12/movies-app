from fastapi import FastAPI, Body, HTTPException, Path, Query, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from models import Movie, User
from typing import List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

app = FastAPI()
app.title = "My First App with FastAPI"
app.version = "0.0.1"


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Terror",
    },
]


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data["user"] != "test":
            raise HTTPException(status_code=403, detail="Invalid Credentials")


@app.post("/login", tags=["auth"])
def login(user: User):
    if user.user == "test" and user.password == "password":
        tk: str = create_token(user.dict())
    return JSONResponse(status_code=200, content=tk)


@app.get("/", tags=["Home"])
def message():
    return HTMLResponse("<h1>Hello World !</1h>")


@app.get(
    "/movies",
    tags=["movies"],
    response_model=List[Movie],
    status_code=200,
    dependencies=[Depends(JWTBearer())],
)
def get_movies() -> List[Movie]:
    return JSONResponse(content=movies)


@app.get("/movies/{id}", tags=["movies"], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=200)) -> Movie:
    for movie in movies:
        if movie["id"] == id:
            return JSONResponse(status_code=200, content=movie)
    return JSONResponse(status_code=404, content=[])


@app.get("/movies/", tags=["movies"], response_model=List[Movie])
def get_movies_by_category(
    category: str = Query(min_length=5, max_length=15)
) -> List[Movie]:
    filtered_movies = []
    for movie in movies:
        if movie["category"] == category:
            filtered_movies.append(movie)
    return JSONResponse(content=filtered_movies)


@app.post("/movies", tags=["movies"], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    movies.append(movie.dict())
    return JSONResponse(status_code=201, content={"message": "Created Satisfactory"})


@app.put("/movies/{id}", tags=["movies"], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    for mov in movies:
        if mov["id"] == id:
            mov.update(movie.dict())
            mov.update({"id": id})

    return JSONResponse(status_code=200, content={"message": "Updated Satisfactory"})


@app.delete("/movies/{id}", tags=["movies"], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
    return JSONResponse(status_code=200, content={"message": "Deleted Satisfactory"})
