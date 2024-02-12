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


@router.post(
    path="/text/validate",
    response_model=ValidationResponseDto,
    tags=["Text Validation Controller"],
    description="Endpoint для проверки строки при помощи заданной модели.",
)
async def apply(
    data: ValidationRequestDto,
    use_case: ValidationUseCaseInterface = Depends(get_validation_use_case),
) -> ValidationResponseDto:
    log.debug(f"Received request to validate string: {data.data}", data.data)

    result = use_case.validate(data=data.data)
    log.info(f"Result of applying model to string: {data.data} - {result}")

    return ValidationResponseDto(result=result)
