import graph
from graph import AdjacentVertex
from graph import Graph
import sys

class Graph2(Graph):

    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        if start not in self._vertices.keys() or end not in self._vertices.keys():
            print("Uno de los vértices no existe")
            return None

        aristas_recorridas = self._min_number_edges(start)
        if aristas_recorridas[end] == sys.maxsize:
            return 0

        return aristas_recorridas[end]

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        if self._directed:
            # Grafo de apoyo
            self.new_graph = graph.Graph(self._vertices, self._directed)

            for v1 in self._vertices.keys():
                # v1 son los vertices del grafo
                for v2 in self._vertices[v1]:
                    # v2 vertices adyacentes a v1
                    self.new_graph.add_edge(v2.vertex, v1, v2.weight)

            self._vertices = self.new_graph._vertices
        return self

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        for v1 in self._vertices:
            if len(self._is_strongly_connected(v1)):
                return False
        return True

#--------------------------------------------------min_number_edges-----------------------------------------------------

    def _min_number_edges(self, start):

        vertices_visitados  = {}  # Diccionario de visitados
        aristas_recorridas = {}  # El valor es la distancia minima de aristas desde el origen
        valores_previos = {}  # Valores de los vertices previos con el valor de ruta minimo

        # Diccionarios por defecto
        for v in self._vertices.keys():
            vertices_visitados[v] = False
            aristas_recorridas[v] = sys. maxsize
            valores_previos[v] = None

        # La aristas que ha recorrido desde el origen es 0
        aristas_recorridas[start] = 0

        # Recorremos todos los vertices
        for _ in range(len(self._vertices)):
            # Cogemos el vertice que recorre menos aristas
            u = self.ver_min_aristas_recorridas(aristas_recorridas, vertices_visitados)
            vertices_visitados[u] = True

            # Vemos los vertices adyacentes a u
            for adj in self._vertices[u]:
                i = adj.vertex
                número_aristas = 1

                # Para los vertices no vistados, vemos si la distancia de aristas es menor
                if not vertices_visitados[i] and aristas_recorridas[i] > aristas_recorridas[u]+número_aristas:
                    # Si la distancia es menor la actualizamnos
                    aristas_recorridas[i] = aristas_recorridas[u]+número_aristas
                    valores_previos[i] = u

        return aristas_recorridas

    def ver_min_aristas_recorridas(self, aristas_recorridas, vertices_visitados):
        """Devuelve el vertice no visitado que menos arista ha recorrido"""

        # Inicializacion por defecto
        min_aristas_recorridas = sys.maxsize
        min_vertex = None

        # Devuelve el vertice que menos aristas ha recorrido
        for vertex in self._vertices.keys():
            if aristas_recorridas[vertex] <= min_aristas_recorridas and not vertices_visitados[vertex]:
                min_aristas_recorridas = aristas_recorridas[vertex]  # Nuevo vertice con menos recorrido
                min_vertex = vertex

        return min_vertex

#-----------------------------------------is_strongly_connected---------------------------------------------------------

    def _is_strongly_connected(self, vertex):
        """
        Devuelve una lista con los vertice a los que no puede llegar desde un vertice determinado
        """

        vertices_visitados = {}  # Diccionario con los vertices visitados
        for v1 in self._vertices:
            vertices_visitados[v1] = False
        self.acesibilidad_vertice(vertex, vertices_visitados)

        result = []  # lista con los vertices no accesibles
        for v1 in self._vertices:
            if not vertices_visitados[v1]:
                result.append(v1)

        return result

    def acesibilidad_vertice(self, vertex, vertices_visitados):
        """
        Esta función visita todos los vertices posibles a los que puedes llegar desde un dicho vertice
        """
        vertices_visitados[vertex] = True
        for adj in self._vertices[vertex]:
            adj_vertex = adj.vertex
            if not vertices_visitados[adj_vertex]:
                self.acesibilidad_vertice(adj_vertex, vertices_visitados)

