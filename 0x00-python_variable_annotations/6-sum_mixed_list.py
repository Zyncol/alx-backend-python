#!/usr/bin/env python3
"""
a module for Task 6
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Computing the sum of a list of integers and floating-point numbers.
    """
    return float(sum(mxd_lst))
