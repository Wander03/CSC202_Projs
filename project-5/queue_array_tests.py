import unittest
from queue_array import Queue

class TestLab1(unittest.TestCase):

    def test_array(self) -> None:
        q = Queue(5)
        self.assertEqual(q.items, [None, None, None, None, None])
        self.assertEqual(q.get_items(), [])
        q.enqueue(1)
        self.assertEqual(q.items, [1, None, None, None, None])
        q.enqueue(2)
        self.assertEqual(q.items, [1, 2, None, None, None])

    def test_init_eq(self) -> None:
        with self.assertRaises(IndexError):
            q = Queue(5, [1, 2, 3, 4, 5, 6])
        q1 = Queue(5, [1, 2, 3, 4])
        self.assertEqual(q1.get_items(), [1, 2, 3, 4])
        q2 = Queue(5, [1, 2, 3, 4])
        self.assertEqual(q1, q2)

    def test_init_eq2(self) -> None:
        q1 = Queue(5, [1, 2, 3, 4, 5])
        q2 = Queue(5, [1, 2, 3, 4, 5])
        self.assertFalse(q1.__eq__(None))
        self.assertEqual(q1, q2)

    def test_repr(self) -> None:
        q1 = Queue(5, [])
        self.assertEqual(q1.__repr__(), "Queue(5, [])")

    def test_queue_simple(self) -> None:
        q = Queue(5)
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 5)

    def test_queue_fill_to_capacity_and_dequeue_all(self) -> None:
        q = Queue(5)
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.size(), 0)
        self.assertRaises(IndexError, q.dequeue)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertRaises(IndexError,q.enqueue,6)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.size(), 0)

    def test_queue_fill_to_capacity(self) -> None:
        q = Queue(5)
        q.enqueue(None)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(None)
        self.assertTrue(q.is_full())
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), None)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), None)

    def test_empty_queue(self) -> None:
        q = Queue(5)
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertRaises(IndexError, q.dequeue)

    def test_everything_and_big_O(self) -> None:
        size = 50000
        q = Queue(size)
        for i in range(size):
            q.enqueue(i)
        for i in range(size):
            self.assertEqual(q.dequeue(), i)
            q.enqueue(i)
            self.assertEqual(q.size(), size)
            self.assertFalse(q.is_empty())
            self.assertTrue(q.is_full())
        for i in range(size):
            self.assertEqual(q.dequeue(), i)
        self.assertTrue(q.is_empty())

if __name__ == '__main__': 
    unittest.main()
