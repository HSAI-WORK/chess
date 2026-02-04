from pydantic import BaseSettings
from typing import List

class Settings(BaseSettings):
    CORS_ORIGINS: List[str] = ["*"]
    DATABASE_URL: str = "sqlite:///./dev.db"

settings = Settings()