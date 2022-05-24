    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visitados = {}
        for vertice in self._vertices.keys():
            visitados[vertice] = False
        for vertice in self._vertices.keys():
            if not visitados[vertice]:
                self._conexiones_dfs(vertice, visitados)
        for vertice in self._vertices.keys():
            if visitados[vertice]:
                return True
        return None
    def is_bridge(self, v1: str, v2: str) -> bool:
        if self.is_connected:
            if v1 in self._vertices and v2 in self._vertices and v1 in self._vertices[v2] and v2 in self._vertices[v1]:
                self._vertices[v1].remove(v2)
                self._vertices[v2].remove(v1)
                conexo = self.is_connected
                self._vertices[v1].append(v2)
                self._vertices[v2].append(v1)
                if conexo:
                    return True
        return False
    def _conexiones_dfs(self, v, visitados):
        visitados[v] = True
        for adj in self._vertices[v]:
            vertice_adj = adj
            if not visitados[vertice_adj]:
                self._conexiones_dfs(vertice_adj, visitados)
