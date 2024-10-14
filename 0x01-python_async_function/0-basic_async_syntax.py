#!/usr/bin/env python3
'''
it waits for random number
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    it Waits for random number of seconds.
    '''
    wtime = random.random() * max_delay
    await asyncio.sleep(wtime)
    return wtime
