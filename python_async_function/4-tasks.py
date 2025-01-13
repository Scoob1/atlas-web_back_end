#!/usr/bin/env python3
"""nearly identical to wait_n except task_wait_random is being called"""

import asyncio
import importlib.util
from typing import List

spec = importlib.util.spec_from_file_location(
    "wait_random", "./0-basic_async_syntax.py"
)
wait_random_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wait_random_module)

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns n task_wait_random coroutines and returns
    their delays in ascending order.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay for each task.

    Returns:
        list: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
