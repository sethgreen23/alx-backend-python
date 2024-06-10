#!/usr/bin/env python3
"""Asynchronous coroutine"""

import asyncio
import random
import time


async def wait_random(max_delay=10):
    """Asyncronous coroutine that waits for a random number of seconds"""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
