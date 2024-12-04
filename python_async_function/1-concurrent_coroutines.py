#!/usr/bin/env python3
"""
Module for concurrent execution of async random delay tasks.
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times and return list of delays.

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay for each wait_random call

    Returns:
        List[float]: List of delays in ascending order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
