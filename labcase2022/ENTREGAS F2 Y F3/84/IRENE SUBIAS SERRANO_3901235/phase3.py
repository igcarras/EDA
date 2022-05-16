import sys

from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        visited = {}    # Para cada vertice, el valor es un buleano indicando si el vertice ha sido visitado
        distances = {}  # Para cada vertice, el valor es la distancia minima en el camino minimo desde el origen
        for v in self._vertices.keys():
            # Inicializar todos los diccionarios
            visited[v] = False

            distances[v] = sys.maxsize
        # La distancia del primero a si mismo es 0
        distances[start] = 0

        for n in range(len(self._vertices)):
            # escoge el vertice no visitado más cercano
            u = self.min_distance(distances, visited)
            visited[u] = True
            # Coge los adyacentes de u
            if u != end and u:
                for adj in self._vertices[u]:
                    i = adj.vertex
                    # para vertices no visitados, hay que comprobar si su distancia es mayor que la distancia desde u
                    if not visited[i] and distances[i] > distances[u]+1:
                        # Hay que actualizar porque la distancia es mayor a la nueva
                        distances[i] = distances[u] + 1
            elif not u:
                return 0
            else:
                return distances[end]
    def min_distance(self, distances: dict, visited: dict) -> int:
        """Devuelve el vertice cuyo valor asociado en el diccionario distancias es el más pequeño.
        solo se considera el grupo de vertices no visitados aún"""
        # Inicializa la mínima distancia para el próximo nodo
        min_distance = sys.maxsize
        min_vertex = None
        # Devuelve el vertice con minima distancia
        for vertex in self._vertices.keys():
            if distances[vertex] <= min_distance and not visited[vertex] and distances[vertex] != sys.maxsize:
                min_distance = distances[vertex]  # actualiza la nueva distancia más pequeña
                min_vertex = vertex      # actualiza el vertice de esa distancia
        return min_vertex

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        # Crea un nuevo grafo que va a ser el transpuesto
        g = Graph2(self._vertices.keys())
        # Recorre los vertices y sus adyacentes
        for v in self._vertices:
            for adj in self._vertices[v]:
                # Añade los vertices transpuestos
                g._vertices[adj.vertex].append(AdjacentVertex(v, adj.weight))
        return g

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        # Recorre cada vértice
        for v in self._vertices:
            # Lista con booleanos de si un vertice ha sido visitado
            visited = {}
            for v1 in self._vertices:
                visited[v1] = False
            # Dfs recorre el grafo y todos los vertices que se pueden visitar
            self._dfs(v, visited)
            # Si algún vertice no ha sido visitado, devuelve False
            for v1 in self._vertices:
                if not visited[v1]:
                    return False
        return True

    def _dfs(self, vertex: object, visited_vertex: dict) -> None:
        # Marca el nodo actual como visitado
        visited_vertex[vertex] = True
        # Repite pra todos los vertices adyacentes
        for adj in self._vertices[vertex]:
            if not visited_vertex[adj.vertex]:
                # Si uno de los vertices adyacentes no han sido vistados hace recursión
                self._dfs(adj.vertex, visited_vertex)
