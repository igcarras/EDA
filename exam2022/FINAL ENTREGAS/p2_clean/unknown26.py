#Luis González Pérez, Grupo 801, NIA 100475299
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        if len(self._vertices) > 1:
            #Empezando por el primer vértice
            visitados = [list(self._vertices.keys())[0]]
            #Se visitan los vertices por dfs
            self.visitar(visitados[0], visitados)
            #Si se han podido visitar todos los vertices desde el inicial, es conexo
            return len(visitados) == len(self._vertices)
        #Si el grafo tiene 0 o 1 vertices será conexo
        return True
    def visitar(self, vertice, visitados):
        #Si no se han visitado, se visitan todos los vertice adyacentes al actual
        for v in self._vertices[vertice]:
            if v not in visitados:
                visitados.append(v)
                #Se repite para cada vértice adyacente
                self.visitar(v, visitados)
    def is_bridge(self, v1: str, v2: str) -> bool:
        #Comprobamos que existan los vertices y la arista
        if v1 in self._vertices and v2 in self._vertices and v1 in self._vertices[v2] and v2 in self._vertices[v1]:
            #Borramos la arista
            self._vertices[v1].remove(v2)
            self._vertices[v2].remove(v1)
            #Comprobamos que ahora no sea connexo
            conexo = self.is_connected()
            #Volvemos a colocar la arista
            self._vertices[v1].append(v2)
            self._vertices[v2].append(v1)
            #Si es conexo con la arista no conexo sin ella, la arista es puente
            return self.is_connected() and not conexo
        return False
