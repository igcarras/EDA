#Raúl Sanz Belmar
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False
        cola = ['A']
        while cola:
            s = cola.pop(0)
            visited[s]=True
            "Accedemos a los adyacentes de A, si no los hemos visitado, los metemos a la cola"
            for adj in self._vertices[s]:
                for i in range(len(adj)):
                    if not visited[adj[i]]:
                        cola.append(adj[i])
        "Si no todos los vértices han sido visitados, significa que no es conexo el grafo"
        for v in self._vertices.keys():
            if visited[v]==False:
                return False
        return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        if not self.check_vertex(v1) or not self.check_vertex(v2):
            "No existe alguno de estos dos vértices"
            return False
        if v2 not in self._vertices[v1]:
            "No hay una arista que conecte esos dos vértices"
            return False
        "Eliminamos la arista para ver si sigue siendo conexo"
        self._vertices[v1].remove(v2)
        self._vertices[v2].remove(v1)
        "Vemos si es conexo por el anterior método"
        conexo = self.is_connected()
        "Introducimos la arista eliminada, ya que el grafo tiene que ser igual y no cambiar"
        self.add_edge(v1, v2)
        "Sigue siendo conexo: no era arista puente. No sigue siendo conexo: era arista puente"
        if conexo:
            return False
        return True
