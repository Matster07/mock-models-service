from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from src.user_interface.http.exception_handlers import validation_exception_handler
from src.user_interface.http.routes import router


def create_application() -> FastAPI:
    application = FastAPI(
        openapi_url="/openapi.json",
        docs_url="/docs")
    application.include_router(
        router=router
    )
    application.add_exception_handler(RequestValidationError, validation_exception_handler)
    return application
