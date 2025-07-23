# movie.py
from pydantic import BaseModel
from typing import List

class MovieBase(BaseModel):
    title: str
    release_year: int

class MovieCreate(MovieBase):
    director_id: int
    genre_ids: List[int]
    actor_ids: List[int]

class MovieOut(MovieBase):
    id: int
    director: str
    genres: List[str]
    actors: List[str]

    class Config:
        orm_mode = True
class Movie(BaseModel):
    title: str
    year: int

    class Config:
        schema_extra = {
            "example": {
                "title": "Inception",
                "year": 2010
            }
        }
