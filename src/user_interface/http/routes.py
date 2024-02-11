import logging

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.config import get_settings
from src.usecase.validation_usecase import get_validation_use_case
from src.usecase.validation_usecase_interface import ValidationUseCaseInterface

log = logging.getLogger()

router = APIRouter(prefix=get_settings().URL_PREFIX)


class ValidationResponseDto(BaseModel):
    result: bool


class ValidationRequestDto(BaseModel):
    data: str


@router.post("/text/validate", response_model=ValidationResponseDto)
async def apply(
        data: ValidationRequestDto,
        use_case: ValidationUseCaseInterface = Depends(get_validation_use_case)
) -> ValidationResponseDto:
    log.debug(f"Received request to validate string: %s", data.data)

    result = use_case.validate(data=data.data)
    log.info(f"Result of applying model to string: %s - %s", data, result)

    return ValidationResponseDto(result=result)
