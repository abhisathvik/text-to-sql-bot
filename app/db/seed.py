from sqlalchemy.orm import Session
from app.db.models import Movie


def seed_data(db: Session):
    if db.query(Movie).count() > 0:
        return

    movies = [
        Movie(name="Inception", genre="Sci-Fi"),
        Movie(name="Interstellar", genre="Sci-Fi"),
        Movie(name="The Dark Knight", genre="Action"),
        Movie(name="Avengers", genre="Action"),
        Movie(name="Titanic", genre="Romance"),
    ]

    db.add_all(movies)
    db.commit()