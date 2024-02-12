import logging
from abc import ABC, abstractmethod

log = logging.getLogger()


class ValidationUseCaseInterface(ABC):
    """
    Интерфейс ответственный за валидацию входных данных в виде строки.
    """

    @abstractmethod
    def validate(self, data: str) -> bool:
        """
        Parameters:
            data (str): Строка для валидации

        Returns:
            bool: Результат применения модели к входной строке.
        """
        pass
