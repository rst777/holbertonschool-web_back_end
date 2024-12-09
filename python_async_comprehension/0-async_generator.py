#!/usr/bin/env python3

"""
Asynchronous Generator Module

This module provides an asynchronous generator that yields random float numbers

Functions:
    - async_generator(): Generates 10 random float numbers asynchronously
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """
    A coroutine that yields 10 random numbers between 0 and 10.
    Each yield is preceded by an asynchronous wait of 1 second.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
