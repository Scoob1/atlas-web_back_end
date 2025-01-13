#!/usr/bin/env python3
"""Measures the total runtime of four async_comprehension calls."""
import asyncio
import time
import importlib

from typing import List


async_comprehension = importlib.import_module(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime of four async_comprehension calls."""
    start_time = time.time()

    # Run four async_comprehension coroutines in parallel using asyncio.gather
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.time()
    return end_time - start_time

# Run the measure_runtime function and print the result
if __name__ == "__main__":
    runtime = asyncio.run(measure_runtime())
    print(f"Total runtime: {runtime} seconds")
