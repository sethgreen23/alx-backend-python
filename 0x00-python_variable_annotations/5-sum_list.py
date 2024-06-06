#!/usr/bin/env python3
"""Module for adding two float variables"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum of list of floats"""
    sum = 0
    for value in input_list:
        sum += value
    return sum
