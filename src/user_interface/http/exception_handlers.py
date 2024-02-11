import logging

from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import RequestValidationError

log = logging.getLogger("uvicorn")


async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    return JSONResponse(
        content={"msg": exc.json()},
        status_code=403
    )
