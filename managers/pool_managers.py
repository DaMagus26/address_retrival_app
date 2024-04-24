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
        with self._executor as exctr:
            result = await wrap_future(exctr.submit(self._worker_function, text))
            print(result)
