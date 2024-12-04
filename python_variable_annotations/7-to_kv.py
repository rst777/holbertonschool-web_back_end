#!/usr/bin/env python3
"""
This module provides a function to return a tuple with
a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string `k` and the square of the number `v`.

    Args:
        k (str): The string key.
        v (Union[int, float]): The value to square, which
        can be an integer or a float.

    Returns:
        Tuple[str, float]: A tuple where the first element is `k`
        and the second is the square of `v` as a float.
    """
    return (k, float(v**2))
