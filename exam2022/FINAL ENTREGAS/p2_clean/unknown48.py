# Álvaro Santos García
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visited = {}
        for x in self._vertices.keys():
            visited[x] = False
        # Este for solo se ejecuta una vez
        for z in self._vertices.keys():
            if visited[z] is False:
                self._is_connected(z, visited)
            if False in visited.values():
                return False
            else:
                return True
    def _is_connected(self, z: str, visited: dict) -> None:
        visited[z] = True
        for adj in self._vertices[z]:
            if not visited[adj]:
                self._is_connected(adj, visited)
    def is_bridge(self, v1: str, v2: str) -> bool:
        if self.conectado(v1, v2) == 0:
            return False
        self.remove(v1, v2)
        aux = self.is_connected()
        self.add_edge(v1, v2)
        if aux is True:
            return False
        else:
            return True
    def remove(self, v1: str, v2: str) -> None:
        for adj in self._vertices[v1]:
            if adj == v2:
                self._vertices[v1].remove(adj)
        for adj in self._vertices[v2]:
            if adj == v1:
                self._vertices[v2].remove(v1)
    def conectado(self, v1: str, v2: str) -> int:
        for adj in self._vertices[v1]:
            if adj == v2:
                return 1
        return 0
