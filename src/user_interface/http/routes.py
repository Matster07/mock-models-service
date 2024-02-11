from fastapi import APIRouter

from src.application.validation_service import model
from src.user_interface.dto.validation_request_dto import ValidationRequestDto
from src.user_interface.dto.validation_response_dto import ValidationResponseDto

router = APIRouter(
    prefix="/api/v1"
)


@router.post("/model/apply", response_model=ValidationResponseDto)
async def apply(body: ValidationRequestDto) -> ValidationResponseDto:
    result = model(data=body.data)
    return ValidationResponseDto(result=result)
