import uvicorn

from src.logging_config import logging_config
from src.user_interface.http.app import create_application

app = create_application()

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        port=8000,
        host="0.0.0.0",
        reload=False,
        log_config=logging_config,
        access_log=False,
    )
