#!/usr/bin/env python3
"""
a module for Task 8
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creating a multiplier function.
    """
    return lambda x: x * multiplier
