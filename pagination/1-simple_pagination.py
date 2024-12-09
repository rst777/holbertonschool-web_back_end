#!/usr/bin/env python3
"""
Simple Pagination Module

This module provides functionality for paginating a dataset of
popular baby names.
It includes a helper function for calculating index ranges and a Server class
for managing dataset pagination.

Functions:
    - index_range(page: int, page_size: int) -> Tuple[int, int]:
        Calculates start and end indexes for pagination.

Classes:
    - Server: Manages pagination of baby names dataset
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indexes for pagination.

    This function determines the correct slice indexes for a given page
    and page size in a paginated dataset.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing start and end indexes.

    Example:
        >>> index_range(1, 7)
        (0, 7)
        >>> index_range(3, 15)
        (30, 45)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.

    This class provides methods to load and paginate a CSV dataset
    of baby names, with caching mechanism for efficient data access.

    Attributes:
        DATA_FILE (str): Path to the CSV file containing baby names data.
        __dataset (List[List] | None): Cached dataset, initially None.

    Methods:
        dataset(): Load and return the dataset from CSV file.
        get_page(page: int = 1, page_size: int = 10):
            Return a specific page of the dataset.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server instance.

        Sets the initial dataset to None, which will be loaded
        lazily when first accessed.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieve the dataset with caching mechanism.

        Loads the dataset from CSV file only once and caches it
        for subsequent calls. Skips the header row.

        Returns:
            List[List]: A list of rows from the dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page from the dataset.

        Validates input parameters and returns the corresponding
        page of data using index_range.

        Args:
            page (int, optional): Page number to retrieve. Defaults to 1.
            page_size (int, optional): Number of items per page. Defaults to 10

        Returns:
            List[List]: A list of rows for the specified page.

        Raises:
            AssertionError: If page or page_size are not positive integers.

        Example:
            >>> server = Server()
            >>> server.get_page(1, 3)
            [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER',
            'Olivia', '172', '1'], ...]
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []

        return dataset[start:end]
