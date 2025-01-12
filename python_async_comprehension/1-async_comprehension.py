#!/usr/bin/env python3
"""A coroutine that collects 10 random numbers from async_generator."""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """A coroutine that collects 10 random numbers from async_generator."""
    return [num async for num in async_generator()]
