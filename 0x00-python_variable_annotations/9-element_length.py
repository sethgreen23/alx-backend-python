#!/usr/bin/env python3
"""Module for adding two float variables"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """"Function to anotate"""
    return [(i, len(i)) for i in lst]
