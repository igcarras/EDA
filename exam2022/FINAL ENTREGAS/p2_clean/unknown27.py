# Cristina López Alcázar
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        # creamos un diccionario de visitados y lo rellenamos con False
        visitados = {}
        for w in self._vertices.keys():
            visitados[w] = False
        # elegimos un vértice y realizamos un recorrido bfs
        v = list(self._vertices.keys())[0]
        queue = []
        queue.append(v)
        visitados[v] = True
        while queue:
            u = queue.pop(0)
            for adj in self._vertices[u]:
                if visitados[adj] == False:
                    queue.append(adj)
                    visitados[adj] = True
        # como es un grafo no dirigido, si algún vértice está sin visitar, no es conexo
        for w in self._vertices.keys():
            if visitados[w] == False:
                return False
        return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        # comprobamos si contiene la arista
        c = self.contains(v1, v2)
        # eliminamos la arista
        self.removeEdge(v1, v2)
        # si tras eliminar la arista sigue siendo conexo, no es arista puente
        if self.is_connected():
            result = False
        else:
            result = True
        # para dejar el grafo como era antes, si contenía la arista, la volvemos a añadir
        if c:
            self.add_edge(v1, v2)
        return result
    def removeEdge(self, v1: str, v2: str):
        # elimina la arista
        if not self.check_vertex(v1):
            return
        if not self.check_vertex(v2):
            return
        for v in self._vertices.keys():
            if v == v1:
                for adj in self._vertices[v]:
                    if adj == v2:
                        self._vertices[v].remove(adj)
        for w in self._vertices.keys():
            if w == v2:
                for adj in self._vertices[w]:
                    if adj == v1:
                        self._vertices[w].remove(adj)
    def contains(self, v1: str, v2: str):
        # comprueba si la arista existe
        if not self.check_vertex(v1):
            return
        if not self.check_vertex(v2):
            return
        # como en el enunciado nos dicen que no es dirigido, si no está en una dirección, tampoco lo estará
        # en la otra, por ello, sólo comprobamos en una dirección
        for v in self._vertices.keys():
            if v == v1:
                for adj in self._vertices[v]:
                    if adj == v2:
                        return True
        return False
