    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visited = {}
        for vertex in self._vertices:
            visited[vertex] = False
        for adj in self._vertices:
            if adj not in visited:
                visited[adj] = True
        for v in visited:
            if visited[v] == False:
                return False
            else:
                return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        return False
