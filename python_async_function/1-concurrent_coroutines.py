#!/usr/bin/env python3
"""Module that spawns multiple wait_random coroutines concurrently."""

import asyncio
import importlib.util
from typing import List

spec = importlib.util.spec_from_file_location(
    "wait_random", "./0-basic_async_syntax.py"
)
wait_random_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wait_random_module)


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns n wait_random coroutines and returns delays in ascending order.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = await asyncio.gather(
        *(wait_random_module.wait_random(max_delay) for _ in range(n))
        )
    return sorted(delays)
