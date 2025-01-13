#!/usr/bin/env python3
"""function that takes an integer max_delay and returns a asyncio.Task"""

import asyncio
import importlib.util

spec = importlib.util.spec_from_file_location(
    "wait_random", "./0-basic_async_syntax.py"
)
wait_random_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wait_random_module)


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task that runs
    the wait_random function.

    Args:
        max_delay (int): Maximum delay for wait_random.

    Returns:
        asyncio.Task: A Task that runs the wait_random function.
    """
    return asyncio.create_task(wait_random_module.wait_random(max_delay))
