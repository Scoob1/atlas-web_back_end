#!/usr/bin/env python3
"""A coroutine that measures the total runtime of four async_comprehension calls."""
import asyncio
import time
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """A coroutine that measures the total runtime of four async_comprehension calls."""
    start_time = time.time()
    # Run four async_comprehension coroutines in parallel using asyncio.gather
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
