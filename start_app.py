"""
This file contains code that is launched before launching the server.
"""
import asyncio

from managers.pool_managers import PoolManager
from retrievers.grammatical import PullentiAddressRetriever
import config


PullentiAddressRetriever.initialize()
_retr = PullentiAddressRetriever(None, inspect_regions=[77])

EXECUTOR = PoolManager(_retr, config.WORKERS_COUNT, PullentiAddressRetriever.initialize)


async def _initialize_workers(
        exc: PoolManager,
        n: int
):
    """
    This method is used to run initializer function for every user
    worker before launching server.This is required to avoid waiting
    for initialization during running each worker for the first time

    :param exc: PoolManager object that is used during inference
    :param n: number of workers to initialize
    :return: None
    """
    await asyncio.gather(*[
        exc.process_request('text to initialize each process') for _ in range(n)
    ])
