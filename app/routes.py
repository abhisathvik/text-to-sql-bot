from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.llm_service import generate_sql
from app.services.sql_service import execute_sql

router = APIRouter()


@router.post("/query")
def query_endpoint(request: dict, db: Session = Depends(get_db)):
    try:
        user_question = request.get("question")

        # Step 1: Generate SQL
        sql_query = generate_sql(user_question)

        # Step 2: Execute SQL
        result = execute_sql(sql_query, db)

        # Step 3: Return only data
        return {"data": result}

    except Exception as e:
        return {"error": str(e)}