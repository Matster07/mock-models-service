import logging
from abc import ABC, abstractmethod

log = logging.getLogger()


class ModelUseCaseInterface(ABC):
    """
    Интерфейс для обращения к модели.
    """

    @abstractmethod
    async def execute(self, query: str) -> bool:
        """
        Parameters:
            query (str): Входной запрос.

        Returns:
            bool: Результат обращения к модели.
        """
        pass
