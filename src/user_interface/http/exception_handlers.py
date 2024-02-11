import logging

from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError, HTTPException
from pydantic import BaseModel
from starlette.responses import JSONResponse

log = logging.getLogger()


class ValidationException(HTTPException):

    def __init__(self, detail):
        super().__init__(
            status_code=400,
            detail=detail
        )


class ApiError(BaseModel):
    msg: str
    type: str = None
    input: str | int | bool | dict | None = None


class ApiErrorResponse(BaseModel):
    errors: list[ApiError]


async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    errors = [ApiError(type=error['type'], msg=error['msg'], input=str(error['input'])) for error in exc.errors()]
    content = jsonable_encoder(ApiErrorResponse(errors=errors))
    log.error(content)
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=content
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    errors = [ApiError(msg=exc.detail)]
    content = jsonable_encoder(ApiErrorResponse(errors=errors))
    log.error(content)
    return JSONResponse(
        status_code=exc.status_code,
        content=content
    )
