#!/usr/bin/env python3
"""
Type-annotated function to_kv
that returns a tuple containing a string and the square of a num.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of a number as a float.
    """
    return (k, float(v ** 2))
