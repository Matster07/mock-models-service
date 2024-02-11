from pydantic import BaseModel


class ValidationResponseDto(BaseModel):
    result: bool
