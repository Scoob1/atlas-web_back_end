#!/usr/bin/env python3
"""
Type-annotated function that calculates the sum of a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of the list elements.
    """
    return sum(input_list)
