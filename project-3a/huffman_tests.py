import unittest
from huffman import *


class TestList(unittest.TestCase):
    def test_cnt_freq(self) -> None:
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist)

    def test_combine(self) -> None:
        a = HuffmanNode(65, 1)
        b = HuffmanNode(66, 2)
        c = combine(a, b)
        if (c.left is not None) and (c.right is not None):
            self.assertEqual(c.left.char_ascii,65)
            self.assertEqual(c.left.freq, 1)
            self.assertEqual(c.right.char_ascii, 66)
            self.assertEqual(c.right.freq, 2)
            self.assertEqual(c.char_ascii, 65)
            self.assertEqual(c.freq, 3)
        else:   # pragma: no cover
            self.fail()
        c = combine(b, a)
        if (c.left is not None) and (c.right is not None):
            self.assertEqual(c.left.char_ascii,65)
            self.assertEqual(c.left.freq, 1)
            self.assertEqual(c.right.char_ascii, 66)
            self.assertEqual(c.right.freq, 2)
            self.assertEqual(c.char_ascii, 65)
            self.assertEqual(c.freq, 3)
        else:   # pragma: no cover
            self.fail()

    def test_create_huff_tree(self) -> None:
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        if hufftree is not None:
            self.assertEqual(hufftree.freq, 32)
            self.assertEqual(hufftree.char_ascii, 97)
            left = hufftree.left
            right = hufftree.right
            if (left is not None) and (right is not None):
                self.assertEqual(left.freq, 16)
                self.assertEqual(left.char_ascii, 97)
                self.assertEqual(right.freq, 16)
                self.assertEqual(right.char_ascii, 100)
            else:  # pragma: no cover
                self.fail()
        else:  # pragma: no cover
            self.fail()

    def test_create_header(self) -> None:
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_code(self) -> None:
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_01_textfile(self) -> None:
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file1_out.txt", "file1_soln.txt"))

