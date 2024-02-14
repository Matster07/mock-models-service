import logging

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.config import get_settings
from src.usecase.models.model_usecase import get_model_use_case
from src.usecase.models.model_usecase_interface import ModelUseCaseInterface

log = logging.getLogger()
audit = logging.getLogger("audit")

router = APIRouter(prefix=get_settings().URL_PREFIX)


class ModelExecutionResponseDto(BaseModel):
    result: bool


class ModelExecutionRequestDto(BaseModel):
    query: str


@router.post(
    path="/model/execute",
    response_model=ModelExecutionResponseDto,
    tags=["Model Executing Controller"],
    description="Endpoint для выполнения запроса к модели.",
)
async def apply(
    data: ModelExecutionRequestDto,
    use_case: ModelUseCaseInterface = Depends(get_model_use_case),
) -> ModelExecutionResponseDto:
    log.debug(f"Received query to call. Query: {data.query}")

    result = await use_case.execute(query=data.query)
    audit.info(f"Result of passing query {data.query} to model is {result}")

    return ModelExecutionResponseDto(result=result)
