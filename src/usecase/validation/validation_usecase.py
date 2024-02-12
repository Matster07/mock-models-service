import logging

from src.usecase.validation.validation_usecase_interface import ValidationUseCaseInterface
from src.user_interface.http.exception_handlers import ValidationException

log = logging.getLogger()


class ValidationUseCase(ValidationUseCaseInterface):
    def validate(self, data: str) -> bool:
        log.debug(f"Validating string: {data}")

        try:
            result = self.__apply_model(data=data)
        except Exception as exc:
            """
            В случае возникновения ошибки при валидации данных, ошибка оборачивается
            в кастомный ValidationException, который наследуется от HTTPException.
            """
            log.error(f"Error occurred while validating string: {data}")
            raise ValidationException(str(exc))

        return result

    def __apply_model(self, data: str) -> bool:
        """
        Модель валидации
        """
        return len(data.split()) % 2 == 1


async def get_validation_use_case() -> ValidationUseCaseInterface:
    """
    Выбор реализации интерфейса, которая будет
    использована по умолчанию при инжекции зависимости.
    """
    return ValidationUseCase()
