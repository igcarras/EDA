from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""

        vertices_visitados = {}
        for v in self._vertices.keys():
            vertices_visitados[v] = False
            
        camino = {}
        for v in self._vertices.keys():
            camino[v] = 0
            
        cola = []
        vertices_visitados[start] = True
        cola.append(start)
        while cola:
            primero = cola.pop(0)
            print(primero, end = " ")            
            for adj in self._vertices[primero]:
                if vertices_visitados[adj.vertex] == False:
                    cola.append(adj.vertex)
                    vertices_visitados[adj.vertex] = True
                    camino[adj.vertex] = camino[primero] + 1
                    if adj.vertex == end:
                        return camino[end]
        return 0  # Si no entra al bucle es porque el grafo está vacío


    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        traspuesto = Graph2(self._vertices.keys(), self._directed)

        for n, adjuntos in self._vertices.items():
            for adjunto in adjuntos:
                nombre = adjunto.vertex
                peso = adjunto.weight
                traspuesto._vertices[nombre].append(AdjacentVertex(n, peso))

        return traspuesto

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        id = []

        for n in self._vertices.keys():
            id.append(n)

        for v1 in id:
            for v2 in id:
                if v1 != v2: #no miro consigo mismo
                    aristas = self.min_number_edges(v1, v2)
                    if aristas == 0:
                        return False

        return True