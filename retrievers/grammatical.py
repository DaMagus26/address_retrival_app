"""
This file contains classes for object
"""

from pathlib import Path
from typing import Optional, List

from retrievers.base import BaseAddressRetriever
from pullenti.address.ProcessTextParams import ProcessTextParams
from pullenti.address.AddressService import AddressService


class PullentiAddressRetriever(BaseAddressRetriever):
    __initialized: bool = False

    def __init__(
            self,
            address_registry_path: Optional[str] = None,
            inspect_regions: Optional[List[int]] = None
    ):
        inspect_regions = inspect_regions or []

        if address_registry_path:
            if isinstance(address_registry_path, str) and not Path(address_registry_path).is_dir():
                raise FileNotFoundError(f'Address registry path "{address_registry_path}" does not exist')

            AddressService.set_gar_index_path(address_registry_path)
            self._info = AddressService.get_gar_statistic()

            if self._info:
                print(self._info)

        self._pars = ProcessTextParams()
        for reg in inspect_regions:
            self._pars.default_regions.append(reg)

    @classmethod
    def initialize(cls):
        print(f'Initialize SDK Pullenti Address v.{AddressService.VERSION} ... ', end="")
        AddressService.initialize()
        print('OK!')
        cls.__initialized = True

    def __call__(
            self,
            text: str
    ) -> List[str]:
        return self.retrieve(text)

    def retrieve(
            self,
            text: str
    ) -> List[str]:

        if not self.__initialized:
            raise RuntimeError(
                f'{self.__class__.__name__} must be initialized before running. Try `{self.__class__.__name__}.initialize()`'
            )

        addrs = AddressService.process_text(text, self._pars)

        result = [addr.get_full_path(', ') for addr in addrs]

        return result
