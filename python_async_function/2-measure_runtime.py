#!/usr/bin/env python3
"""
Module to measure runtime of async tasks.
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure total execution time for wait_n and return average time per task.

    Args:
        n (int): Number of tasks
        max_delay (int): Maximum delay for each task

    Returns:
        float: Average time per task
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
