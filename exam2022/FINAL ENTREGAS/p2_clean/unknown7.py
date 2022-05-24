    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        for v in self._vertices.keys():
            visited = []
            list = []
            self._adj(v, visited, list)
            if len(self._vertices) != len(list):
                return False
        return True
    def _adj(self, v, visited, lista):
        if v not in visited:
            visited.append(v)
            lista.append(v)
            for j in self._vertices[v]:
                self._adj(j, visited, lista)
    def is_bridge(self, v1: str, v2: str) -> bool:
        if v1 in self._vertices[v2] and v2 in self._vertices[v1]:
            g2 = self
            print(self)
            g2.remove(v1, v2)
            result = not g2.is_connected()
            g2.add_edge(v1, v2)
            print(self)
            return result
        return False
    def remove(self, v1: object, v2: object):
        if v1 not in self._vertices.keys() or v2 not in self._vertices.keys():
            return
        for adj in self._vertices[v1]:
            if adj == v2:
                self._vertices[v1].remove(adj)
        for adj in self._vertices[v2]:
            if adj == v1:
                self._vertices[v2].remove(adj)
