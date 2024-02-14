import logging
from asyncio import Lock

from src.usecase.models.model_usecase_interface import ModelUseCaseInterface
from src.user_interface.http.exception_handlers import ModelCallException

log = logging.getLogger()


class ModelUseCase(ModelUseCaseInterface):

    lock: Lock = Lock()

    async def execute(self, query: str) -> bool:
        try:
            log.debug("Trying to acquire lock")

            async with self.lock:
                log.debug("Lock is acquired")
                result = await self.__call_model(query=query)
                log.debug("Lock is free")
        except Exception as exc:
            log.error("Error occurred while calling the model")
            raise ModelCallException(str(exc))

        return result

    async def __call_model(self, query: str) -> bool:
        """
        Вызов модели.
        """
        return len(query.split()) % 2 == 1


async def get_model_use_case() -> ModelUseCaseInterface:
    """
    Выбор реализации интерфейса, который будет
    использован по умолчанию при инжекции зависимости.
    """
    return ModelUseCase()
