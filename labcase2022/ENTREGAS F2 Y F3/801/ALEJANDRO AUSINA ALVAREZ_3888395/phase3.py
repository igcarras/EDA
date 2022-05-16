from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        recorrido = self._min_number_edges(start, end, 0, None)
        if recorrido:
            return recorrido
        else:
            return 0


    def _min_number_edges(self, vertice, final, distancia, camino):
        if vertice == final:
            return distancia
        else:
            if camino == None or distancia + 1 <= camino:
                for v in self._vertices[vertice]:
                    if camino == None or distancia + 1 <= camino:
                        camino_nuevo = self._min_number_edges(v.vertex, final, distancia + 1, camino)
                        if camino == None or camino_nuevo < camino:
                            camino = camino_nuevo

            return camino








    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        vertices2 = {}
        if not self._directed:
            return self
        for v in self._vertices:
            vertices2[v] = []
        for vertice in self._vertices:
            for vertice2 in vertices2:
                for nodo in self._vertices[vertice]:
                    if nodo.vertex == vertice2:
                        vertices2[vertice2].append(AdjacentVertex(vertice, weight= 1))

        self._vertices = vertices2

        return self




    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        for primer_vertice in self._vertices:
            adjunt = [primer_vertice, None]
            visited = [primer_vertice]
            while len(adjunt) != None:
                v = adjunt.pop(0)
                if v == None:
                    adjunt.append(None)
                    if adjunt[0] == None:
                        break
                else:
                    for adj in self._vertices[v]:
                        if adj.vertex not in visited:
                            visited.append(adj.vertex)
                            adjunt.append(adj.vertex)
            if len(visited) < len(self._vertices):
                return False
        return True

