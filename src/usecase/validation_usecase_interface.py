import logging
from abc import ABC, abstractmethod

log = logging.getLogger()


class ValidationUseCaseInterface(ABC):

    @abstractmethod
    def validate(self, data: str) -> bool:
        pass

