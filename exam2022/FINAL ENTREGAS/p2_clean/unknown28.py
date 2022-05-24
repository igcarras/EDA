    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        for v in self._vertices.keys():
            visited = []
            ad = []
            self._is_conected(v, visited, ad)
            if len(self._vertices) != len(ad):
                return False
        return True
    def _is_conected(self,v,visited,adjacentes):
        if v not in visited:
            visited.append(v)
            adjacentes.append(v)
            for adj in self._vertices[v]:
                self._is_conected(adj, visited, adjacentes)
    def is_bridge(self, v1: str, v2: str) -> bool:
        #Comprobar que existen
        if v1 not in self._vertices.keys():
            print("ERROR:", v1, "no pertenece al grafo")
            return False
        if v2 not in self._vertices.keys():
            print("ERROR:", v2, "no pertenece al grafo")
            return False
        #Comprbar que existe la arista
        existe = False
        for adj in self._vertices[v1]:
            if adj == v1:
                existe = True
            return existe
        self._remove_edge(v1,v2)
        return self.is_connected()
    def _remove_edge(self, v1, v2):
        for adj in self._vertices[v1]:
            if adj.vertex == v2:
                self._vertices[v1].remove(adj)
        # Como no es dirigido borras en ambos sentidos
        for adj in self._vertices[v2]:
            if adj.vertex == v1:
                self._vertices[v2].remove(adj)
