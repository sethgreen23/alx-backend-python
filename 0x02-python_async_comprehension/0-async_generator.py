#!/usr/bin/env python3
"""Loop 10 times each time asyncronously wait 1 second"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """Loop 10 times each time asyncronously wait 1 second"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
