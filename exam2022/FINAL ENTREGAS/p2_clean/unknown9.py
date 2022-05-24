        def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        for v in self._vertices.keys():
            path = self.dfs(v)
            for u in self._vertices:
                if u not in path:
                    return False
        return True
    def dfs(self, v):
        visited = []
        self._dfs(v, visited)
        return visited
    def _dfs(self, v, visited):
        visited.append(v)
        for adj in self._vertices[v]:
            if adj not in visited:
                self._dfs(adj, visited)
    def is_bridge(self, v1: str, v2: str) -> bool:
        # for v in self._vertices[v1]:
        #     self._is_bridge(v1, {}, v2)
        if self.is_connected():
            return False
        else:
            return True
    def _is_bridge(self, v, visited, parent):
        visited[v] = True
        for i in self._vertices[v]:
            if visited[i] == False:
                parent[i] = v
                self._is_bridge(v, visited, parent)
                if self.is_connected():
                    return False
            elif i != parent[v]:
                return True
