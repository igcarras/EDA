#Álvaro Moreno Martín
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        conexo = True
        if len(self._vertices) > 0:
            visitados = []
            self._is_connected(list(self._vertices.keys())[0], visitados)
            if len(visitados) < len(self._vertices):
                conexo = False
        return conexo
    def _is_connected(self, vertice: str, visitados: list):
        for vert in self._vertices[vertice]:
            if vert not in visitados:
                visitados.append(vert)
                self._is_connected(vert, visitados)
    def is_bridge(self, v1: str, v2: str) -> bool:
        if self.is_connected() and v2 in self._vertices[v1]: #Si el grafo es conexo y v2 está en la lista de adyacentes de v1 (la cual es el valor de la clave v1 del diccionario)
            self._vertices[v1].remove(v2) #eliminamos el vertice v2 adyacente a v1
            self._vertices[v2].remove(v1) #y viceversa por si es no dirigido
            connected = self.is_connected()
            self._vertices[v1].append(v2)
            self._vertices[v2].append(v1)
            if connected == False:
                return True
            else:
                return False
        else:
            return False
