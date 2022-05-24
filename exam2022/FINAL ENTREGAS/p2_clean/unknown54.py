# Jaime Espada Santos
    def dfs(self):
        visited = {}
        for v in self._vertices.keys():
            visited[v] == False
        for v in self._vertices.keys():
            if visited[v] == False:
                self._dfs(v, visited)
    def _dfs(self, v, visited):
        visited[v] = True
        for adj in self._vertices[v]:
            if visited[adj] == False:
                self._dfs(adj, visited)
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        if self.dfs: # Comprobamos si se puede ir de un elemento a otro del grafo
            return True
        return False
    def is_bridge(self, v1: str, v2: str) -> bool:
        if v1 == None or v2 == None:
            return False
        if v1 not in self._vertices or v2 not in self._vertices:
            return False
        return True
