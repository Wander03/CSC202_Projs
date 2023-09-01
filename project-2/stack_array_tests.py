import unittest
from stack_array import Stack
        
class TestLab2(unittest.TestCase):

    def test_init(self) -> None:
        stack = Stack(5)
        self.assertEqual(stack.items, [None]*5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self) -> None:
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5,[1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)
        self.assertFalse(stack1.__eq__(None))

    def test_repr(self) -> None:
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

    def test_is_empty01(self) -> None:
        stack = Stack(5)
        self.assertTrue(stack.is_empty())

    def test_is_empty02(self) -> None:
        stack = Stack(5, [1, 2, 3])
        self.assertFalse(stack.is_empty())

    def test_is_full01(self) -> None:
        stack = Stack(5)
        self.assertFalse(stack.is_full())

    def test_is_full02(self) -> None:
        stack = Stack(5, [1, 2, 3, 4, 5])
        self.assertTrue(stack.is_full())

    def test_is_full03(self) -> None:
        stack = Stack(5, [1, 2, 3])
        self.assertFalse(stack.is_full())

    def test_push01(self) -> None:
        stack = Stack(3)
        stack.push(1)
        self.assertEqual(stack.items, [1, None, None])
        self.assertEqual(stack.num_items, 1)

    def test_push02(self) -> None:
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.items, [1, 2, 3])
        self.assertEqual(stack.num_items, 3)

    def test_push03(self) -> None:
        stack = Stack(1)
        stack.push(1)
        
        with self.assertRaises(IndexError):
            stack.push(2)

    def test_pop01(self) -> None:
        stack = Stack(3, [1, 2, 3])
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.items, [1, 2, 3])
        self.assertEqual(stack.num_items, 2)

        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.items, [1, 2, 3])
        self.assertEqual(stack.num_items, 1)

        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.items, [1, 2, 3])
        self.assertEqual(stack.num_items, 0)

    def test_pop02(self) -> None:
        stack = Stack(5)
        
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek01(self) -> None:
        stack = Stack(3, [1, 2, 3])
        self.assertEqual(stack.peek(), 3)
        self.assertEqual(stack.items, [1, 2, 3])
        self.assertEqual(stack.num_items, 3)

    def test_peek02(self) -> None:
        stack = Stack(5)
        
        with self.assertRaises(IndexError):
            stack.peek()

    def test_size01(self) -> None:
        stack = Stack(3, [1, 2, 3])
        self.assertEqual(stack.size(), 3)

    def test_size02(self) -> None:
        stack = Stack(3)
        self.assertEqual(stack.size(), 0)

    def test_size03(self) -> None:
        stack = Stack(3)
        stack.push(4)
        self.assertEqual(stack.size(), 1)

if __name__ == '__main__': 
    unittest.main()
