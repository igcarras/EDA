    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        for v in self._vertices:
            visited={}
            for v1 in self._vertices.keys():
                visited[v1]=False
            self._is_connected(v,visited)
            for v2 in self._vertices:
                if visited[v2]==False:
                    return False
        return True
    def _is_connected(self,vertex,visited):
        visited[vertex]=True
        for adj in self._vertices[vertex]:
            if visited[adj]==False:
                self._is_connected(adj,visited)
    def is_bridge(self, v1: str, v2: str) -> bool:
        for v in self._vertices:
            visited = {}
            for v4 in self._vertices.keys():
                visited[v4] = False
            self._is_bridge(v, visited,v1,v2)
            for v3 in self._vertices:
                if visited[v3] == False:
                    return False
        return True
    def _is_bridge(self, vertex, visited,v1,v2):
        visited[vertex] = True
        for adj in self._vertices[vertex]:
            if visited[adj] == False and (vertex==v1 and adj==v2) and (vertex==v2 and adj==v1):
                self._is_connected(adj, visited)
