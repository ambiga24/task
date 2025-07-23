# app/db/dependency.py
from app.db.database import SessionLocal
from sqlalchemy.orm import Session

# Dependency injection for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
