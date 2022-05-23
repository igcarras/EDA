import copy
def compare_lists(list1: list, list2: list) -> bool:
    if len(list1) != len(list2):
        return False
    # we compare both list of vertices
    for a, b in zip(list1, list2):
        # print(str(a), str(b))
        if a != b:
            return False
    return True

class MyGraph:
    """Implementation of an undirected and unweighted graph"""

    def __init__(self, lst_vertices: list) -> None:
        """We use a dictionary to save the vertices"""
        self._vertices = {}
        for vertex in lst_vertices:
            # Each vertex is a key of the dictionary
            # Its associated value will be the list of its adjacent vertices
            self._vertices[vertex] = []

    def check_vertex(self, vertex: str) -> bool:
        """checks if the vertex exists in the graph"""
        return vertex in self._vertices

    def add_edge(self, v1: str, v2: str) -> None:
        if not self.check_vertex(v1):
            print(v1, " is not a vertex!!!")
            return
        if not self.check_vertex(v2):
            print(v2, " is not a vertex!!!")
            return
        if v1 == v2:
            print("({},{}) loops edges are not allowed!".format(v1, v2))
            return
        if v2 in self._vertices[v1] or v1 in self._vertices[v2]:
            print("({},{}) multiple edges are not allowed!".format(v1, v2))
            return

        self._vertices[v1].append(v2)
        self._vertices[v2].append(v1)

    def __eq__(self, other: 'MyGraph') -> bool:
        if other is None:
            return False

        self_keys = sorted(list(self._vertices.keys()))
        other_keys = sorted(list(other._vertices.keys()))

        if not compare_lists(self_keys, other_keys):
            return False

        # print(len(self_keys), len(other_keys))

        for vertex in self._vertices.keys():
            if not compare_lists(sorted(self._vertices[vertex]), sorted(other._vertices[vertex])):
                return False

        return True

    def __str__(self) -> str:
        """ returns a string containing the graph"""
        result = ''
        for vertex in self._vertices:
            result += '\n' + str(vertex) + ': '
            for adj in self._vertices[vertex]:
                result += str(adj) + ", "
            if result.endswith(", "):
                result = result[:-2]
        return result


    def checkingConected(self,nextOnes,vis_copy,master,curV):
        if (master==curV):
            return all(vis_copy.values())
        for vertex in nextOnes:
            if not vis_copy[vertex]:
                vis_copy[vertex]=True
                self.checkingConected(self._vertices[vertex],vis_copy,master,vertex)
        return all(vis_copy.values())

    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visitados = {}
        etique =  self._vertices.keys()
        for v in etique:
            for j in  self._vertices:
                visitados[j] = False
            if not self.checkingConected(self._vertices[v],visitados,v,None):
                return False
        return True

    def is_bridge(self, v1: str, v2: str) -> bool:
        if v2 not in self._vertices[v1]:
            return False
        self._vertices[v1].remove(v2)
        self._vertices[v2].remove(v1)
        if(self.is_connected()):
            self.add_edge(v1, v2)
            return False
        self.add_edge(v1, v2)
        return True


if __name__ == '__main__':
   
    print('Third graph:')
    vertices = ['A', 'B', 'C', 'D', 'E']
    # vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    g3 = MyGraph(vertices)
    g3.add_edge('A', 'B')
    g3.add_edge('B', 'C')
    g3.add_edge('C', 'D')
    g3.add_edge('D', 'E')
    # g3.add_edge('D', 'E')
    # g3.add_edge('D', 'F')
    # g3.add_edge('D', 'G')
    # g3.add_edge('E', 'F')
    print("Isconected;",g3.is_connected())
    print("IsBridge",g3.is_bridge("D","E"))

    print(g3)

    # u, v = 'A', 'B'
    # print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # True
    # # assert g3.is_bridge(u, v)

    # u, v = 'B', 'A'
    # print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # True
    # # assert g3.is_bridge(u, v)

    # u, v = 'B', 'C'
    # print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # True
    # # assert g3.is_bridge(u, v)

    # u, v = 'D', 'G'
    # print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # True
    # # assert g3.is_bridge(u, v)

    # u, v = 'C', 'E'
    # print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # False
    # # assert not g3.is_bridge(u, v)

    # u, v = 'D', 'F'
    # print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # False
    # # assert not g3.is_bridge(u, v)

    # u, v = 'D', 'E'
    # print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # False
    # # assert not g3.is_bridge(u, v)

    # u, v = 'C', 'D'
    # print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # False
    # # assert not g3.is_bridge(u, v)
 # Create a graph: A<->B<->C<->D
    # vertices = ['A', 'B', 'C', 'D']
    # g = MyGraph(vertices)
    # g.add_edge('A', 'B')
    # g.add_edge('B', 'C')
    # g.add_edge('C', 'D')
    # print("First graph: ", str(g))
    # print()
    # print("is_connected()={}\n".format(g.is_connected()))  # True
    # # assert g.is_connected()

    # u, v = 'A', 'B'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # # assert g.is_bridge(u, v)

    # u, v = 'B', 'A'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # # assert g.is_bridge(u, v)

    # u, v = 'A', 'C'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # # assert not g.is_bridge(u, v)

    # u, v = 'A', 'D'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # # assert not g.is_bridge(u, v)

    # u, v = 'B', 'C'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # # assert g.is_bridge(u, v)

    # u, v = 'C', 'B'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # # assert g.is_bridge(u, v)

    # u, v = 'B', 'D'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # # assert not g.is_bridge(u, v)

    # u, v = 'C', 'D'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # # assert g.is_bridge(u, v)

    # u, v = 'D', 'C'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # # assert g.is_bridge(u, v)

    # # second graph
    # print('Second graph:')
    # vertices = ['A', 'B', 'C', 'D', 'E']
    # g = MyGraph(vertices)
    # g.add_edge('A', 'B')
    # g.add_edge('A', 'C')
    # g.add_edge('B', 'C')
    # g.add_edge('A', 'D')
    # g.add_edge('D', 'E')
    # print(g)

    # print("is_connected()={}\n".format(g.is_connected()))  # True
    # #  assert g.is_connected()

    # u, v = 'A', 'B'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # # assert not g.is_bridge(u, v)

    # u, v = 'A', 'C'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # # assert not g.is_bridge(u, v)

    # u, v = 'B', 'C'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # # assert not g.is_bridge(u, v)

    # u, v = 'A', 'D'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # # assert g.is_bridge(u, v)

    # u, v = 'D', 'A'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # # assert g.is_bridge(u, v)

    # u, v = 'D', 'E'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # # assert g.is_bridge(u, v)

    # u, v = 'E', 'D'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # # assert g.is_bridge(u, v)

    # u, v = 'B', 'E'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # # assert not g.is_bridge(u, v)

    # u, v = 'A', 'E'
    # print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # # assert not g.is_bridge(u, v)
