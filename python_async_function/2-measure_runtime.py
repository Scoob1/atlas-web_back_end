#!/usr/bin/env python3

"""
Module to measure the execution time of the wait_n function.
"""

import time
import asyncio
import importlib.util

spec = importlib.util.spec_from_file_location(
    "wait_n", "./1-concurrent_coroutines.py"
)
wait_n_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wait_n_module)


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n_module.wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
