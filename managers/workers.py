from typing import Optional, List

from managers.base import BaseWorker
from retrievers.grammatical import PullentiAddressRetriever


class PullentiRetrieverWorker(BaseWorker):
    def __init__(
            self,
            address_registry_path: Optional[str] = None,
            inspect_regions: Optional[List[int]] = None
    ):
        self.initialize()
        self._retriever = PullentiAddressRetriever(address_registry_path, inspect_regions=inspect_regions)

    def initialize(self):
        PullentiAddressRetriever.initialize()

    def __call__(
            self,
            text: str
    ) -> List[str]:
        return self._retriever(text)
