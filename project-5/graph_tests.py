import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self) -> None:
        g = Graph('test1.txt')
        self.assertEqual([['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']], g.conn_components())
        self.assertTrue(g.is_bipartite())

    def test_02(self) -> None:
        g = Graph('test2.txt')
        self.assertEqual([['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']], g.conn_components())
        self.assertEqual(g.is_bipartite(), False)
        self.assertFalse(g.is_bipartite())

    def test_03(self) -> None:
        g = Graph("test1.txt")
        self.assertEqual(g.get_vertices(), ['v1','v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        g.add_vertex('v10')
        self.assertEqual(g.get_vertices(), ['v1', 'v10', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])

    def test_04(self) -> None:
        v = Vertex('1')
        v2 = Vertex('2')
        v3 = Vertex('1')
        self.assertEqual(v.__repr__(), "Vertex('1', [], False, None)")
        self.assertTrue(v.__eq__(v3))
        self.assertFalse(v.__eq__(v2))
        self.assertFalse(v.__eq__('1'))

    def test_05(self) -> None:
        g = Graph("test1.txt")
        self.assertEqual(g.get_vertex('1'), None)
        g.add_edge('v1', 'v9')
        temp = g.get_vertex('v9')
        if temp is not None:
            temp = temp.adjacent_to[-1].id
        self.assertEqual(temp, 'v1')

    def test_06(self) -> None:
        g = Graph('test3.txt')
        self.assertEqual([['A', 'C', 'D', 'E', 'F'], ['B', 'G']], g.conn_components())
        self.assertEqual(g.is_bipartite(), False)
        self.assertFalse(g.is_bipartite())

    def test_07(self) -> None:
        g = Graph('test4.txt')
        self.assertEqual([['A', 'C', 'D', 'E', 'F'], ['B', 'G']], g.conn_components())
        self.assertEqual(g.is_bipartite(), True)
        self.assertTrue(g.is_bipartite())

if __name__ == '__main__':
   unittest.main()
