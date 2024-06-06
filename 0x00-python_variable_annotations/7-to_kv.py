#!/usr/bin/env python3
"""Module for adding two float variables"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function to add two floats"""
    return (k, v * v)
