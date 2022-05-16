"""Module"""
import sys
from graph import AdjacentVertex
from graph import Graph


class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        # Complejidad n²
        """returns the minimum number of edges from start to end"""
        distancia = self.dijkstra(start)
        num = distancia[end]
        if num == sys.maxsize:
            num = 0
        print(distancia[end])
        return num

    def dijkstra(self, origen):
        # Complejidad n²
        visitados = {}
        previo = {}
        distancias = {}
        for i in self._vertices.keys():
            visitados[i] = False
            previo[i] = -1
            distancias[i] = sys.maxsize

        distancias[origen] = 0

        for n in range(len(self._vertices)):
            u = self.minimum_distance(distancias, visitados)
            visitados[u] = True

            for v in self._vertices[u]:
                i = v.vertex
                weight = v.weight
                if visitados[i] is False and distancias[i] > distancias[u] + weight:
                    distancias[i] = distancias[u] + weight
                    previo[i] = u
        return distancias

    def minimum_distance(self, distancias, visitados):
        # Complejidad n
        minimo = sys.maxsize

        for i in self._vertices:
            if distancias[i] <= minimo and visitados[i] is False:
                minimo = distancias[i]
                min_index = i

        return min_index

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        # Complejidad n²
        grafo = Graph2(self._vertices.keys(), self._directed)

        for i in self._vertices:
            for j in self._vertices[i]:
                if not self._directed and grafo.contain_edge(j.vertex, i) == 0:
                    # Si no es dirigido solo hacemos la conexión una vez
                    grafo.add_edge(j.vertex, i, j.weight)
                if self._directed:
                    grafo.add_edge(j.vertex, i, j.weight)
        return grafo

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        # Complejidad n ~ Algoritmo Kosaraju es lineal

        return self._connected()

    def _connected(self):
        """Algoritmo de Kosaraju & depth-first search"""
        claves = self._vertices.keys()

        visitados = {}
        for i in claves:  # Marcamos todos como no visitados
            visitados[i] = False

        pila = []
        for j in claves:  # Visitar todos los nodos y los añadimos a la cola en orden depth-first
            if visitados[j] is False:
                self.visitar(j, visitados, pila)

        traspuesta = self.transpose()

        for i in claves:  # Volvemos a marcar todos como no visitados
            visitados[i] = False

        lista_final = []  # Guarda los conjuntos de elementos conexos como strings

        while pila:
            i = pila.pop()
            if visitados[i] is False:
                lista_final.append(traspuesta.depth_first_traversal(i, visitados))

        # print(lista_final, len(lista_final))
        # Si solo hay un string → Solo hay un elemento conexo / Todo el grafo es conexo
        return len(lista_final) == 1

    def depth_first_traversal(self, nodo, visitados) -> str:
        """Método para recorrer el grafo depth-first y devuelve las componentes conexas todas juntas en un string"""
        visitados[nodo] = True
        word = nodo
        for i in self._vertices[nodo]:
            if visitados[i.vertex] is False:
                word += self.depth_first_traversal(i.vertex, visitados)
        return word

    def visitar(self, nodo, visitados, pila):
        """Marca el nodo actual como visitado y luego visitamos todos sus vecinos"""
        visitados[nodo] = True

        for i in self._vertices[nodo]:
            if visitados[i.vertex] is False:
                self.visitar(i.vertex, visitados, pila)
        pila.append(nodo)
