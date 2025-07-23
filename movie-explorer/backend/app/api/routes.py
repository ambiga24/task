from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import movie as schemas
from app.crud import crud_movie
from app.db.database import get_db

router = APIRouter()

@router.get("/movies", response_model=List[schemas.MovieOut])
def read_movies(genre: str = None, actor: str = None, director: str = None, db: Session = Depends(get_db)):
    return crud_movie.get_movies(db, genre, actor, director)
