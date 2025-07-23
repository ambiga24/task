# crud_movie.py
from sqlalchemy.orm import Session
from app.models import movie as models
from app.schemas import movie as schemas

def get_movies(db: Session, genre=None, actor=None, director=None):
    query = db.query(models.Movie)
    if genre:
        query = query.join(models.Movie.genres).filter(models.Genre.name == genre)
    if actor:
        query = query.join(models.Movie.actors).filter(models.Actor.name == actor)
    if director:
        query = query.join(models.Movie.director).filter(models.Director.name == director)
    return query.all()
