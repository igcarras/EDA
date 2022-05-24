"""
Nombre: Iván Merchán Ruiz
NIA: 100451135
"""
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        if self != None:
            for v1 in self._vertices.keys():
                for v2 in self._vertices.keys():
                    if self.conectados(v1, v2) != True:
                        return False
            return True
        return False
    def is_bridge(self, v1: str, v2: str) -> bool:
        i1 = self.existev(v1)
        i2 = self.existev(v2)
        if i1 == -1 or i2 == -1:
            return False
        if self.is_connected:
            self._vertices[v1] = None
            for v in self._vertices.keys():
                for v2 in self._vertices.keys():
                    if self.conectados(v, v2) != True:
                        return True
        return False
# Funciones Auxiliares
    def existev(self, v):
        #Comprueba que v existe en el grafo
        for i in self._vertices.keys():
            if self._vertices[i] == v:
                return i
        return -1
    def conectados(self, v1, v2):
        #Comprueba si dos vertices están conectados
        i1 = self.existev(v1)
        i2 = self.existev(v2)
        if i1 == -1:
            return False
        if i2 == -1:
            return False
        for adj in self._vertices[i1]:
            if adj.vertex == i2:
                return True
        return False
