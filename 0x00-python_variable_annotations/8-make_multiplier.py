#!/usr/bin/env python3
"""Module for adding two float variables"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function to add two floats"""
    def multiply(a: float) -> float:
        """Function to add two floats"""
        return multiplier * a  
    return multiply
