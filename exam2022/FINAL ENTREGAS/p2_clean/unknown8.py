"""Daniel Gómez Magro Problema 2"""
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        for i in self._vertices.keys():
            visitados=[]
            accesibles=[]
            self._profundidad(i,visitados,accesibles)
            if len(self._vertices)!=len(accesibles):
                return False
        return True
    def _profundidad(self,v,visitados,accesibles):
        if v not in visitados:
            visitados.append(v)
            accesibles.append(v)
            for j in self._vertices[v]:
                self._profundidad(j,visitados,accesibles)
    def is_bridge(self, v1: str, v2: str) -> bool:
        if v1 not in self._vertices.keys():
            return False
        if v2 not in self._vertices.keys():
            return False
        if v2 not in self._vertices[v1]:
            return False
        if v1 not in self._vertices[v2]:
            return False
        self.remove_edge(v1,v2)
        if self.is_connected():
            self.add_edge(v1,v2)
            return False
        if self.is_connected() == False:
            self.add_edge(v1,v2)
            return True
    def remove_edge(self, v1: object, v2: object):
        for adj in self._vertices[v1]:
            if adj == v2:
                self._vertices[v1].remove(adj)
        for adj in self._vertices[v2]:
            if adj == v1:
                self._vertices[v2].remove(adj)
