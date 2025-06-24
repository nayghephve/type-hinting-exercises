"""
THIS EXERCISE IS NOT MANDATORY
note: you may need to explore typing a bit more to finish hard mode

Define a decorator that wraps a function and returns a function with the same signature.

levels:
    easy - only type 'decorator' func and nothing inside it
    hard - type everything on 'decorator' and inside it
"""


def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
