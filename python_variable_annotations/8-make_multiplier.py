#!/usr/bin/env python3
"""
Type-annotated funct make_multiplier that returns a multiplier funct.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a funct that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
