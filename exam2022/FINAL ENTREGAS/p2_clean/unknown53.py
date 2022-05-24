# ALUMNO: JAVIER PRATS MUÑOZ
# GRUPO: 84
    def is_connected(self) -> bool:
        # returns True if the graph is connected, False eoc
        for vertex1 in self._vertices.keys():
            visited_vertex = {}
            path = []
            for v in self._vertices.keys():
                visited_vertex[v] = False
            self.dfs(vertex1, visited_vertex, path)
            for vertex2 in self._vertices.keys():
                if vertex1 != vertex2:
                    if vertex2 not in path:
                        return False
        return True
    def dfs(self, vertex: object, visited_vertex: dict, path: list) -> None:
        visited_vertex[vertex] = True
        for adjacent in self._vertices[vertex]:
            if not visited_vertex[adjacent]:
                path.append(adjacent)
                self.dfs(adjacent, visited_vertex, path)
    def is_bridge(self, v1: str, v2: str) -> bool:
        if (not self.check_vertex(v1)) or (not self.check_vertex(v2)):
            return False
        if v1 == v2:
            return False
        if v1 not in self._vertices[v2]:
            return False
        self._vertices[v1].remove(v2)
        self._vertices[v2].remove(v1)
        if self.is_connected():
            self.add_edge(v1, v2)
            return False
        self.add_edge(v1, v2)
        return True
