# Cristina López Alcázar
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
        # creamos un diccionario de visitados y lo rellenamos con False
        visitados = {}
        for w in self._vertices.keys():
            visitados[w] = False
        # elegimos un vértice y realizamos un recorrido bfs
        v = list(self._vertices.keys())[0]
        queue = []
        queue.append(v)
        visitados[v] = True
        while queue:
            u = queue.pop(0)
            for adj in self._vertices[u]:
                if visitados[adj] == False:
                    queue.append(adj)
                    visitados[adj] = True
        # como es un grafo no dirigido, si algún vértice está sin visitar, no es conexo
        for w in self._vertices.keys():
            if visitados[w] == False:
                return False
        return True

    def is_bridge(self, v1: str, v2: str) -> bool:
        # comprobamos si contiene la arista
        c = self.contains(v1, v2)
        # eliminamos la arista
        self.removeEdge(v1, v2)
        # si tras eliminar la arista sigue siendo conexo, no es arista puente
        if self.is_connected():
            result = False
        else:
            result = True
        # para dejar el grafo como era antes, si contenía la arista, la volvemos a añadir
        if c:
            self.add_edge(v1, v2)
        return result

    def removeEdge(self, v1: str, v2: str):
        # elimina la arista
        if not self.check_vertex(v1):
            return
        if not self.check_vertex(v2):
            return
        for v in self._vertices.keys():
            if v == v1:
                for adj in self._vertices[v]:
                    if adj == v2:
                        self._vertices[v].remove(adj)
        for w in self._vertices.keys():
            if w == v2:
                for adj in self._vertices[w]:
                    if adj == v1:
                        self._vertices[w].remove(adj)

    def contains(self, v1: str, v2: str):
        # comprueba si la arista existe
        if not self.check_vertex(v1):
            return
        if not self.check_vertex(v2):
            return
        # como en el enunciado nos dicen que no es dirigido, si no está en una dirección, tampoco lo estará
        # en la otra, por ello, sólo comprobamos en una dirección
        for v in self._vertices.keys():
            if v == v1:
                for adj in self._vertices[v]:
                    if adj == v2:
                        return True
        return False

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
