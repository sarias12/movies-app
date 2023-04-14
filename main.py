# FastApi
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from routers import movie_api, auth_api

# Middlewares
from middlewares import error_handler

# ORM Sqlalchemy
from config.database import Base, engine

# Data Validation - Pydantic
from schemas import User
from jwt_manager import create_token

app = FastAPI()
app.title = "My First App with FastAPI"
app.version = "0.0.1"
app.add_middleware(error_handler.ErrorHandler)


Base.metadata.create_all(bind=engine)


@app.get("/", tags=["Home"])
def message():
    return HTMLResponse("<h1>Welcome to Movies App!</1h>")


app.include_router(auth_api.router)
app.include_router(movie_api.router)
