import logging

import uvicorn

from src.config import get_settings
from src.user_interface.http.app import create_application


app = create_application()


log = logging.getLogger("uvicorn")

if __name__ == "__main__":
    port = get_settings().PORT

    uvicorn.run(
        app="main:app",
        port=get_settings().PORT,
        reload=True
    )


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
