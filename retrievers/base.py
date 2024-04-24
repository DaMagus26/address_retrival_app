from typing import Optional, List
from abc import ABC, abstractmethod


class BaseAddressRetriever(ABC):
    @abstractmethod
    def __call__(
            self,
            text: str
    ) -> List[str]:
        pass

    @abstractmethod
    def retrieve(
            self,
            text: str
    ) -> List[str]:
        pass
