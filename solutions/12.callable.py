"""
TODO:

foo should accept a callable argument that accepts an integer and returns a string.
"""
from typing import Callable


def foo(x: Callable[[int], str]):
    ...