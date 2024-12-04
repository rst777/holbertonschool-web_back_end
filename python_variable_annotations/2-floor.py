#!/usr/bin/env python3
"""
This module provides a function to compute the floor of a float.
"""


def floor(n: float) -> int:
    """
    Return the floor of the given float.

    Args:
        n (float): The float number to compute the floor of.

    Returns:
        int: The largest integer less than or equal to the float.
    """
    return int(n // 1)
