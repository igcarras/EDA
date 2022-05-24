    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        resultado = False
        visited = {}
        for vertex in self._vertices.keys():
            visited[vertex] = False
        self._is_connected(vertex, visited)
        for vertice in self._vertices.keys():
            if not visited[vertice]:
                return False
            else:
                resultado = True
        return resultado
    def _is_connected(self, vertex: object, visited: dict) -> None:
        queue = []
        visited[vertex] = True
        queue.append(vertex)
        while queue:
            s = queue.pop(0)
            for adjacent in self._vertices[s]:
                if not visited[adjacent]:
                    queue.append(adjacent)
                    visited[adjacent] = True
    def is_bridge(self, v1: str, v2: str) -> bool:
        if v1 is None or v2 is None:
            return False
        if self._vertices[v1] == v2 and self._vertices[v2] == v1:
            return True
        else:
            return False
