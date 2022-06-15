    def is_connected(self) -> bool:
        for vertex in self._vertices:
            visited = {}
            for v in self._vertices.keys():
                visited[v] = False
            result = self._is_connected(vertex, visited)
            if not result:
                return False
        return True

    def _is_connected(self,vertex, visited:list)-> bool:
        visited[vertex] = True
        for adj in self._vertices[vertex]:
            if not visited[adj]:
                self._is_connected(adj, visited)
        for v in visited:
            if visited[v] == False:
                return False
        return True

    def is_bridge(self, v1: str, v2: str) -> bool:
        if v1 in self._vertices[v2] and v2 in self._vertices[v1]:
            New = self
            New.eliminar(v1, v2)#Eliminamos la arista y comprobamos que sea conexo el nuevo grafo
            result = not New.is_connected()
            New.add_edge(v1, v2) #devolvemos la arista, para no modificar el grafo
            return result
        return False



    def eliminar(self, start: object, end: object):
        if start not in self._vertices.keys():
            return
        if end not in self._vertices.keys():
            return
        for adj in self._vertices[start]:
            if adj == end:
                self._vertices[start].remove(adj)
        for adj in self._vertices[end]:
            if adj == start:
                self._vertices[end].remove(adj)
