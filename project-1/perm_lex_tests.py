import unittest
import perm_lex
from typing import List

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex_01(self) -> None:
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])

    def test_perm_gen_lex_02(self) -> None:
        self.assertEqual(perm_lex.perm_gen_lex(''),[])

    def test_perm_gen_lex_03(self) -> None:
        self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc','acb', 'bac', 'bca', 'cab', 'cba'])

    def test_perm_gen_lex_04(self) -> None:
        self.assertEqual(perm_lex.perm_gen_lex('a'),['a'])

    def test_perm_gen_lex_05(self) -> None:
        self.assertEqual(perm_lex.perm_gen_lex('abcd'),['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
                                                        'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
                                                        'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
                                                        'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'])

if __name__ == "__main__":
        unittest.main()
