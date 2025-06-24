"""
TODO:

Define a generic class that represents a stack.
It can be instantiated with a certain type, with method `push` accepting an object of the specified type,
and `pop` returning an an object of the same type
"""


class Stack:
    def __init__(self) -> None:
        self.items: list = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
