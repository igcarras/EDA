    def is_connected(self) -> bool:
        return self.dfs()
    def dfs(self):
        stop=0
        visited={}
        for vertex in self._vertices.keys():
            visited[vertex]=False
        for vertex in self._vertices.keys(): #Si es conexo, con una sola iteracion basta para visitar todos los vertices
            if stop<=1:
                self._dfs(vertex,visited)
                stop+=1
        print ("VISITED",visited)
        for elem in visited:
            if visited[elem]==False:
                return False
        return True
    def _dfs(self,vertex,visited):
        visited[vertex]=True
        for adj in self._vertices[vertex]:
            if not visited[vertex]:
                self._dfs(visited)
    def is_bridge(self, v1: str, v2: str) -> bool:
        return None
