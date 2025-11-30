import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    MYSQL_URL: str = os.getenv("MYSQL_URL")  # mysql+pymysql://user:password@localhost/db
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    LLM_MODEL: str = "gpt-4o-mini"
    DATA_REPORT_DIR: str = "data/reports"
    DATA_TRANSCRIPT_DIR: str = "data/transcripts"

settings = Settings()
