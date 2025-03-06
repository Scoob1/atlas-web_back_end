#!/usr/bin/env python3
"""Coroutine that waits for a random delay up to max_delay."""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Coroutine that waits for a random delay up to max_delay."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
