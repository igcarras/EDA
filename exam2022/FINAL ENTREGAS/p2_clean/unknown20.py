import copy
    def checkingConected(self,nextOnes,vis_copy,master,curV):
        if (master==curV):
            return all(vis_copy.values())
        for vertex in nextOnes:
            if not vis_copy[vertex]:
                vis_copy[vertex]=True
                self.checkingConected(self._vertices[vertex],vis_copy,master,vertex)
        return all(vis_copy.values())
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visitados = {}
        etique =  self._vertices.keys()
        for v in etique:
            for j in  self._vertices:
                visitados[j] = False
            if not self.checkingConected(self._vertices[v],visitados,v,None):
                return False
        return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        if v2 not in self._vertices[v1]:
            return False
        self._vertices[v1].remove(v2)
        self._vertices[v2].remove(v1)
        if(self.is_connected()):
            self.add_edge(v1, v2)
            return False
        self.add_edge(v1, v2)
        return True
