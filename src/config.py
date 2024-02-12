import logging
import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

log = logging.getLogger()

DEFAULT_ENV_FILE = "../.env"


def __find_dotenv() -> str:
    """
    Конструируем путь до env файла с учетом был ли указан профиль в переменных среды.
    """

    env_file = DEFAULT_ENV_FILE
    profile_env = __get_profile()

    if profile_env == "default":
        env_file = f"../.{profile_env}.env"

    return env_file


def __get_profile() -> str:
    profile = os.getenv("PROFILE")
    return profile if profile is not None else "default"


class Settings(BaseSettings):
    URL_PREFIX: str = "/api/v1"
    LOG_LEVEL: str = "INFO"


@lru_cache()
def get_settings() -> Settings:
    load_dotenv(dotenv_path=__find_dotenv())
    profile = __get_profile()
    log.info(f"Application starting using {profile} profile")
    return Settings()
