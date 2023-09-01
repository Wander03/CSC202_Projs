import abc
from typing import List


# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in: str) -> List:
    """Takes a string and returns a list of permutations in 
       lexicographic order.

    Parameters:
        str_in -- string of 0 or more unique, lower-case, letters 
                  in alphabetical order
    """
    output: List = []

    # If empty string return empty list
    if str_in == '':
        return []

    # Base Case -- return single char
    if len(str_in) == 1:
        output.append(str_in)
        return output

    # For each char in str_in...
    for i in range(len(str_in)):
            
        # Create simpler
        if i == 0:
            simpler = str_in[1:]
        else:
            simpler = str_in[:i] + str_in[i + 1:]

        # Create permutations and save to output list
        output = output + perm_gen_lex(simpler)

        # Modify each NEW permutation by adding removed char to beginning
        for n in range(len(output)):
            if len(output[n]) < len(str_in):
                output[n] = (str_in[i] + output[n])

    return output
