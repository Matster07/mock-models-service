from pydantic import BaseModel


class ValidationRequestDto(BaseModel):
    data: str
