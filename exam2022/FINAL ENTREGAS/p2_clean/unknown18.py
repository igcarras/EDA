    def _find(self, vertex, vertices):
        for v in self._vertices[vertex]:
            if v not in vertices:
                vertices.append(v)
                self._find(v, vertices)
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        if len(self._vertices) > 0:
            vertices = []
            self._find(list(self._vertices.keys())[0], vertices)
            return len(vertices) == len(self._vertices)
    def is_bridge(self, v1: str, v2: str) -> bool:
        if self.is_connected() and v2 in self._vertices[v1]:
            self._vertices[v1].remove(v2)
            self._vertices[v2].remove(v1)
            conectado = self.is_connected()
            self._vertices[v1].append(v2)
            self._vertices[v2].append(v1)
            if not conectado:
                return True
        return False
