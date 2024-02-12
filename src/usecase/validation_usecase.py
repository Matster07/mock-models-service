import logging

from src.usecase.validation_usecase_interface import ValidationUseCaseInterface
from src.user_interface.http.exception_handlers import ValidationException

log = logging.getLogger()


class ValidationUseCase(ValidationUseCaseInterface):

    def validate(self, data: str) -> bool:
        log.debug(f"Validating string: {data}")

        try:
            result = self.__apply_model(data=data)
        except Exception as exc:
            raise ValidationException(str(exc))

        return result

    def __apply_model(self, data: str) -> bool:
        return len(data.split()) % 2 == 1


async def get_validation_use_case() -> ValidationUseCaseInterface:
    return ValidationUseCase()
