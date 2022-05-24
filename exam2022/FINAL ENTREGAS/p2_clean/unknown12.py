class queue:
      def __len__(self):
         return len(self.items)
      def isEmpty(self):
        return len(self)==0
      def enqueue(self,e):
         self.items.append(e)
      def dequeue(self):
        if self.isEmpty():
           return None
        return self.items.pop(0)
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        for v in self._vertices:
            path, visited_vertex = self.dfs(v)
            for u in self._vertices:
                if u not in path:
                    return False
    def _dfs(self, vertex: str, visited_vertex: dict, path: list) -> None:
        visited_vertex[vertex] = True
        path.append(vertex)
        for adj in self._vertices[vertex]:
            if not visited_vertex[adj.vertex]:
                self._dfs(adj.vertex, visited_vertex, path)
    def is_bridge(self, v1: str, v2: str) -> int:
        """returns the minimum number of edges from start to end"""
        if v1 not in self._vertices.keys():
            return -1
        if v2 not in self._vertices.keys():
            return -1
        visited_vertex = {}
        for vertex in self._vertices:
            visited_vertex[vertex] = False
        distances = {}
        for vertex in self._vertices:
            distances[vertex] = 0
        visited_vertex[v1] = True
        queue = [v1]
        while queue:
            vertex = queue.pop(0)
            for adj in self._vertices[vertex]:
                    visited_vertex[adj.vertex] = True
                    distances[adj.vertex] = distances[vertex] + 1
                    queue.append(adj.vertex)
        return distances[v2]
