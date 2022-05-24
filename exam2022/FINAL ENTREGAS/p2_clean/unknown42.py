# Miguel Salas Heras
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visited = {}
        frist_vertex = None
        for v in self._vertices.keys():
            if not frist_vertex:
                frist_vertex = v
            visited[v] = False
        self.recorrido(frist_vertex,visited)
        for v in self._vertices.keys():
            if not visited[v]:
                return False
        return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        if v1 not in self._vertices.keys() or v2 not in self._vertices.keys():
            return False
        if v1 not in self._vertices[v2] or v2 not in self._vertices[v1]:
            return False
        self._vertices[v1].remove(v2)
        self._vertices[v2].remove(v1)
        if not self.is_connected():
            self._vertices[v1].append(v2)
            self._vertices[v2].append(v1)
            return True
        self._vertices[v1].append(v2)
        self._vertices[v2].append(v1)
        return False
    def recorrido(self,vertex,visited):
        visited[vertex] = True
        for v in self._vertices[vertex]:
            if not visited[v]:
                self.recorrido(v, visited)
