#Pablo Garaulet Tovar
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visit = {}
        for v in self._vertices.keys():
            for adj in self._vertices:
                visit[adj] = False
            if  self.aux(self._vertices[v], visit, v, None):
                return True
            else:
                return False
    def aux(self, sig, c, r, s):
        if r == s:
            return all(c.values())
        else:
            pass
        for v in sig:
            if not c[v]:
                c[v] = True
                self.aux(self._vertices[v], c, r, v)
        return all(c.values())
    def is_bridge(self, v1: str, v2: str) -> bool:
        if v2 not in self._vertices[v1]:
            return False
        self._vertices[v1].remove(v2)
        self._vertices[v2].remove(v1)
        #conexo
        if self.is_connected():
            self.add_edge(v1, v2)
            return False
        else:
            self.add_edge(v1, v2)
        return True
