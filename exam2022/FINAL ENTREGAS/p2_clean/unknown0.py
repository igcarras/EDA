#Ignacio Tordable Mestres
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
        if v1 in self._vertices[v2] and v2 in self._vertices[v1]:
            grafoNuevo = self
            grafoNuevo.remove(v1, v2)
            solucion = not grafoNuevo.is_connected()
            grafoNuevo.add_edge(v1, v2)
            return solucion
        return False
    def remove(self, start: object, end: object):
        if start not in self._vertices.keys():
            return
        if end not in self._vertices.keys():
            return
        for adj in self._vertices[start]:
            if adj == end:
                self._vertices[start].remove(adj)
        for adj in self._vertices[end]:
            if adj == start:
                self._vertices[end].remove(adj)
