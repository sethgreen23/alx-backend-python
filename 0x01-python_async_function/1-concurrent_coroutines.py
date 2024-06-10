#!/usr/bin/env python3
"""Module to Execute multiple Coroutines at the same time"""

import asyncio
import time
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines at the same time"""
    lis = []
    for i in range(n):
        res = await wait_random(max_delay)
        lis.append(res)
    return sorted(lis)
