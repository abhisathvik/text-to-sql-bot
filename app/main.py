from fastapi import FastAPI
from app.routes import router
from app.db.database import engine, Base, SessionLocal
from app.db import models
from app.db.seed import seed_data


def create_app() -> FastAPI:
    app = FastAPI(
        title="Text-to-SQL Chatbot",
        version="1.0.0"
    )

    # Create tables
    Base.metadata.create_all(bind=engine)

    # ✅ FIX: startup event inside function
    @app.on_event("startup")
    def startup_event():
        db = SessionLocal()
        seed_data(db)
        db.close()

    app.include_router(router)

    return app


app = create_app()


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "API is running 🚀"
    }