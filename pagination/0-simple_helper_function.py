#!/usr/bin/env python3
"""
Pagination helper function.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns the start and end index for a given page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
