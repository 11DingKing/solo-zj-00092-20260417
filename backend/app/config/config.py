import os
import secrets
from typing import Literal

from pydantic import AnyHttpUrl, EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env"),
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
    )

    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ENVIRONMENT: Literal["development", "test", "production"] = "development"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []
    PROJECT_NAME: str
    FIRST_SUPERUSER: EmailStr
    FIRST_SUPERUSER_PASSWORD: str

    MONGO_HOST: str
    MONGO_PORT: int
    MONGO_USER: str | None = None
    MONGO_PASSWORD: str | None = None
    MONGO_DB: str

    GOOGLE_CLIENT_ID: str | None = None
    GOOGLE_CLIENT_SECRET: str | None = None
    SSO_CALLBACK_HOSTNAME: str | None = None
    SSO_LOGIN_CALLBACK_URL: str | None = None


settings = Settings()  # type: ignore
