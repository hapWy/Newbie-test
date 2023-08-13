import os
from typing import ClassVar
from dotenv import load_dotenv

from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):

    
    __DB_USER: ClassVar[str] = os.getenv("DB_USER")
    __DB_PASSWORD: ClassVar[str] = os.getenv("DB_PASSWORD")
    __DB_HOST: ClassVar[str] = os.getenv("DB_HOST")
    __DB_NAME: ClassVar[str] = os.getenv("DB_NAME")


    SQLALCHEMY_DATABASE_URL: ClassVar[str] = f"postgresql+asyncpg://{__DB_USER}:{__DB_PASSWORD}@{__DB_HOST}:5432/{__DB_NAME}"
    TEST_DB_NAME: ClassVar[str] = os.getenv("TEST_DB_NAME")
    TEST_SQLALCHEMY_DATABASE_URL: ClassVar[str] = f"postgresql+asyncpg://{__DB_USER}:{__DB_PASSWORD}@{__DB_HOST}:5432/{TEST_DB_NAME}"
    MAX_PER_PAGE: ClassVar[int] = 10


settings = Settings()