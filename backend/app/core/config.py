from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Realtime AI Interpreter"
    app_version: str = "0.1.0"
    environment: str = "development"

    database_url: str
    redis_url: str

    stt_provider: str = "gemini"
    translation_provider: str = "gemini"
    tts_provider: str = "gemini"

    gemini_api_key: str
    gemini_translation_model: str = "gemini-3.5-flash"
    gemini_stt_model: str = "gemini-3.5-flash"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
