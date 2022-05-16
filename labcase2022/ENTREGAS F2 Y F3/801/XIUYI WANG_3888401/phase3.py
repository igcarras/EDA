from graph import Graph


class Graph2(Graph):

    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return -1
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return -1

        visited = {}
        for v in self._vertices.keys():
            visited[v] = False

        distance = {}
        for v in self._vertices.keys():
            distance[v] = 0

        queue = []
        distance[start] = 0
        distance[end] = 0

        queue.append(start)
        visited[start] = True
        while queue:
            s = queue.pop(0)
            for i in self._vertices[s]:
                if visited[i.vertex] is False:
                    distance[i.vertex] = distance[s] + 1
                    queue.append(i.vertex)
                    visited[i.vertex] = True

        return distance[end]

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        grafoT = Graph2(self._vertices, self._directed)
        if self._directed:
            for v in self._vertices.keys():
                for adj in self._vertices[v]:
                    u = adj.vertex
                    w = adj.weight
                    grafoT.add_edge(u, v, w)

            return grafoT
        return self

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
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
            if adj.vertex not in visited:
                self._dfs(adj.vertex, visited)
