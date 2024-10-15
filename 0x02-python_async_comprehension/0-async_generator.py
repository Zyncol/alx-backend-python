#!/usr/bin/env python3
'''
For the task 0
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    it generates a sequence of 10 random numbers
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
