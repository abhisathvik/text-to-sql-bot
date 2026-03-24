import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,  # deterministic output
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


# 🔹 Static schema (can be dynamic later)
SCHEMA = """
Table: movies
Columns:
- id (integer)
- name (text)
- genre (text)
- created_at (datetime)
"""


# 🔹 Codex-style prompt template
PROMPT_TEMPLATE = """
You are a senior SQL engineer and database expert.

Your task is to convert a user's natural language question into a syntactically correct SQL query.

DATABASE SCHEMA:
{schema}

STRICT RULES:

- Return ONLY SQL query
- No explanation
- No markdown
- Only SELECT queries
- No INSERT, UPDATE, DELETE, DROP
- Use ORDER BY created_at DESC for recent queries
- Use LIMIT when needed (default 10)
- Use only given schema

USER QUESTION:
{question}

FINAL OUTPUT:
"""


def generate_sql(user_query: str) -> str:
    """
    Convert natural language to SQL using Gemini
    """

    # Inject schema + question into prompt
    prompt = PROMPT_TEMPLATE.format(
        schema=SCHEMA,
        question=user_query
    )

    try:
        response = llm.invoke(prompt)

        sql_query = response.content.strip()

        # 🔐 Safety Check
        if not sql_query.lower().startswith("select"):
            raise ValueError("Unsafe query generated")

        return sql_query

    except Exception as e:
        raise Exception(f"LLM Error: {str(e)}")