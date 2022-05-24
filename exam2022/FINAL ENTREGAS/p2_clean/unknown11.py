    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visited = {}
        visited2 = {}
        for i in self._vertices.keys():
            visited[i] = False
            visited2[i] = False
        for v in self._vertices.keys():
            self._dfs(v, visited)
            for adj in self._vertices[v]:
                self._dfs(adj, visited2)
                for v in self._vertices.keys():
                    if not (visited[v] or visited2[v]):
                        return False
        return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        graph=MyGraph(list(self._vertices))
        for v in self._vertices.keys():
            for adj in self._vertices[v]:
                graph.add_edge(v,adj)
        graph.remove_edge(v1,v2)
        if graph.is_connected():
            return False
        else:
            return True
    def _dfs(self,v,visited):
        visited[v] = True
        for adj in self._vertices[v]:
            if visited[adj]==False:
                self._dfs(adj,visited)
                visited[adj] = True
    def remove_edge(self, start: object, end: object):
        """ removes the edge (start, end)"""
        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return
        # we must look for the adjacent AdjacentVertex (neighbour)  whose vertex is end, and then remove it
        for adj in self._vertices[start]:
            if adj == end:
                self._vertices[start].remove(adj)
