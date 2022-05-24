    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visitados = {}
        for v in self._vertices.keys():
            visitados[v] = False
        for v in self._vertices.keys():
            if not visitados[v]:
                return self._is_connected(v,visitados)
    def _is_connected(self, v, visitados):
        cola = []
        visitados[v] = True
        cola.append(v)
        while cola:
            s = cola.pop(0)
            for adj in self._vertices[s]:
                if not visitados[adj]:
                    visitados[adj] = True
                    cola.append(adj)
        for n in visitados:
            if visitados[n] == False:
                return False
        return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False
        for v in self._vertices.keys():
            if not visited[v]:
                return self._is_connected(v, visited)
        """for v in self._vertices.keys():
            for adj in self._vertices.keys():
                if adj in v"""
        if v1 in self._vertices[v2]:
            #eliminar arista
             if not self._is_connected(v2, visited):
                 self.add_edge(v1,v2)
                 return False
             else:
                return True
