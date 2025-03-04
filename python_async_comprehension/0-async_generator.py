#!/usr/bin/env python3
"""A coroutine that yields a random number between 0 and 10, 10 times."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """A coroutine that yields a random number between 0 and 10, 10 times."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
