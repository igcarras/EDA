# Mario Rodríguez Román Grupo 84
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False
        aux = list(self._vertices.keys())
        #con comprobar que un vértice está unido con los demas es suficiente, ya que es un grafo no dirigido
        x = aux[0]
        self._dfs(x, visited)
        for i in self._vertices.keys():
            if not visited[i]:
                return False
        return True
    def _dfs(self, vertex, visited: dict):
        if not visited[vertex]:
            visited[vertex] = True
            for v in self._vertices[vertex]:
                self._dfs(v, visited)
    def is_bridge(self, v1: str, v2: str) -> bool:
        if v2 not in self._vertices[v1] or v1 not in self._vertices[v2] or not self.check_vertex(
                v2) or not self.check_vertex(v1):
            return False
        self._vertices[v1].remove(v2)
        self._vertices[v2].remove(v1)
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False
        aux = list(self._vertices.keys())
        x = aux[0]
        self._dfs(x, visited)
        for i in self._vertices.keys():
            if not visited[i]:
                self.add_edge(v1, v2)
                return True
        self.add_edge(v1, v2)
        return False
