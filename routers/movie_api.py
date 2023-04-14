# FastApi
from fastapi import Path, Query, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import APIRouter

# Middlewares
from middlewares.jwt_bearer import JWTBearer

# ORM Sqlalchemy
from models.movie import Movie as MovieModel
from config.database import Session

# Data Validation - Pydantic
from schemas import Movie
from typing import List


router = APIRouter()


@router.get(
    "/movies",
    tags=["Movies"],
    response_model=List[Movie],
    status_code=200,
    dependencies=[Depends(JWTBearer())],
)
def get_movies() -> List[Movie]:
    db = Session()
    result = db.query(MovieModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@router.get(
    "/movies/{id}",
    tags=["Movies"],
    response_model=Movie,
    dependencies=[Depends(JWTBearer())],
)
def get_movie(id: int = Path(ge=1, le=200)) -> Movie:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movie not Found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@router.get(
    "/movies/",
    tags=["Movies"],
    response_model=List[Movie],
    dependencies=[Depends(JWTBearer())],
)
def get_movies_by_category(
    category: str = Query(min_length=5, max_length=15)
) -> List[Movie]:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.category == category).all()
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movies not Found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@router.post(
    "/movies",
    tags=["Movies"],
    response_model=dict,
    status_code=201,
    dependencies=[Depends(JWTBearer())],
)
def create_movie(movie: Movie) -> dict:
    db = Session()
    new_movie = MovieModel(**movie.dict())
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Created Satisfactory"})


@router.put(
    "/movies/{id}",
    tags=["Movies"],
    response_model=dict,
    status_code=200,
    dependencies=[Depends(JWTBearer())],
)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movie not Found"})
    result.update(movie.dict(exclude_unset=True))
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Updated Satisfactory"})


@router.delete(
    "/movies/{id}",
    tags=["Movies"],
    response_model=dict,
    status_code=200,
    dependencies=[Depends(JWTBearer())],
)
def delete_movie(id: int) -> dict:
    db = Session()
    query = db.query(MovieModel).filter(MovieModel.id == id)
    if not query.first():
        return JSONResponse(status_code=404, content={"message": "Movie not Found"})
    query.delete(synchronize_session=False)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Deleted Satisfactory"})
