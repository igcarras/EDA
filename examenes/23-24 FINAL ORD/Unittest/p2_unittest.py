class MyGraph:

    def __init__(self, lst_vertices: list) -> None:
        self._vertices = {}
        for vertex in lst_vertices:
            self._vertices[vertex] = []

    def check_vertex(self, vertex: str) -> bool:
        return vertex in self._vertices

    def add_edge(self, v1: str, v2: str) -> None:
        if not self.check_vertex(v1):
            print(v1, " is not a vertex!!!")
            return
        if not self.check_vertex(v2):
            print(v2, " is not a vertex!!!")
            return
        if v2 in self._vertices[v1] or v1 in self._vertices[v2]:
            print("({},{}) multiple edges are not allowed!".format(v1, v2))
            return

        self._vertices[v1].append(v2)

    def minDistance(self, start: str, end: str) -> int:
        ...

    def __str__(self) -> str:
        """ returns a string containing the graph"""
        result = ''
        for v in self._vertices:
            result += '\n' + str(v) + ':'
            for adj in self._vertices[v]:
                result += str(adj) + "  "
        return result


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        return

    def test0(self):
        print('Test 0')
        labels = ['A', 'B', 'C', 'D']

        g = MyGraph(labels)

        # Now, we add the edges
        g.add_edge('A', 'C')
        g.add_edge('A', 'B')
        g.add_edge('C', 'B')
        g.add_edge('B', 'D')
        g.add_edge('D', 'C')

        self.assertEqual(g.minDistance('A', 'A'), 0)
        self.assertEqual(g.minDistance('A', 'B'), 1)
        self.assertEqual(g.minDistance('A', 'C'), 1)
        self.assertEqual(g.minDistance('A', 'D'), 2)
        self.assertEqual(g.minDistance('B', 'C'), 2)
        self.assertEqual(g.minDistance('B', 'D'), 1)
        self.assertEqual(g.minDistance('C', 'D'), 2)
        self.assertEqual(g.minDistance('C', 'E'), None)

    def test1(self):
        print('Test 1')
        labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

        g = MyGraph(labels)

        # Now, we add the edges
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('C', 'D')
        g.add_edge('B', 'D')
        g.add_edge('D', 'E')
        g.add_edge('D', 'F')
        g.add_edge('E', 'G')
        g.add_edge('F', 'G')

        self.assertEqual(g.minDistance('A', 'A'), 0)
        self.assertEqual(g.minDistance('A', 'B'), 1)
        self.assertEqual(g.minDistance('A', 'C'), 1)
        self.assertEqual(g.minDistance('A', 'D'), 2)
        self.assertEqual(g.minDistance('A', 'E'), 3)
        self.assertEqual(g.minDistance('A', 'F'), 3)
        self.assertEqual(g.minDistance('A', 'G'), 4)
        self.assertEqual(g.minDistance('B', 'C'), -1)
        self.assertEqual(g.minDistance('B', 'D'), 1)
        self.assertEqual(g.minDistance('B', 'E'), 2)
        self.assertEqual(g.minDistance('B', 'F'), 2)
        self.assertEqual(g.minDistance('B', 'G'), 3)
        self.assertEqual(g.minDistance('C', 'D'), 1)
        self.assertEqual(g.minDistance('C', 'E'), 2)
        self.assertEqual(g.minDistance('C', 'F'), 2)
        self.assertEqual(g.minDistance('C', 'G'), 3)
        self.assertEqual(g.minDistance('D', 'E'), 1)
        self.assertEqual(g.minDistance('D', 'F'), 1)
        self.assertEqual(g.minDistance('D', 'G'), 2)
        self.assertEqual(g.minDistance('E', 'F'), -1)
        self.assertEqual(g.minDistance('E', 'G'), 1)
        self.assertEqual(g.minDistance('F', 'G'), 1)

    def test2(self):
        print('Test 2')
        labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

        g = MyGraph(labels)

        # Now, we add the edges
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('C', 'D')
        g.add_edge('B', 'D')
        g.add_edge('E', 'F')
        g.add_edge('E', 'G')
        g.add_edge('F', 'G')

        self.assertEqual(g.minDistance('A', 'A'), 0)
        self.assertEqual(g.minDistance('A', 'B'), 1)
        self.assertEqual(g.minDistance('A', 'C'), 1)
        self.assertEqual(g.minDistance('A', 'D'), 2)
        self.assertEqual(g.minDistance('A', 'E'), -1)
        self.assertEqual(g.minDistance('A', 'F'), -1)
        self.assertEqual(g.minDistance('A', 'G'), -1)
        self.assertEqual(g.minDistance('B', 'C'), -1)
        self.assertEqual(g.minDistance('B', 'D'), 1)
        self.assertEqual(g.minDistance('B', 'E'), -1)
        self.assertEqual(g.minDistance('B', 'F'), -1)
        self.assertEqual(g.minDistance('B', 'G'), -1)
        self.assertEqual(g.minDistance('C', 'D'), 1)
        self.assertEqual(g.minDistance('C', 'E'), -1)
        self.assertEqual(g.minDistance('C', 'F'), -1)
        self.assertEqual(g.minDistance('C', 'G'), -1)
        self.assertEqual(g.minDistance('D', 'E'), -1)
        self.assertEqual(g.minDistance('D', 'F'), -1)
        self.assertEqual(g.minDistance('D', 'G'), -1)
        self.assertEqual(g.minDistance('E', 'F'), 1)
        self.assertEqual(g.minDistance('E', 'G'), 1)
        self.assertEqual(g.minDistance('F', 'G'), 1)


unittest.main(argv=['first-arg-is-ignored'], exit=False)

