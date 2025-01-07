#!/usr/bin/env python3
"""
type-annotated function concat that takes a str1 and a str2 as args,
and returns a concat string.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concat two strings and returns the result.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concat string.
    """
    return str1 + str2
