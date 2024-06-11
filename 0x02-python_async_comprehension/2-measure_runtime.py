#!/usr/bin/env python3
"""Loop 10 times each time asyncronously wait 1 second"""
import asyncio
from typing import Generator, List
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Loop 10 times each time asyncronously wait 1 second"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
