import uvicorn

from src.config import get_settings
from src.logging_config import logging_config
from src.user_interface.http.app import create_application

app = create_application()

if __name__ == "__main__":
    port = get_settings().PORT

    uvicorn.run(
        app="main:app",
        port=get_settings().PORT,
        reload=False,
        log_config=logging_config,
        access_log=False
    )
