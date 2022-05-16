from graph import AdjacentVertex
from graph import Graph


class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        if start not in self._vertices.keys() or end not in self._vertices.keys():
            return 0
        visitados = {}
        camino = {}
        lista = []

        for v in self._vertices:
            visitados[v] = False
        for v in self._vertices:
            camino[v] = 0
        #Visitamos el vertice start
        visitados[start] = True
        lista.append(start)
        while lista:
            #Sacamos el primer vertice de la lista y buscamos sus vertices adyacentes
            vertice = lista.pop(0)
            for adj in self._vertices[vertice]:
                #Si no han sido visitados, los metemos en la lista, y cuando los visitamos añadimos uno al camino
                if visitados[adj.vertex] == False:
                    lista.append(adj.vertex)
                    visitados[adj.vertex] = True
                    camino[adj.vertex] = camino[vertice] + 1
                    #Cuando lleguemos al vertice end, devolvemos el camino
                    if adj.vertex == end:
                        return camino[end]
        return 0  #lista vacia
    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        #Creamos el grafo
        grafo_tras = Graph2(self._vertices.keys())
        for v in self._vertices:
            for adj in self._vertices[v]:
            #Trasponemos las aristas del grafo
                grafo_tras.add_edge(adj.vertex,v)

        return grafo_tras



    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        for v in self._vertices:
            unidos = []
            visitados = []
            unidos.append(v)
            visitados.append(v)
            while len(unidos):
                # Sacamos el primer vertice de la lista y buscamos sus vertices adyacentes
                vertice = unidos.pop(0)
                if vertice:
                    for adj in self._vertices[vertice]:
                        if adj.vertex not in visitados:
                            visitados.append(adj.vertex)
                            unidos.append(adj.vertex)
            #Si la lista de visitados es menor que la de los vertices, significa que no se han visitado/unido todos
            if len(visitados) < len(self._vertices):
                return False
        return True

