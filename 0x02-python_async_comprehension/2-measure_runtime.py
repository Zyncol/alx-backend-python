#!/usr/bin/env python3
'''
For the task 2
'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Executes async_comprehension 4 times and measures the
    execution time.
    '''
    stime = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    measur = time.time() - stime
    return measur
