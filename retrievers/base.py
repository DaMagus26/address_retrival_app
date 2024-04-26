"""
Abstract and base classes for address retriever models. Supposed to provide single interface, when using different algorithms for address retrieval
"""

from typing import List
from abc import ABC, abstractmethod


class BaseAddressRetriever(ABC):
    @abstractmethod
    def __call__(
            self,
            text: str
    ) -> List[str]:
        """
        Used to adapt BaseAddressRetriever class for ProcessPoolExecutor. Meant to call self.retrieve method.
        :param text: input text
        :return: list of found address lines
        """
        pass

    @abstractmethod
    def retrieve(
            self,
            text: str
    ) -> List[str]:
        """

        :param text: input text
        :return: list of found address lines
        """
        pass
