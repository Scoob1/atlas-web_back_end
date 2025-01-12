#!/usr/bin/env python3
"""Module that spawns multiple wait_random coroutines concurrently."""

import asyncio
from 0_basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Spawns n wait_random coroutines and returns their delays in ascending order.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        list: List of delays in ascending order.
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return delays
