    def is_connected(self) -> bool:
        #Lo que vmas a hacer en esta funcion es comprobar
        #que visitamos todos los vertices
        visitados = [list(self._vertices.keys())[0]]
        cola = [list(self._vertices.keys())[0]]
        #recoremos una de las listas
        while len(cola):
            for vertex in self._vertices[cola.pop(0)]:
                if vertex not in visitados:
                    #si un vretice no esta en la lista de visitados lo añadimos
                    visitados.append(vertex)
                    cola.append(vertex)
        #por ultimo comparamos la longitud de la lista de visitados con la original de los vertices
        return len(self._vertices) == len(visitados)
    def is_bridge(self, v1: str, v2: str) -> bool:
        #caso base
        if v1 not in self._vertices.keys() or v2 not in self._vertices.keys():
            return False
        #Para comprobar to do eliminado la conexion v2 de v1 y v1 de v2
        self._vertices[v1].remove(v2)
        self._vertices[v2].remove(v1)
        #En caso de que no sea un grafo con todos los vertices conectados
        #le añadimos a cada uno su conexion  y devolvemos true
        if not self.is_connected():
            self._vertices[v1].append(v2)
            self._vertices[v2].append(v1)
            return True
        #En caso contrario devolvemos false
        self._vertices[v1].append(v2)
        self._vertices[v2].append(v1)
        return False
