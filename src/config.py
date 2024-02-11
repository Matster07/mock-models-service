import logging
import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

log = logging.getLogger()

DEFAULT_ENV_FILE = "../.env"


def find_dotenv() -> str:
    profile_env = get_profile()

    return f"../.{profile_env}.env" if profile_env != 'default' else DEFAULT_ENV_FILE


def get_profile() -> str:
    return os.getenv('PROFILE') if os.getenv('PROFILE') else 'default'


class Settings(BaseSettings):
    PORT: int = 8000
    URL_PREFIX: str = "/api/v1"
    LOG_LEVEL: str = "INFO"


@lru_cache()
def get_settings() -> Settings:
    load_dotenv(dotenv_path=find_dotenv())
    profile = get_profile()
    log.info(f"Application starting using %s profile", profile)
    return Settings()