# My tests
    def test_cnt_freq_01(self) -> None:
        freqlist = cnt_freq("file3.txt")
        anslist = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 0]
        self.assertListEqual(freqlist[46:60], anslist)

    def test_lt_01(self) -> None:
        node1 = HuffmanNode(5, 5)
        node2 = HuffmanNode(4, 5)
        node_list = [node1, node2]

        self.assertFalse(comes_before(node1, node2))
        self.assertTrue(comes_before(node2, node1))
        self.assertFalse(node1 < node2)
        self.assertTrue(node2 < node1)

        node_list.sort()
        self.assertEqual(node_list, [node2, node1])

    def test_lt_02(self) -> None:
        node1 = HuffmanNode(5, 1)
        node2 = HuffmanNode(4, 5)
        node_list = [node1, node2]

        self.assertTrue(comes_before(node1, node2))
        self.assertFalse(comes_before(node2, node1))
        self.assertTrue(node1 < node2)
        self.assertFalse(node2 < node1)

        node_list.sort()
        self.assertEqual(node_list, [node1, node2])

    def test_lt_03(self) -> None:
        node1 = HuffmanNode(5, 1)
        node2 = HuffmanNode(4, 5)
        node3 = HuffmanNode(1, 2)
        node_list = [node1, node2, node3]

        self.assertTrue(comes_before(node1, node2))
        self.assertFalse(comes_before(node2, node1))
        self.assertTrue(node1 < node2)
        self.assertFalse(node2 < node1)

        node_list.sort()
        self.assertEqual(node_list, [node1, node3, node2])

    def test_eq(self) -> None:
        self.assertEqual(HuffmanNode(1,1), HuffmanNode(1,1))
        self.assertNotEqual(HuffmanNode(1,1), HuffmanNode(1,2))

        node1 = HuffmanNode(5, 1)
        node2 = HuffmanNode(4, 5)
        node3 = 54378965

        parent1 = HuffmanNode(1, 2, node1, node2)
        parent2 = HuffmanNode(1, 2, node2, node1)
        parent3 = HuffmanNode(1, 2, node1, node2)

        self.assertEqual(parent1, parent3)
        self.assertNotEqual(parent1, parent2)
        self.assertNotEqual(parent2, parent3)
        self.assertNotEqual(node3, node1)

    def test_combine_01(self) -> None:
        node1 = HuffmanNode(5, 5)
        node2 = HuffmanNode(4, 5)
        node_list = [node1, node2]
        node_list.sort()
        parent = combine(node_list[0], node_list[1])

        self.assertEqual(parent, HuffmanNode(4, 10, node2, node1))

    def test_combine_02(self) -> None:
        node1 = HuffmanNode(5, 1)
        node2 = HuffmanNode(4, 5)
        node_list = [node1, node2]
        node_list.sort()
        parent = combine(node_list[0], node_list[1])

        self.assertEqual(parent, HuffmanNode(4, 6, node1, node2))

    def test_combine_03(self) -> None:
        node1 = HuffmanNode(1, 1)
        node2 = HuffmanNode(4, 5)
        node3 = HuffmanNode(5, 2)
        node_list = [node1, node2, node3]
        node_list.sort()

        parent = combine(node_list.pop(0), node_list.pop(0))
        self.assertEqual(parent, HuffmanNode(1, 3, node1, node3))

        parent2 = combine(parent, node_list.pop(0))
        self.assertEqual(parent2, HuffmanNode(1, 8, parent, node2))

    def test_create_huff_tree_01(self) -> None:
        freqlist = cnt_freq("file3.txt")
        hufftree = create_huff_tree(freqlist)
        if hufftree is not None:
            self.assertEqual(hufftree.freq, 16)
            self.assertEqual(hufftree.char_ascii, 47)
            left = hufftree.left
            right = hufftree.right
            if (left is not None) and (right is not None):
                self.assertEqual(left.freq, 7)
                self.assertEqual(left.char_ascii, 47)
                self.assertEqual(right.freq, 9)
                self.assertEqual(right.char_ascii, 53)
            else: # pragma: no cover
                self.fail()
        else: # pragma: no cover
            self.fail()

    def test_create_huff_tree_02(self) -> None:
        freqlist = cnt_freq("file4.txt")
        hufftree = create_huff_tree(freqlist)
        if hufftree is not None:
            self.assertEqual(hufftree.freq, 13)
            self.assertEqual(hufftree.char_ascii, 32)
            left = hufftree.left
            right = hufftree.right
            if (left is not None) and (right is not None):
                self.assertEqual(left.freq, 6)
                self.assertEqual(left.char_ascii, 32)
                self.assertEqual(right.freq, 7)
                self.assertEqual(right.char_ascii, 97)
            else: # pragma: no cover
                self.fail()
        else: # pragma: no cover
            self.fail()

    def test_create_huff_tree_03(self) -> None:
        freqlist = cnt_freq("empty_file.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree, None)

    def test_create_code_01(self) -> None:
        freqlist = cnt_freq("file3.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('/')], '0010')
        self.assertEqual(codes[ord('0')], '0011')
        self.assertEqual(codes[ord('1')], '0100')
        self.assertEqual(codes[ord('2')], '0101')
        self.assertEqual(codes[ord('3')], '0110')
        self.assertEqual(codes[ord('4')], '0111')
        self.assertEqual(codes[ord('5')], '1000')
        self.assertEqual(codes[ord('6')], '1001')
        self.assertEqual(codes[ord('7')], '1010')
        self.assertEqual(codes[ord('8')], '1011')
        self.assertEqual(codes[ord('9')], '000')
        self.assertEqual(codes[ord(':')], '11')

    def test_create_code_02(self) -> None:
        freqlist = cnt_freq("file4.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord(' ')], '00')
        self.assertEqual(codes[ord('a')], '11')
        self.assertEqual(codes[ord('b')], '01')
        self.assertEqual(codes[ord('c')], '101')
        self.assertEqual(codes[ord('d')], '100')

    def test_create_header_01(self) -> None:
        freqlist = cnt_freq("file3.txt")
        self.assertEqual(create_header(freqlist), "47 1 48 1 49 1 50 1 51 1 52 1 53 1 54 1 55 1 56 1 57 1 58 5")

    def test_create_header_02(self) -> None:
        freqlist = cnt_freq("file4.txt")
        self.assertEqual(create_header(freqlist), "32 3 97 4 98 3 99 2 100 1")

    def test_create_header_03(self) -> None:
        freqlist = cnt_freq("file5.txt")
        self.assertEqual(create_header(freqlist), "97 3 98 4 99 2")

    def test_encode_01(self) -> None:
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file2_out.txt", "file2_soln.txt"))

    def test_encode_02(self) -> None:
        huffman_encode("file3.txt", "file3_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file3_out.txt", "file3_soln.txt"))

    def test_encode_03(self) -> None:
        huffman_encode("file4.txt", "file4_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file4_out.txt", "file4_soln.txt"))

    def test_encode_04(self) -> None:
        huffman_encode("file5.txt", "file5_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file5_out.txt", "file5_soln.txt"))

    def test_encode_05(self) -> None:
        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("multiline_out.txt", "multiline_soln.txt"))

    def test_encode_06(self) -> None:
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("declaration_out.txt", "declaration_soln.txt"))

    def test_encode_07(self) -> None:
        huffman_encode("empty_file.txt", "empty_file_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("empty_file_out.txt", "empty_file_soln.txt"))

    def test_encode_08(self) -> None:
        huffman_encode("unique.txt", "unique_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("unique_out.txt", "unique_soln.txt"))

    def test_encode_09(self) -> None:
     with self.assertRaises(FileNotFoundError):
        huffman_encode("NOTFOUND.txt", "NOTFOUND_out.txt")

    ################### PART B TESTS ###########################################################

    def test_parse_header(self) -> None:
        header = "97 2 98 4 99 8 100 16 102 2"
        freqlist = parse_header(header)
        anslist = [0]*256
        anslist[97:104] = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist[97:104], anslist[97:104])

    def test_parse_header_01(self) -> None:
        header = "47 1 48 1 49 1 50 1 51 1 52 1 53 1 54 1 55 1 56 1 57 1 58 5"
        freqlist = parse_header(header)
        anslist = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 0]
        self.assertListEqual(freqlist[46:60], anslist)

    def test_parse_header_02(self) -> None:
        header = "97 5"
        freqlist = parse_header(header)
        anslist = [5]
        self.assertListEqual(freqlist[97:98], anslist)

    def test_parse_header_03(self) -> None:
        header = ""
        freqlist = parse_header(header)
        anslist = [0] * 256
        self.assertListEqual(freqlist, anslist)

    def test_decode_01(self) -> None:
        huffman_decode("file1_soln.txt", "file1_decode.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file1.txt", "file1_decode.txt"))

    def test_decode_02(self) -> None:
        huffman_decode("declaration_soln.txt", "declaration_decode.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("declaration.txt", "declaration_decode.txt"))

    def test_decode_03(self) -> None:
        huffman_decode("empty_file_soln.txt", "empty_file_decode.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("empty_file.txt", "empty_file_decode.txt"))

    def test_decode_04(self) -> None:
        huffman_decode("file2_soln.txt", "file2_decode.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file2.txt", "file2_decode.txt"))

    def test_decode_05(self) -> None:
        huffman_decode("file3_soln.txt", "file3_decode.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file3.txt", "file3_decode.txt"))

    def test_decode_06(self) -> None:
        huffman_decode("file4_soln.txt", "file4_decode.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file4.txt", "file4_decode.txt"))

    def test_decode_07(self) -> None:
        huffman_decode("file5_soln.txt", "file5_decode.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file5.txt", "file5_decode.txt"))

    def test_decode_08(self) -> None:
        huffman_decode("multiline_soln.txt", "multiline_decode.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("multiline.txt", "multiline_decode.txt"))

    def test_decode_09(self) -> None:
     with self.assertRaises(FileNotFoundError):
        huffman_decode("NOTFOUND.txt", "NOTFOUND_out.txt")

# Compare files - takes care of CR/LF, LF issues
def compare_files(file1: str,file2: str) -> bool: # pragma: no cover
    match = True
    done = False
    with open(file1, "r") as f1:
        with open(file2, "r") as f2:
            while not done:
                line1 = f1.readline().strip()
                line2 = f2.readline().strip()
                if line1 == '' and line2 == '':
                    done = True
                if line1 != line2:
                    done = True
                    match = False
    return match

if __name__ == '__main__':
    unittest.main()
