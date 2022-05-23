"""100451322 - Yago Brotón Gutiérrez"""


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

    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""

        visitados = {}
        for i in self._vertices:
            visitados[i] = False

        comp = []  # Lista con las distintas componentes conexas
        for i in visitados:
            palabra = ''
            if visitados[i] is False:
                palabra += self.dfs(i, visitados)
                comp.append(palabra)

        # print(comp)
        return len(comp) == 1  # Si es conexo, solo hay una componente

    def dfs(self, v, visitados):
        """Recorrido depth-first"""
        visitados[v] = True
        # print(v, end='\t')

        for adj in self._vertices[v]:
            if visitados[adj] is False:
                self.dfs(adj, visitados)
        return v

    def is_bridge(self, v1: str, v2: str) -> bool:
        inicial = self.is_connected()
        if inicial is False:  # Si inicialmente el grafo no es conexo, no tiene aristas puente
            return False

        # Comprobamos que la unión v1 -- v2 existe
        if v1 not in self._vertices[v2]:
            return False
        if v2 not in self._vertices[v1]:
            return False

        # Borramos la arista, y comprobamos si el grafo resultante sigue siendo conexo
        self._vertices[v1].remove(v2)
        self._vertices[v2].remove(v1)

        borrado = self.is_connected()

        # Como hemos borrado la conexión, hay que volver a añadirla
        self.add_edge(v1, v2)

        return borrado == False  # Si es falso, primero era conexo, y al borrar ya no lo era


if __name__ == '__main__':
    # Create a graph: A<->B<->C<->D
    vertices = ['A', 'B', 'C', 'D']
    g = MyGraph(vertices)
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
    print("First graph: ", str(g))
    print()
    print("is_connected()={}\n".format(g.is_connected()))  # True
    # assert g.is_connected()

    u, v = 'A', 'B'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'B', 'A'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'A', 'C'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # assert not g.is_bridge(u, v)

    u, v = 'A', 'D'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # assert not g.is_bridge(u, v)

    u, v = 'B', 'C'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'C', 'B'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'B', 'D'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # assert not g.is_bridge(u, v)

    u, v = 'C', 'D'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'D', 'C'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    # second graph
    print('Second graph:')
    vertices = ['A', 'B', 'C', 'D', 'E']
    g = MyGraph(vertices)
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'C')
    g.add_edge('A', 'D')
    g.add_edge('D', 'E')
    print(g)

    print("is_connected()={}\n".format(g.is_connected()))  # True
    #  assert g.is_connected()

    u, v = 'A', 'B'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # assert not g.is_bridge(u, v)

    u, v = 'A', 'C'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # assert not g.is_bridge(u, v)

    u, v = 'B', 'C'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # assert not g.is_bridge(u, v)

    u, v = 'A', 'D'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'D', 'A'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'D', 'E'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'E', 'D'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # True
    # assert g.is_bridge(u, v)

    u, v = 'B', 'E'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # assert not g.is_bridge(u, v)

    u, v = 'A', 'E'
    print("is_bridge({},{})={}\n".format(u, v, g.is_bridge(u, v)))  # False
    # assert not g.is_bridge(u, v)

    print('Third graph:')
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    g3 = MyGraph(vertices)
    g3.add_edge('A', 'B')
    g3.add_edge('B', 'C')
    g3.add_edge('C', 'D')
    g3.add_edge('C', 'E')
    g3.add_edge('D', 'E')
    g3.add_edge('D', 'F')
    g3.add_edge('D', 'G')
    g3.add_edge('E', 'F')
    print(g3)

    u, v = 'A', 'B'
    print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # True
    # assert g3.is_bridge(u, v)

    u, v = 'B', 'A'
    print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # True
    # assert g3.is_bridge(u, v)

    u, v = 'B', 'C'
    print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # True
    # assert g3.is_bridge(u, v)

    u, v = 'D', 'G'
    print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # True
    # assert g3.is_bridge(u, v)

    u, v = 'C', 'E'
    print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # False
    # assert not g3.is_bridge(u, v)

    u, v = 'D', 'F'
    print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # False
    # assert not g3.is_bridge(u, v)

    u, v = 'D', 'E'
    print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # False
    # assert not g3.is_bridge(u, v)

    u, v = 'C', 'D'
    print("is_bridge({},{})={}\n".format(u, v, g3.is_bridge(u, v)))  # False
    # assert not g3.is_bridge(u, v)
