from fastapi import FastAPI
from app.api.routes import movies

app = FastAPI(title="Movie Explorer")

app.include_router(movies.router, prefix="/api")

# Swagger UI available at /docs
app = FastAPI(
    title="Movie Explorer",
    description="Explore movies, genres, actors, and directors.",
    version="1.0.0",
    openapi_tags=[
        {"name": "Movies", "description": "Movie-related endpoints"},
        {"name": "Genres", "description": "Genre-related endpoints"}
    ]
)