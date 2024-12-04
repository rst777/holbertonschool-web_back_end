#!/usr/bin/env python3
"""
Module for creating and managing async tasks.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times and return list of delays.

    Args:
        n (int): Number of times to spawn task_wait_random
        max_delay (int): Maximum delay for each task

    Returns:
        List[float]: List of delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
