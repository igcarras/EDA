    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        for primer_vert in self._vertices:     #buscamos en todos los vertices del grafo
            vert_visitados = [primer_vert]
            adjuntos_vert = [primer_vert, None]      #establecemos cuales son los adjuntos y los vertices visitados
            while len(adjuntos_vert):     #miramos si el diccionario de adjuntos esta lleno
                x = adjuntos_vert.pop(0)
                if x != None:
                    for adjuntos in self._vertices[x]:       #en caso de que este lleno
                        if adjuntos not in vert_visitados:
                            adjuntos_vert.append(adjuntos)
                            vert_visitados.append(adjuntos)
            if len(self._vertices) > len(vert_visitados):     #comparamos si es el mismo len entre los visitados y los que de verdad tenemos
                return False
        return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        if v2 not in self._vertices and v1 not in self._vertices:     #comprobamos si los vertices que nos dan existen en el grafo dado
            return False         #sino devolvemos falso
        for adjunt in self._vertices[v2]:     #miramos los vecinos de v2
            if adjunt == v1:       #lo comparamos con v1
                self._vertices[v2].remove(v1)       #ahora quitamos las aristas y comprobamos si sigue estando conectado. Si ds true, no son puente y si da false son puente
                self._vertices[v1].remove(v2)
                connected = self.is_connected()
                self._vertices[v2].append(v1)
                self._vertices[v1].append(v2)
                if connected:             #devolvemos el resultado
                    return False
            return True
