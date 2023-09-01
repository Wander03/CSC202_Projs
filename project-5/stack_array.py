from typing import Optional, List, Any

# Stack class implemented with array
class Stack:
    """Implements an efficient last-in first-out Abstract Data Type using a Python List"""

    # capacity is max number of Nodes, init_items is optional List parameter for initialization
    # if the length of the init_items List exceeds capacity, raise IndexError
    def __init__(self, capacity: int, init_items: Optional[List] = None):
        """Creates an empty stack with a capacity"""
        self.capacity = capacity        # capacity of stack
        self.items = [None]*capacity    # array for stack
        self.num_items = 0              # number of items in stack
        if init_items is not None:      # if init_items is not None, initialize stack
            if len(init_items) > capacity:
                raise IndexError
            else:
                self.num_items = len(init_items)
                self.items[:self.num_items] = init_items

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Stack):
            return (self.capacity == other.capacity
            and self.items[:self.num_items] == other.items[:other.num_items])
        else:
            return False

    def __repr__(self) -> str:
        return ("Stack({!r}, {!r})".format(self.capacity, self.items[:self.num_items]))

    def is_empty(self) -> bool:
        """Returns true if the stack self is empty and false otherwise"""
        return self.num_items == 0

    def is_full(self) -> bool:
        """Returns true if the stack self is full and false otherwise"""
        return self.num_items == self.capacity

    def push(self, item: Any) -> None:
        """Pushes item on the top of the Stack"""
        if self.num_items == self.capacity:
            raise IndexError
        self.items[self.num_items] = item
        self.num_items += 1

    def pop(self) -> Any:
        """Removes item from the top of the stack and returns it
        If stack is empty, raises IndexError"""
        if self.num_items == 0:
            raise IndexError
        self.num_items -= 1
        return self.items[self.num_items]

    def peek(self) -> Any:
        """Returns item on the top of the stack but does not remove it"""
        if self.num_items == 0:
            raise IndexError
        return self.items[self.num_items-1]

    def size(self) -> int:
       """Returns the number of items in the stack. Must be O(1)"""
       return self.num_items

 