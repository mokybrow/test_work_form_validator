from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(
    BaseSettings,
):
    project_name: str


    class Config:
        env_prefix = 'FORM_'
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()