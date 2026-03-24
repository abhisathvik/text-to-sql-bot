from app.services.llm_service import generate_sql
from app.services.sql_service import execute_sql
from app.db.database import SessionLocal

def main():
    db = SessionLocal()

    while True:
        user_input = input("\nEnter your query (or 'exit'): ")

        if user_input.lower() == "exit":
            break

        try:
            # Step 1: NL → SQL
            sql_query = generate_sql(user_input)
            print(f"\n[DEBUG SQL]: {sql_query}")  # optional (for debugging)

            # Step 2: SQL → DB
            result = execute_sql(sql_query, db)

            # Step 3: Output
            print("\nResult:")
            for row in result:
                print(row)

        except Exception as e:
            print(f"\nError: {e}")

    db.close()


if __name__ == "__main__":
    main()