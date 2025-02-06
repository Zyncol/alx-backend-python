#!/usr/bin/env python3
"""
a module for Task 9
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computing the length of a list of sequences.
    """
    return [(i, len(i)) for i in lst]
