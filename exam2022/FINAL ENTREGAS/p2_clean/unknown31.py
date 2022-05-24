# David Serrano Sangrador
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        # como el grafo es no dirigido, si para un solo vértice nos sale verdadero, el resto también será verdadero
        # y estará fuertemente conectado
        lista = []
        for v in self._vertices:
            lista.append(v)
        visited = self.bfs(lista[0])
        for adj in visited:
            if visited[adj] == False:
                return False
        return True
    def bfs(self, v):
        visited = {}
        for v in self._vertices:
            visited[v] = False
        return self._bfs(v, visited)
    def _bfs(self, v, visited):
        queue = []
        visited[v] = True
        queue.append(v)
        while queue:
            s = queue.pop(0)
            for adj in self._vertices[s]:
                if visited[adj] == False:
                    visited[adj] = True
                    queue.append(adj)
        return visited
    def is_bridge(self, v1: str, v2: str) -> bool:
        lista = []
        for v in self._vertices:
            lista.append(v)
        visited = self.bfs2(lista[0], v1, v2)
        for adj in visited:
            if visited[adj] == False:
                return False
        return True
    def bfs2(self, v, v1, v2):
        visited = {}
        for v in self._vertices:
            visited[v] = False
        # marcamos las aristas v1 y v2 como visitadas para que de este modo, no se pueda recorrer,
        # de este modo, esta que los conecta sería inutil y sería como si no existiera y en caso de que solo hubiera
        # esa, quedaría inutilizada
        visited[v1] = True
        visited[v2] = True
        return self._bfs(v, visited)    # reutilizamos el bfs oculto
