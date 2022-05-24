#Paula Subías Serrano
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        for v in self._vertices:
            visited= {}
            for n in self._vertices:
                visited[n] = False
            self._dfs(v, visited)
            for v in visited:
                if visited[v] == False:
                    return False
        return True
    def _dfs(self, vertex: object, visited: dict) -> None:
        visited[vertex] = True
        for adj in self._vertices[vertex]:
            if not visited[adj]:
                self._dfs(adj, visited)
    def is_bridge(self, v1: str, v2: str) -> bool:
        if v2 in self._vertices[v1]:
            self._vertices[v1].remove(v2)
            self._vertices[v2].remove(v1)
            if self.is_connected():
                self.add_edge(v1,v2)
                return False
        else:
            return False
        self.add_edge(v1,v2)
        return True
