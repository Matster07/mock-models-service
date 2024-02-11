import logging
import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")

DEFAULT_ENV_FILE = "../.env"


class Settings(BaseSettings):
    PORT: int = 8000

    LOG_LEVEL: str = "info"


def find_dotenv() -> str:
    profile_env = os.getenv("PROFILE")

    return f"../.{profile_env}.env" if profile_env else DEFAULT_ENV_FILE


@lru_cache()
def get_settings() -> Settings:
    log.info("Loading config settings from the environment...")
    load_dotenv(dotenv_path=find_dotenv())
    return Settings()
