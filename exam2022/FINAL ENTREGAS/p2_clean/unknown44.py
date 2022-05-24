    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        for vertex in self._vertices.keys():
            lista_nueva = []
            visited = []
            self.DFS(vertex, visited, lista_nueva)
            if len(self._vertices) != len(lista_nueva):
                return False
        return True
    def DFS(self, vertex, visited, lista_nueva):
        if vertex not in visited:
            visited.append(vertex)
            lista_nueva.append(vertex)
            for adj in self._vertices[vertex]:
                self.DFS(adj, visited, lista_nueva)
    def is_bridge(self, v1: str, v2: str) -> bool:
        if not self.check_vertex(v1):
            return False
        if not self.check_vertex(v1):
            return False
        exist1 = False
        for adj in self._vertices[v1]:
            if adj == v2:
                exist1 = True
        exist2 = False
        for adj in self._vertices[v2]:
            if adj == v1:
                exist2 = True
        if not exist1 and not exist2:
            return False
        self.remove_edge(v1, v2)
        if not self.is_connected():
            self.add_edge(v1, v2)
            return True
        else:
            self.add_edge(v1, v2)
            return False
    def remove_edge(self, v1: str, v2: str):
        for adj in self._vertices[v1]:
            if adj == v2:
                self._vertices[v1].remove(adj)
        for adj in self._vertices[v2]:
            if adj == v1:
                self._vertices[v2].remove(adj)
