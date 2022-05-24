    def _depth(self, vert, visitado, listVert):
        if vert not in visitado:
            visitado.append(vert)
            listVert.append(vert)
            for i in self._vertices[vert]:
                self._depth(i, visitado, listVert)
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        for i in self._vertices.keys():
            visitado = checkList = []
            self._depth(i, visitado, checkList)
            if len(self._vertices) != len(checkList):
                return False
        return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        if not self.check_vertex(v1):
            # v1 no es un vertice
            return False
        if not self.check_vertex(v2):
            # v2 no es un vertice
            return False
        if v1 == v2:
            # son el mismo vertice
            return False
        if v2 in self._vertices[v1] or v1 in self._vertices[v2]:
            print("({},{}) multiple edges are not allowed!".format(v1, v2))
            return False
        self._vertices[v1].remove(v2)
        self._vertices[v2].remove(v1)
        if self.is_connected:
            return True
        else:
            return False
