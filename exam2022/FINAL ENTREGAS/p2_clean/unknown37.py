#Irene Subías Serrano
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visited = {}
        hecho = False
        for vertex in self._vertices.keys():
            visited[vertex] = False
        for vertex in self._vertices.keys():
            if not hecho:
                self._bfs(vertex, visited)
                hecho = True
        for v in self._vertices:
            if not visited[v]:
                return False
        return True
    def _bfs(self, vertex, visited) -> None:
        cola = []
        visited[vertex] = True
        cola.append(vertex)
        while cola:
            s = cola.pop(0)
            for adj in self._vertices[s]:
                if not visited[adj]:
                    cola.append(adj)
                    visited[adj] = True
    def is_bridge(self, v1: str, v2: str) -> bool:
        conectado = self.is_connected()
        return not conectado
