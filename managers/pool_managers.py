"""
This file contains wrappers for ProcessPoolExecutor, that is
used for implementing manager/worker architecture
"""
from concurrent.futures import ProcessPoolExecutor
from typing import Callable
from asyncio import wrap_future


class PoolManager:
    def __init__(
            self,
            worker_function: Callable,
            workers_count: int = 3,
            worker_initializer: Callable = lambda: ...
    ):
        self._executor = ProcessPoolExecutor(
            max_workers=workers_count,
            initializer=worker_initializer
        )
        self._worker_function = worker_function

    async def process_request(self, text):
        result = await wrap_future(self._executor.submit(self._worker_function, text))
        # self._executor.shutdown(wait=False)
        return result

    def shutdown(self, wait=True):
        self._executor.shutdown(wait)
