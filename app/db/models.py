from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)