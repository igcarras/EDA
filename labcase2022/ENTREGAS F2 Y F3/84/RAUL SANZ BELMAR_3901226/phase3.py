from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        fin = False
        camino = 0
        nodos = [start]
        visitados = []
        while not fin:
            a = len(nodos)
            e = 0
            print("ejecucion", camino,  nodos, visitados)
            for i in range(a):
                if nodos[i - e] == end:
                    return camino
                for actual in self._vertices[nodos[i - e]]:
                    if actual.vertex not in visitados and actual.vertex not in nodos:
                        nodos.append(actual.vertex)
                visitados.append(nodos[i - e])
                del(nodos[i - e])
                e += 1
            camino += 1
            fin = len(nodos) == 0
        return 0

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        if not self._directed:
            return self
        else:
            vertices = []
            for llave in self._vertices:
                vertices.append(llave)
            graph = Graph2(vertices, True)
            for llave in self._vertices:
                for arista in self._vertices[llave]:
                    graph.add_edge(arista.vertex, llave)
            return graph

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        if not self._directed:

            a = 0
            for i in self._vertices.keys():
                if a == 0:
                    nodos = [i]
                    a = 1

            visited = {}
            for v in self._vertices.keys():
                visited[v] = False
            fin = False
            while not fin:
                for nodo in nodos:
                    visited[nodo] = True
                a = len(nodos)
                e = 0
                for i in range(a):
                    for actual in self._vertices[nodos[i - e]]:
                        if visited[actual.vertex] == False:
                            nodos.append(actual.vertex)
                    del (nodos[i - e])
                    e += 1
                fin = len(nodos) == 0
            f_conec = True
            for v in self._vertices.keys():
                if visited[v] == False:
                    f_conec = False
            return f_conec
        else:
            conectado = True
            for key in self._vertices.keys():
                visited = {}
                for v in self._vertices.keys():
                    visited[v] = False
                nodos = [key]
                fin = False
                while not fin:
                    for nodo in nodos:
                        visited[nodo] = True
                    a = len(nodos)
                    e = 0
                    for i in range(a):
                        for actual in self._vertices[nodos[i - e]]:
                            if visited[actual.vertex] == False:
                                nodos.append(actual.vertex)
                        del (nodos[i - e])
                        e += 1
                    fin = len(nodos) == 0
                for v in self._vertices.keys():
                    if visited[v] == False:
                        return False
            return conectado
