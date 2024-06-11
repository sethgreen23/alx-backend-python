#!/usr/bin/env python3
"""Loop 10 times each time asyncronously wait 1 second"""
import asyncio
from typing import Generator, List
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Loop 10 times each time asyncronously wait 1 second"""
    return [i async for i in async_generator()]
