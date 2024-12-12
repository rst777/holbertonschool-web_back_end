#!/usr/bin/env python3

"""
Runtime Measurement Module

This module provides a function to measure the runtime of parallel
execution of async comprehensions.
"""


import asyncio
import time
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    and measures the total runtime.

    Returns:
        The total runtime in seconds.
    """
    start_time = time.time()

    task = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*task)

    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime
