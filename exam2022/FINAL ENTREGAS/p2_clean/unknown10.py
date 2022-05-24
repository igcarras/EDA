    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        for n in self._vertices.keys():
            visited=[]
            lista=[]
            self._dfs(n,visited,lista)
            if len(self._vertices)!=len(lista):
                return False
        return True
    def _dfs(self,v,visited,lista):
        if v not in visited:
            visited.append(v)
            lista.append(v)
            for i in self._vertices[v]:
                self._dfs(i,visited,lista)
    def is_bridge(self, v1: str, v2: str) -> bool:
        if self.is_connected():
            if v1 in self._vertices[v2]:
                self._vertices[v2].remove(v1)
                self._vertices[v1].remove(v2)
                conectados = self.is_connected()
                self._vertices[v2].append(v1)
                self._vertices[v1].append(v2)
                if conectados==False:
                    return True
        return False
