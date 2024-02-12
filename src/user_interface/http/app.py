from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException

from src.user_interface.http.exception_handlers import validation_exception_handler
from src.user_interface.http.exception_handlers import http_exception_handler
from src.user_interface.http.routes import router


def create_application() -> FastAPI:
    app = FastAPI(openapi_url="/openapi.json", docs_url="/docs")
    app.include_router(router=router)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    return app
