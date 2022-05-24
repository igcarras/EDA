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
        # Usaremos bfs para intentar recorrer to do el grafo a partir de un solo vértice y ver si es conexo
        visitados = {}
        for v in self._vertices.keys():
            visitados[v] = False
        visitados = self._bfs(visitados, list(self._vertices.keys())[0]) # Con el diccionario de visitados podemos comprobar
        for e in visitados.keys(): #  si hay algun vértice que sea inaccesible
            if not visitados[e]:
                return False # Si hay alguno no visitado devolveremos False
        return True # Si se visitan todos se devuelve True
        # Al ser un grafo no dirigido  solo es necesario hacer una comprobacion, ya que las aristas tienen ambos sentidos
    
    
    def _bfs(self, visitados, v):
        cola = []
        cola.append(v) # Se añade a la cola el vertice inicial y se marca como visitado
        visitados[v] = True
        while cola:
            s = cola.pop(0)
            for ady in self._vertices[s]: # Se hace los mismo con cada vértice adyacente a el actual y asi sucesivamente,
                if not visitados[ady]:    # hasta que se agote la cola o no queden más vertices sin visitar
                    cola.append(ady)
                    visitados[ady] = True
        return visitados


    def is_bridge(self, v1: str, v2: str) -> bool:
        if not self.check_vertex(v1) or not self.check_vertex(v2): # Se comprueba que existen ambos vértices
            return False
        if v2 not in self._vertices[v1]: # Se comprueba que existe la arista
            return False

        self._vertices[v1].remove(v2) # Se elimina la arista
        self._vertices[v2].remove(v1)  
        respuesta = not self.is_connected() #Se mira si es conexo el grafo modificado. Si lo es, la arista no era puente y viceversa
        self.add_edge(v1, v2) # Se vuelve a colocar la arista eliminada
        return (respuesta)


if __name__ == '__main__':
    # Create a graph: A<->B<->C<->D
    vertices = ['A', 'B', 'C', 'D']
    g = MyGraph(vertices)
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
    print(g)
    g.is_bridge('A', 'B')
    print(g)
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
