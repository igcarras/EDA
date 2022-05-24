#Aitana Ortiz Guiño
    def DFS(self, vertex, visited, lista_nueva):
        if vertex not in visited:
            visited.append(vertex)
            lista_nueva.append(vertex)
            for j in self._vertices[vertex]:
                self.DFS(j, visited, lista_nueva)
    def is_connected(self):
        for vertex in self._vertices.keys():
            lista_nueva = []
            visited = []
            self.DFS(vertex, visited, lista_nueva)
            if len(self._vertices) != len(lista_nueva):
                return False
        return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        # por alguno motivo no me compruba el caso de que no exita la arista pero bueno
        if v1 not in self._vertices.keys() or v2 not in self._vertices.keys():
            return False
        self._vertices[v1].remove(v2)
        self._vertices[v2].remove(v1)
        if not  self.is_connected():
            self._vertices[v1].append(v2)
            self._vertices[v2].append(v1)
            return True
        else:
            self._vertices[v1].append(v2)
            self._vertices[v2].append(v1)
            return False
