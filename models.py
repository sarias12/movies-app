from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] | None = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(ge=1900, le=2022)
    rating: float = Field( ge=0, le=10)
    category:str = Field(min_length=5, max_length=20)

    class Config:
        schema_extra = {
            "example": {
                "id": 99,
                "title": 'Title Example',
                "overview": "Summary example for the movie",
                "year": 2021,
                "rating": 0,
                "category":"Without category",
            }
        }

class User(BaseModel):
    user: str
    password: str