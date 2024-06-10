#!/usr/bin/env python3
"""Asynchronous coroutine"""

import asyncio
import random
import time


async def wait_random(max_delay: int=10) -> float:
    """Asyncronous coroutine that waits for a random number of seconds"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
