# MIKEL UGARTE PLAZAOLA
    def remove_edge(self,start,end):
        if start not in self._vertices.keys():
            return
        if end not in self._vertices.keys():
            return
        for adj in self._vertices[start]:
            if adj.vertex==end:
                self._vertices[start].remove(adj)
    def is_connected(self,) -> bool:
        """returns True if the graph is connected, False eoc"""
        todo_vertices = list(self._vertices.keys())
        for i in self._vertices.keys():
            booleano = [False]
            vertices= []
            self._is_connected(i, vertices, todo_vertices, booleano)
            if booleano[0] == False:
                return False
        return True
    def _is_connected(self,vertice,vertices,allverts,booleano):
        vertices.append(vertice)
        if len(vertices) == len(allverts):
            booleano[0] = True
        for i in self._vertices[vertice]:
            if i not in vertices:
                self._is_connected(i, vertices, allverts, booleano)
    def is_bridge(self, v1: str, v2: str) -> bool:
        todo_vertices=list(self._vertices.keys())
        newgraph=MyGraph(todo_vertices)
        if v1 or v2 not in self._vertices.keys():
            return False
        newgraph.remove_edge(v1,v2)
        resultado=newgraph.is_connected()
        if resultado==False:
            return True
        else:
            return False
