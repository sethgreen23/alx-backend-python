#!/usr/bin/env python3
"""Asynchronous coroutine"""

import asyncio
import random


async def wait_random(max_delay=10):
    """Asyncronous coroutine"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return max_delay
