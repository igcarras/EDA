    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        for vertice in self._vertices:
            visited = {}
            for v in self._vertices.keys():
                visited[v] = False
            if not self._is_connected(vertice, visited):
                return False
        return True
    def _is_connected(self, current, visited):
        visited[current] = True
        for adj in self._vertices[current]:
            if not visited[adj]:
                self._is_connected(adj, visited)
        for v in visited:
            if visited[v] == False:
                return False
        return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        if v1 not in self._vertices.keys() or v2 not in self._vertices.keys():
            print('No existe esa arista en el grafo')
            return False
        elif v1 not in self._vertices[v2]:
            print('No existe esa arista en el grafo')
            return False
        elif not self.is_connected():
            return False
        else:
            Aux_grafo = self
            Aux_grafo.remove(v1, v2)
            if not Aux_grafo.is_connected():
                solucion = True
            else:
                solucion = False
            Aux_grafo.add_edge(v1, v2)
            return solucion
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
