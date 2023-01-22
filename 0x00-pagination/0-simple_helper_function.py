#!/usr/bin/env python3
""" Simple helper function """


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
        page (int) - page number
        page_size (int) - Number of items/rows per page
    Return:
        tuple of (page, page_size)
    """
    final_size: int = page * page_size
    start_size: int = final_size - page_size
    return (start_size, final_size)
