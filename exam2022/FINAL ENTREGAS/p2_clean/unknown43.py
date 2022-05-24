    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visited = {}
        print(list(self._vertices.keys())[0])
        for vertex in self._vertices.keys():
            visited[vertex] = False
        first_vertex = list(self._vertices.keys())[0]
        self._dfs(first_vertex, visited)
        for vertex in visited:
            if visited[vertex] == False:
                return False
        return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        if v2 not in self._vertices.get(v1) or v1 not in self._vertices.get(v2):
            return False
        self._vertices.get(v1).remove(v2)
        self._vertices.get(v2).remove(v1)
        result = not self.is_connected()
        self.add_edge(v1, v2)
        return result
    def _dfs(self, vertex: str, visited: dict) -> None:
        visited[vertex] = True
        for adj in self._vertices[vertex]:
            # adj is an object of AdjacentVertex
            if not visited[adj]:
                self._dfs(adj, visited)
