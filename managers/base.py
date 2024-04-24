from abc import ABC, abstractmethod
from typing import Any


class BaseWorker(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs) -> Any:
        pass

    def initialize(self):
        pass
