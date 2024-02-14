import os
from logging import Filter, LogRecord

from src.config import get_settings

FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


class BadDefaultFastApiLogNameFilter(Filter):
    """
    Фильтр подмены названия логов от FastAPI, т.к. у них не лучший нейминг.
    """

    def filter(self, record: LogRecord) -> bool:
        if record.name == "uvicorn.error" or record.name == "uvicorn.access":
            record.name = "fastapi"

        return True


logging_config: dict = {
    "version": 1,
    "filters": {
        "default.fastapi.log.name.filter": {
            "()": lambda: BadDefaultFastApiLogNameFilter()
        }
    },
    "formatters": {
        "basic": {
            "format": FORMAT,
        },
    },
    "handlers": {
        "console": {
            "formatter": "basic",
            "filters": ["default.fastapi.log.name.filter"],
            "class": "logging.StreamHandler",
        },
        "audit_handler": {
            "formatter": "basic",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.abspath(os.getcwd()) + "/../logs/info.log",
            "mode": "a",
            "maxBytes": 1048576,
            "backupCount": 10,
        },
    },
    "root": {
        "handlers": ["console"],
        "level": get_settings().LOG_LEVEL,
        "propagate": False,
    },
    "loggers": {
        "uvicorn.access": {
            "handlers": ["console"],
            "level": get_settings().LOG_LEVEL,
            "propagate": False,
        },
        "uvicorn.error": {
            "handlers": ["console"],
            "level": get_settings().LOG_LEVEL,
            "propagate": False,
        },
        "audit": {
            "handlers": ["console", "audit_handler"],
            "level": get_settings().LOG_LEVEL,
            "propagate": False,
        },
    },
}
