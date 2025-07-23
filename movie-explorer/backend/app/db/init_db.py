# app/db/init_db.py
from app.db.database import Base, engine
from app.models import movie, actor, director, genre
from app.db.database import init_db

# Run this to create all tables
@app.on_event("startup") # type: ignore
def on_startup():
    init_db()

