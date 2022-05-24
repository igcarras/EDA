    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visitado = {}
        for v in self._vertices.keys():
            visitado[v] = False
        self._dfs(v, visitado)
        for v in self._vertices.keys():
            if not visitado[v]:
                return False
        return True
    def _dfs(self, v, visitado):
        for adj in self._vertices[v]:
            if not visitado[adj]:
                visitado[adj] = True
                self._dfs(adj, visitado)
    def is_bridge(self, v1: str, v2: str) -> bool:
        if self.is_connected() and v2 in self._vertices[v1]:
            self._vertices[v1].remove(v2)
            self._vertices[v2].remove(v1)
            resultado = self.is_connected()
            self._vertices[v1].append(v2)
            self._vertices[v2].append(v1)
            if not resultado:
                return True
        return False
