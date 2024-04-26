import asyncio

from managers.pool_managers import PoolManager
from retrievers.grammatical import PullentiAddressRetriever
import config


PullentiAddressRetriever.initialize()
# _retr = PullentiAddressRetriever(config.REGISTRY_PATH, inspect_regions=[77])
_retr = PullentiAddressRetriever(None, inspect_regions=[77])

EXECUTOR = PoolManager(_retr, config.WORKERS_COUNT, PullentiAddressRetriever.initialize)


async def _initialize_workers(exc, n):
    await asyncio.gather(*[
        exc.process_request('text to initialize each process') for _ in range(n)
    ])
