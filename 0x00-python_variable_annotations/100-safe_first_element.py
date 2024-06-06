#!/usr/bin/env python3
"""Module for adding two float variables"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function to anotate"""
    if lst:
        return lst[0]
    else:
        return None
