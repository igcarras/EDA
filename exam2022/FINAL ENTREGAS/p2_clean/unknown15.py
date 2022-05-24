    def dfs(self):
        visited_vertex = {}
        for vertex in self._vertices.keys():
            visited_vertex[vertex] = False
        for vertex in self._vertices.keys():
            if not visited_vertex[vertex]:
                self._dfs(vertex, visited_vertex)
    def _dfs(self, vertex, visited_vertex):
        visited_vertex[vertex] = True
        for adj in self._vertices[vertex]:
            if not visited_vertex[adj]:
                self._dfs(adj, visited_vertex)
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visited_vertex = {}
        for vertex in self._vertices.keys():
            visited_vertex[vertex] = False
        for vertex in self._vertices.keys():
            if not visited_vertex[vertex]:
                self._dfs(vertex, visited_vertex)
        for v in self._vertices:
            if visited_vertex[v]:
                return True
            else:
                return False
    def is_bridge(self, v1: str, v2: str) -> bool:
        if (v1 or v2) not in self._vertices:
            return False
        for v in self._vertices:
            self.dfs()
            return True
        else:
            return False
    def _is_bridge(self,v1,v2,visited):
        visited[v1] = True
        for v in self._vertices[v2]:
            if not visited[v]:
                self._is_bridge(v1,v2,visited)
