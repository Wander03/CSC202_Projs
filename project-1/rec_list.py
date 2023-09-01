### NOTE Ask about coverage for lines 19 and 22 ###

from __future__ import annotations
from typing import Optional, Any, Tuple


# NodeList is
# None or
# Node(value, rest), where rest is the rest of the NodeList
class Node:
    def __init__(self, value: Any, rest: Optional[Node]):
        self.value = value
        self.rest = rest

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return (self.value == other.value
                    and self.rest == other.rest
                    )
        else:
            return False

    def __repr__(self) -> str:
        return ("Node({!r}, {!r})".format(self.value, self.rest))

# a StrList is one of
# - None, or
# - Node(string, StrList)

# StrList -> string
# Returns first (as determined by Python compare) string in StrList
# If StrList is empty (None), return None
# Must be implemented recursively
def first_string(strlist: Optional[Node]) -> Optional[str]:
    # If Node is empty
    if strlist is None:
        return None
    
    first = first_string(strlist.rest)
    current = strlist.value

    if (first is None) or (current < first):
        return current
    else:
        return first


# StrList -> (StrList, StrList, StrList)
# Returns a tuple with 3 new StrLists,
# the first one with strings from the input list that start with a vowel,
# the second with strings from the input list that start with a consonant,
# the third with strings that don't start with an alpha character
# Must be implemented recursively
def split_list(strlist: Optional[Node]) -> Tuple[Optional[Node], Optional[Node], Optional[Node]]:
    if strlist is None:
        return (None, None, None)
    
    vowel_list, const_list, other_list = split_list(strlist.rest)
    current = strlist.value

    # If current is an empty string
    if current == '':
        return (vowel_list, const_list, Node(current, other_list))

    # Adds to front of Node so output Nodes follow order of input Node
    if current[0].lower() in ['a','e','i','o','u']:
        return (Node(current, vowel_list), const_list, other_list)
    elif current[0].isalpha():
        return (vowel_list, Node(current, const_list), other_list)
    else:
        return (vowel_list, const_list, Node(current, other_list))
