    def dfs(self, vertex: str) -> list:
        """ returns the dfs traversal from vertex"""
        visited_vertex = {}
        for v in self._vertices:
            visited_vertex[v] = False
        path = []
        self._dfs(vertex, visited_vertex, path)
        return path, visited_vertex
        # return visited_vertex
    def _dfs(self, vertex: str, visited_vertex: dict, path: list) -> None:
        visited_vertex[vertex] = True
        path.append(vertex)
        # Recur for all the vertices  adjacent to this vertex
        for adj in self._vertices[vertex]:
            if not visited_vertex[adj.vertex]:
                self._dfs(adj.vertex, visited_vertex, path)
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False """
        for v in self._vertices:
            path, visited_vertex = self.dfs(v)
            for u in self._vertices:
                if u not in path:
                    return False
        return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        # una vez recibida la arista, la elimino
        # puede ser que la arista no exista
        # busco la conexión v1 v2
        # rompo la conexión del grafo, (elimino la arista)
        #newGraph = MyGraph(self)
        for v in self._vertices.keys():
            for j in self._vertices.keys():
                if j in self._vertices[v]:
                    if v == v1 and j == v2 or v == v2 and j ==v2:
                        self._vertices[v].pop(j)
                    #else:
                        #newGraph.add_edge(v, j)
        # compruebo si sigue siendo conexo tras la ruptura, llamo al
        # newGraph.
        # método is conected
        return self.is_connected()
