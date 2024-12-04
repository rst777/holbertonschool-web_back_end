#!/usr/bin/env python3
"""
This module provides a function to compute the sum of a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Compute and return the sum of a list of floats.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of the float numbers in the list.
    """
    return sum(input_list)
