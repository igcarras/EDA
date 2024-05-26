from graph import Graph

class Graph2(Graph):
    def dfs(self):
        visitados = {}
        for v in self._vertices.keys():
            visitados[v] = False
        for v in self._vertices:
            if not visitados[v]:
                self._dfs(v, visitados)
    def _dfs(self, vertice, visitados):
        visitados[vertice] = True
        print("Estoy en el vértice:", vertice)
        for ady in self._vertices[vertice]:
            if not visitados[ady.vertex]:
                self._dfs(ady.vertex, visitados)
    def is_connected(self, vertice):
        if vertice not in self._vertices.keys():
            print("el vertice pasado por parametro no se encuentra en la lista")
            return -1
        visitados = {}
        for v in self._vertices.keys():
            visitados[v] = False
        self._dfs(vertice, visitados)
        for v in visitados:
            if not visitados[v]:
                return False
        return True

    def is_brigde(self, u, v):
        visitados = {}
        for v in self._vertices.keys():
            visitados[v] = False
        self.remove_edge(u, v)
        self._dfs(u, visitados)
        for v in visitados:
            print("Compruebo vertices visitados")
            print(visitados[v])
            if not visitados[v]:
                print("holaaa")
                return True
        return False



vertices = ["a", "b", "c", "d", "e"]
g = Graph2(vertices, False)
g.add_edge("a", "b", 1)
g.add_edge("a", "c", 1)
g.add_edge("b", "c", 1)
g.add_edge("a", "d", 1)
g.add_edge("d", "e", 1)
print(g)

#print(g.is_connected("a"))
print(g.is_brigde("a", "d"))




