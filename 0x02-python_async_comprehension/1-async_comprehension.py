#!/usr/bin/env python3
'''
For the task 1
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    it creates a list of 10 numbers from 10-number generator
    '''
    gener = [num async for num in async_generator()]
    return gener
