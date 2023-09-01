from __future__ import annotations
from os import read
from typing import List, Optional


class HuffmanNode:
    def __init__(self, char_ascii: int, freq: int, left: Optional[HuffmanNode] = None, right: Optional[HuffmanNode] = None):
        self.char_ascii = char_ascii    # stored as an integer - the ASCII character code value
        self.freq = freq                # the frequency associated with the node
        self.left = left                # Huffman tree (node) to the left!
        self.right = right              # Huffman tree (node) to the right

    def __lt__(self, other: HuffmanNode) -> bool:
        return comes_before(self, other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HuffmanNode):
            return False
        else:
             return (self.char_ascii == other.char_ascii
                        and self.freq == other.freq
                        and self.left == other.left
                        and self.right == other.right)

def comes_before(a: HuffmanNode, b: HuffmanNode) -> bool:
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise (tie borken by ascii value)"""
    if a.freq == b.freq:
        return a.char_ascii < b.char_ascii
    else:
        return a.freq < b.freq

def combine(a: HuffmanNode, b: HuffmanNode) -> HuffmanNode:
    """Creates a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lower of the a and b char ASCII values"""
    if a.char_ascii < b.char_ascii:
        lesser_char = a.char_ascii
    else: 
        lesser_char = b.char_ascii

    sum_freq = a.freq + b.freq

    if a < b:
        lesser_node = a
        greater_node = b
    else:
        lesser_node = b
        greater_node = a

    return HuffmanNode(lesser_char, sum_freq, lesser_node, greater_node)

def cnt_freq(filename: str) -> List:
    """Opens a text file with a given file name (passed as a string) and counts the
    frequency of occurrences of all the characters within that file
    Returns a Python List with 256 entries - counts are initialized to zero.
    The ASCII value of the characters are used to index into this list for the frequency counts"""
    ascii_array = [0] * 256

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                for char in line:
                    ascii_array[ord(char)] += 1
    except:
        raise FileNotFoundError

    return ascii_array

def create_huff_tree(char_freq: List) -> Optional[HuffmanNode]:
    """Input is the list of frequencies (provided by cnt_freq()).
    Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree. Returns None if all counts are zero."""
    tree_list: List = []

    for i in range(len(char_freq)):
        if char_freq[i] != 0:
            tree_list.append(HuffmanNode(i, char_freq[i]))

    if len(tree_list) == 0:
        return None
    if len(tree_list) == 1:
        new_parent = tree_list[0]
    else:
        tree_list.sort()  # Wouldn't sorting in decending order be better since we could use .pop() for O(1)?
        while len(tree_list) != 1:
            new_parent = combine(tree_list.pop(0), tree_list.pop(0))

            i = 0
            added = False
            while not added:
                try:
                    if new_parent > tree_list[i]:
                        raise Exception
                    else:
                        tree_list.insert(i, new_parent)
                        added = True
                except:
                    if i != len(tree_list):
                        i += 1
                    else:
                        tree_list.insert(i, new_parent)
                        added = True

    return new_parent

def create_code(node: Optional[HuffmanNode]) -> List:
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the array, with the resulting Huffman code for that character stored at that location.
    Characters that are unused should have an empty string at that location"""
    codes_array = [""] * 256
    
    code_helper(node, "", codes_array)

    return codes_array

def code_helper(cur: Optional[HuffmanNode], code: str, array: List) -> None:
    """Traverses HuffmanNode, adding Huffman Codes for each leaf node"""
    if cur is not None:
        if cur.left is not None:
            code_helper(cur.left, code + "0", array)
        else:
            array[cur.char_ascii] = code
        if cur.right is not None:
            code_helper(cur.right, code + "1", array)
        else:
            array[cur.char_ascii] = code

def create_header(freqs: List) -> str:
    """Input is the list of frequencies (provided by cnt_freq()).
    Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    out = ""

    for i in range(len(freqs)):
        if freqs[i] != 0:
            out += "%d %d " % (i, freqs[i])

    return out.rstrip()

def huffman_encode(in_file: str, out_file: str) -> None:
    """Takes input file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take note of special cases - empty file and file with only one unique character"""
    freqs = cnt_freq(in_file)
    huff_tree = create_huff_tree(freqs)
    codes = create_code(huff_tree)

    with open(in_file, 'r') as f:
        lines = "".join(f.readlines())

    with open(out_file, 'w', newline='') as f:
        f.write(create_header(freqs) + "\n")
        for char in lines:
            f.write(codes[ord(char)])


def parse_header(header_string: str) -> List:
    """Takes header from encoded_file as parameter and returns a freq list"""
    ascii_array = [0] * 256
    header_list = header_string.split()

    for ascii_val in range(0, (len(header_list)), 2):
        ascii_array[int(header_list[ascii_val])] = int(header_list[ascii_val + 1])

    return ascii_array


def huffman_decode(encoded_file: str, decode_file: str) -> None:
    """Takes inut file name and output file name as parameters
    Uses Huffman Tree coding process from header information in encoded_file 
    If the encoded_file does not exist, raise FileNotFoundError. If output file exists, overwrite"""
    try:
        with open(encoded_file, 'r') as f:
            header = f.readline()
    except:
        raise FileNotFoundError

    freq_list = parse_header(header)
    huff_tree = create_huff_tree(freq_list)

    with open(encoded_file, 'r') as f:
        lines = "".join(f.readlines()[1:])

    with open(decode_file, 'w', newline='') as f:
        cur = huff_tree
        for num in lines:
            if cur is not None:
                    if num == '0' and cur.left is not None:
                        cur = cur.left
                    elif num == '1' and cur.right is not None:
                        cur = cur.right
                    else:
                        f.write(chr(cur.char_ascii))
                        if num == '0' and huff_tree is not None:
                            cur = huff_tree.left
                        else:
                            if huff_tree is not None:
                                cur = huff_tree.right

        if cur is not None:             # Get last char
            f.write(chr(cur.char_ascii))
