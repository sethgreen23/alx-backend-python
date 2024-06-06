#!/usr/bin/env python3
"""Module for adding two float variables"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the sum of list of integer and floats"""
    sum = 0
    for value in mxd_lst:
        sum += value
    return sum
