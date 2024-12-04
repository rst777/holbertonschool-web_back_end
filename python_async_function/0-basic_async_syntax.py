#!/usr/bin/env python3
"""
Module for generating random asynchronous delays.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Generate a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): Maximum delay in seconds. Defaults to 10.

    Returns:
        float: Random delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
