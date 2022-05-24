# Pablo Sánchez Redondo
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visitados = {}
        for v in self._vertices.keys():
            visitados[v]: False
        queue = []
        for i in visitados:
            if len(queue) < 1:
                queue.append(i)
        while queue:
            s = queue.pop()
            visitados[s]: True
            for adj in self._vertices[s]:
                if not visitados[adj]:
                    queue.append(visitados[adj])
        for i in visitados:
            if not visitados[i]:
                return False
        return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        if v2 not in self._vertices[v1] or v1 not in self._vertices[v2]:
            return False
        self._vertices[v1].remove(v2)
        self._vertices[v2].remove(v1)
        if self.is_connected():
            return False
        else:
            return True
