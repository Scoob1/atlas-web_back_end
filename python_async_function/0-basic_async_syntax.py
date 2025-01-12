#!/usr/bin/env python3
import asyncio
import random

def wait_random(max_delay: int = 10) -> float:
    """Asynch coroutine that waits for a random delay between 0 and max_delay seconds."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
