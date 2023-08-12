import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):

    
    __DB_USER = os.getenv("DB_USER")
    __DB_PASSWORD = os.getenv("DB_PASSWORD")
    __DB_HOST = os.getenv("DB_HOST")
    __DB_NAME = os.getenv("DB_NAME")


    SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{__DB_USER}:{__DB_PASSWORD}@{__DB_HOST}:5432/{__DB_NAME}"
    TEST_DB_NAME = os.getenv("TEST_DB_NAME")
    TEST_SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{__DB_USER}:{__DB_PASSWORD}@{__DB_HOST}:5432/{TEST_DB_NAME}"
    MAX_PER_PAGE = 10


settings = Settings()