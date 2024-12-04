#!/usr/bin/env python3
"""
This module provides a function to return the length of elements in a list.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple
    contains an element and its length.

    Args:
        lst (Iterable[Sequence]): A list (or any iterable)
        of sequences (like strings, lists, etc.).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        each containing an element and its length.
    """
    return [(i, len(i)) for i in lst]
