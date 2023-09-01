import unittest
from huffman import *


class TestList(unittest.TestCase):
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
def compare_files(file1: str,file2: str) -> bool:
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
