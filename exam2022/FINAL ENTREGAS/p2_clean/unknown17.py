# Daniel Sánchez de la Cruz. NIA: 100475344
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visited = {}
        for v in self._vertices:
            visited[v] = False
        v = list(self._vertices)[0]
        self._dfs(v, visited)
        for v in visited:
            if not visited[v]:
                return False
        return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        # Devolvemos False si la arista no existe
        if v2 not in self._vertices[v1]:
            return False
        # Eliminamos la arista y comprobamos si el grafo es conexo
        self._vertices[v1].remove(v2)
        self._vertices[v2].remove(v1)
        result = not self.is_connected()
        # Volvemos a añadir la arista para devolver el grafo a su estructura original
        self._vertices[v1].append(v2)
        self._vertices[v2].append(v1)
        return result
    def _dfs(self, v, visited):
        visited[v] = True
        for u in self._vertices[v]:
            if not visited[u]:
                self._dfs(u, visited)
