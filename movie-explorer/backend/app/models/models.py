# movie.py
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.database import Base


movie_genre = Table(
    'movie_genre', Base.metadata,
    Column('movie_id', ForeignKey('movies.id')),
    Column('genre_id', ForeignKey('genres.id'))
)

movie_actor = Table(
    'movie_actor', Base.metadata,
    Column('movie_id', ForeignKey('movies.id')),
    Column('actor_id', ForeignKey('actors.id'))
)

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_year = Column(Integer)
    director_id = Column(Integer, ForeignKey('directors.id'))

    director = relationship("Director", back_populates="movies")
    genres = relationship("Genre", secondary=movie_genre, back_populates="movies")
    actors = relationship("Actor", secondary=movie_actor, back_populates="movies")



class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)

