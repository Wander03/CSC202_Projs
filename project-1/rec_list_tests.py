import unittest
from rec_list import *

# Starter test cases - write more!!

class TestRecList(unittest.TestCase):

    def test_first1(self) -> None:
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(first_string(strlist),"49ers")

    def test_first2(self) -> None:
        strlist = None
        self.assertEqual(first_string(strlist),None)

    def test_first3(self) -> None:
        strlist = Node(None, None)
        self.assertEqual(first_string(strlist),None)

    def test_first4(self) -> None:
        strlist = Node("xyz", Node("", Node("49ers", None)))
        self.assertEqual(first_string(strlist),"")

    def test_first5(self) -> None:
        strlist = Node("0xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(first_string(strlist),"0xyz")

    def test_first6(self) -> None:
        strlist = Node("xyz", None)
        self.assertEqual(first_string(strlist),"xyz")

    def test_split1(self) -> None:
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(split_list(strlist),(Node('Abc', None), Node('xyz', None), Node('49ers', None)))

    def test_split2(self) -> None:
        strlist = Node("Yellow", Node("abc", Node("$7.25", Node("lime", Node("42", Node("Ethan", None))))))
        self.assertEqual(split_list(strlist),(Node('abc', Node("Ethan", None)), Node('Yellow', Node("lime", None)), Node('$7.25', Node("42", None))))

    def test_split3(self) -> None:
        strlist = None
        self.assertEqual(split_list(strlist),(None, None, None))

    def test_split4(self) -> None:
        strlist = Node("xyz", Node("Abc", None))
        self.assertEqual(split_list(strlist),(Node('Abc', None), Node('xyz', None), None))

    def test_split5(self) -> None:
        strlist = Node("xyz", Node("  ", Node("Abc", Node("49ers", Node("", None)))))
        self.assertEqual(split_list(strlist),(Node('Abc', None), Node('xyz', None), Node("  ", Node('49ers', Node("", None)))))

    def test_eq1(self) -> None:
        node1 = Node(1, Node(3, None))
        node2 = Node(3, Node(1, None))
        self.assertFalse(node1 == node2)

    def test_eq2(self) -> None:
        node1 = Node(1, Node(3, None))
        node2 = Node(1, Node(3, None))
        self.assertTrue(node1 == node2)

    def test_eq3(self) -> None:
        node1 = Node(1, Node(3, None))
        node2 = 111
        self.assertFalse(node1 == node2)

    def test_repr1(self) -> None:
        node1 = repr(Node(1, Node(3, None)))
        node1_repr = 'Node(1, Node(3, None))'
        self.assertTrue(node1 == node1_repr)

    def test_repr2(self) -> None:
        node1 = repr(Node(1, Node(3, None)))
        node1_repr = 'Node(1, Node(3))'
        self.assertFalse(node1 == node1_repr)

if __name__ == "__main__":
        unittest.main()