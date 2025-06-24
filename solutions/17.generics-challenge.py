"""
THIS EXERCISE IS NOT MANDATORY
note: you may need to explore typing a bit more to finish hard mode

Define a decorator that wraps a function and returns a function with the same signature.

levels:
    easy - only type 'decorator' func and nothing inside it
    hard - type everything on 'decorator' and inside it
"""
from typing import Callable, TypeVar, ParamSpec

# easy
def decorator[T: Callable](func: T) -> T:
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


# hard
def decorator[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return func(*args, **kwargs)

    return wrapper
