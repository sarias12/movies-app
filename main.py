from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from models import Movie

app = FastAPI()
app.title = "My First App with FastAPI"
app.version = "0.0.1"

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Terror'    
    } 
]


@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>Hello World !</1h>')

@app.get('/movies', tags=['movies'])
def get_movies():
    print(movies)
    return movies

@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for movie in movies:
        if movie['id'] == id: 
            return movie
    return []

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str):
    filtered_movies = []
    for movie in movies:
        if movie['category'] == category: 
            filtered_movies.append(movie)
    return filtered_movies

@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):

    movies.append(movie.dict())
    return movies

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):

    for mov in movies:
        if mov['id'] == id: 
            breakpoint()    
            mov.update(movie.dict())
            mov.update({'id': id})
            return mov

@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
    return movies