# Application configuration (env variables)
# Sample configuration file for environment variables.

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / "config" / f"{os.getenv('ENVIRONMENT', 'dev')}.env")

class Config:
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", 8000))
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
