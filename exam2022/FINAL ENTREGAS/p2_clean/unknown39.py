# Manuel Sanz Muñoz
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visitados = []
        siguientes = []
        """las proximas 5 lineas sirven para escoger el vertice de inicio"""
        a = 0
        for vertice in self._vertices.keys():
            if a == 0:
                siguientes = [vertice]
                visitados = [vertice]
                a = 1
        """Para recorrer el grafo he usado la lista siguientes. Mientras contiene vertices busca los adjacentes a
        estos y si no estan visitados los añade a la lista para recorrerlos (tambien los marca como visitados
        para que no se añadan varias veces a la lista siguientes)"""
        while len(siguientes):
            for vertice in siguientes:
                for adjacente in self._vertices[vertice]:
                    if adjacente not in visitados:
                        visitados.append(adjacente)
                        siguientes.append(adjacente)
                siguientes.remove(vertice)
        connected = True
        for vertice in self._vertices.keys():
            if vertice not in visitados:
                connected = False
        return connected
    def is_bridge(self, v1: str, v2: str) -> bool:
        """elimina la arista del grafo, compruba si es conexo y almacena la respuesta luego añade la arista ota vez y
        devuelve True si v1-v2 era una arista puente)"""
        existe_arista = self.remove_edge(v1, v2)
        puente = not self.is_connected()
        if existe_arista:
            self.add_edge(v1, v2)
        return puente
    def remove_edge(self, v1, v2) -> bool:
        """devuelve falso si la arista no estaba en el grafo"""
        a = True
        if self.check_vertex(v1) and self.check_vertex(v2):
            if v2 in self._vertices[v1]:
                self._vertices[v1].remove(v2)
            else:
                a = False
            if v1 in self._vertices[v2]:
                self._vertices[v2].remove(v1)
            else:
                a = False
        else:
            a = False
        return a
