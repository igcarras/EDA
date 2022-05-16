from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        if start not in self._vertices.keys() or end not in self._vertices.keys(): # comprobar que existen los vértices
            return 0
        niveles = {}
        visitados = {}
        for v in self._vertices.keys(): # poner a todos los vértices como no visitados y en nivel 0
            visitados[v] = False
            niveles[v] = 0
        # hacer un recorrido bfs desde start
        queue = []
        queue.append(start)
        visitados[start] = True
        while queue:
            u = queue.pop(0)
            print(u)
            for adj in self._vertices[u]:
                if visitados[adj.vertex] == False:
                        queue.append(adj.vertex)
                        visitados[adj.vertex] = True
                        # subir un nivel a los vértices adyacentes
                        niveles[adj.vertex] = niveles[u] + 1
                if adj.vertex == end:
                    # cuando estamos en el vértice end, devolvemos su nivel
                    return niveles[end]
        # si no llegamos al end devolvemos 0, ya que no hay arista que llegue a end
        return 0

    def transpose(self) -> 'Graph2':
        """ devuelve un grafo traspuesto"""
        # creamos un grafo con los mismos vertices que el original
        transpuesto = Graph2(self._vertices.keys())
        # mediante un bucle añadimos las aristas al nuevo grafo con los 
        # vértices invertidos
        for v in self._vertices.keys():
            for adj in self._vertices[v]:
                transpuesto.add_edge(adj.vertex, v)
        return transpuesto

    def is_strongly_connected(self) -> bool:
        """ verifica si el grafo es fuertemente conexo"""
        # creamos un grafo traspuesto
        grafo2 = self.transpose()
        # ponemos a todos los vértices en no visitados
        visited1 = {}
        visited2 = {}
        for v in self._vertices.keys():
            visited1[v] = False
        for w in grafo2._vertices.keys():
            visited2[w] = False
        start = list(self._vertices.keys())[0]
        # recorremos ambos grafos en dfs
        self._dfs(start, visited1)
        grafo2._dfs(start, visited2)
        # si están todos los vértices visitados, significa que es fuertemente conexo
        for v in self._vertices.keys():
            if visited1[v] == False:
                return False
        for w in grafo2._vertices.keys():
            if visited2[w] == False:
                return False
        return True

    def _dfs(self, v, visited):
        """ recorre el grafo en profundidad desde un vértice"""
        visited[v] = True
        for adj in self._vertices[v]:
            if visited[adj.vertex] == False:
                self._dfs(adj.vertex, visited)
