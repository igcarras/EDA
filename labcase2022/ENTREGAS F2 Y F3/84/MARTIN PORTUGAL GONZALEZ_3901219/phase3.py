from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        diccionario = {}
        for i in self._vertices:
            diccionario[i] = [False, 0]
        diccionario[start][0] = True
        lista = []
        lista.append(start)
        while lista:
            s = lista.pop(0)
            for i in range(len(self._vertices[s])):
                if diccionario[self._vertices[s][i].vertex][0] == False:
                    diccionario[self._vertices[s][i].vertex][0] = True
                    diccionario[self._vertices[s][i].vertex][1] = diccionario[s][1] + 1
                    lista.append(self._vertices[s][i].vertex)

        return diccionario[end][1]
    """Se crea un diccionario donde se meten todos los vértices, junto a listas con False y 0, posteriormente se van 
       actualizando estos valores para saber si han sido visitados y cual es la distancia """

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        if self._directed == True:
            traspuesto = Graph2(self._vertices)
            for i in self._vertices:
                for j in self._vertices[i]:
                    traspuesto._vertices[j.vertex].append(AdjacentVertex(i, j.weight))
            return traspuesto

        return self

    """En el método transpose se crea un grafo nuevo con las mismos vértices, y posteriormente en funcion de las aristas 
       del grafo original se añaden las aristas traspuestas en funcio de j e i, cogiendo el vertice inicial del AdjVertex 
       y el final del primer bucle que va pasando por todas las keys del diccionario"""

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        for i in self._vertices:
            for j in self._vertices:
                if self.min_number_edges(i, j) == 0 and i != j:
                    return False

        return True

    """Esta basada en el primer metodo, el cual te permitia saber si habia caminos entre dos vertices, en este metodo se 
       comprueba si existen caminos entre todos los vertices"""