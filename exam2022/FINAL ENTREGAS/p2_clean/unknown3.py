    def _is_connected(self, v, visited):
        visited[v] = True
        for adj in self._vertices[v]:
            if not visited[adj]:
                self._is_connected(adj, visited)
        for v in visited:
            if visited[v] == False:
                return False
        return True

    def is_connected(self) -> bool:
        for v in self._vertices:
            visited = {}
            for adj in self._vertices.keys():
                visited[adj] = False
            if not self._is_connected(v, visited):
                return False
        return True


    def is_bridge(self, v1: str, v2: str) -> bool:
        if v1 in self._vertices[v2] and v2 in self._vertices[v1]:
            aux_graph = self
            aux_graph.remove(v1, v2)
            solution = not aux_graph.is_connected()
            aux_graph.add_edge(v1, v2)
            return solution
        return False




    def remove(self, start: object, end: object):
        if start not in self._vertices.keys():
            return None
        if end not in self._vertices.keys():
            return None
        for adj in self._vertices[start]:
            if adj == end:
                self._vertices[start].remove(adj)
        for adj in self._vertices[end]:
            if adj == start:
                self._vertices[end].remove(adj)
