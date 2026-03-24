from sqlalchemy.orm import Session
from sqlalchemy import text


def execute_sql(query: str, db: Session):
    """
    Execute SQL query safely and return results
    """

    try:
        # 🔐 Extra safety (double check)
        if not query.lower().strip().startswith("select"):
            raise ValueError("Only SELECT queries are allowed")

        result = db.execute(text(query))

        rows = result.fetchall()
        columns = result.keys()

        # Convert to list of dicts
        data = [dict(zip(columns, row)) for row in rows]

        return data

    except Exception as e:
        raise Exception(f"SQL Execution Error: {str(e)}")