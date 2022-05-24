#Marina Pérez Barbero
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visited ={}
        for v in self._vertices:
            visited[v] = False
        lis = []
        for v in self._vertices:
            u = self.dfs(v)
            print(u)
            if len(u) != len(self._vertices):
                return False
        return True
        #return None
    def dfs(self,v):
        lis = []
        visited = {}
        for n in self._vertices:
            visited[n] = False
        return self._dfs(v, visited, lis)
    def _dfs(self,v,visited,lis):
        visited[v] = True
        #print(v)
        if v not in lis:
            lis.append(v)
        for adj in self._vertices[v]:
            if visited[adj] == False:
                self._dfs(adj, visited,lis)
        return lis
    def is_bridge(self, v1: str, v2: str) -> bool:
        lista = list(self._vertices.keys())
        aux = MyGraph(lista)
        aux = self
        #a = aux.is_connected()
        print("a",self._vertices[v1])
        self._vertices[v1].remove(v2)
        print("b",self._vertices[v1])
        print("c", self._vertices[v2])
        self._vertices[v2].remove(v1)
        print("d", self._vertices[v2])
        if len(self._vertices[v1]) == 0:
            self._vertices[v1].append(v2)
            self._vertices[v2].append(v1)
            return True
        elif len(self._vertices[v2]) ==0:
            self._vertices[v1].append(v2)
            self._vertices[v2].append(v1)
            return True
        else:
            self._vertices[v1].append(v2)
            self._vertices[v2].append(v1)
            return False
        #return False
