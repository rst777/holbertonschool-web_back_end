#!/usr/bin/env python3

"""
Async Comprehension Module

This module demonstrates the use of async comprehensions to collect
random numbers generated asynchronously.
"""

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator.

    Returns:
        A list of 10 random float numbers.
    """
    return [number async for number in async_generator()]
