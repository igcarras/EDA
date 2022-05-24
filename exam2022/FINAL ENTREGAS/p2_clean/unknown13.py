"Pablo Albendea Obispo"
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visitado = {}
        for vertex in self._vertices:
            visitado[vertex] = False
        accesibles = self.dfs(visitado)
        accedidos = ()
        for visita in accesibles:
            if accesibles[visita] == False:
                return False
        return True
    def dfs(self, visitado):
        for vertex in self._vertices.keys():
                self._dfs(vertex, visitado)
        return visitado
    def _dfs(self, vertice, visitado):
        for adj in self._vertices[vertice]:
            if not visitado[adj]:
                visitado[vertice] = True
                return self._dfs(adj, visitado)
        return visitado
    def remove_edge(self, v1, v2):
        self._vertices[v1].remove(v2)
        self._vertices[v2].remove(v1)
    def is_bridge(self, v1: str, v2: str) -> bool:
        if not v2 in self._vertices[v1]:
            return False
        else:
            #Borro la arista para comprobar si es puente
            Grafo_prueba = MyGraph(self._vertices)
            Grafo_prueba._vertices = self._vertices
            Grafo_prueba.remove_edge(v1, v2)
            NoPuente = Grafo_prueba.is_connected()
            Grafo_prueba.add_edge(v1, v2)
            if NoPuente:
                return False
            else:
                return True
