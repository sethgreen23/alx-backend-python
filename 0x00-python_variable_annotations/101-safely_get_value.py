#!/usr/bin/env python3
"""Module for adding two float variables"""
from typing import Mapping, Any, Union, TypeVar


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'),
                                    None] = None) -> Union[Any, TypeVar('T')]:
    """Function to anotate"""
    if key in dct:
        return dct[key]
    else:
        return default
