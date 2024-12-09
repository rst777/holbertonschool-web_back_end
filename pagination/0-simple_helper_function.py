#!/usr/bin/env python3
"""
"Module containing a helper function for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end indexes for a given page.
    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of elements per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index
        and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
