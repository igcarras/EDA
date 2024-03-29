class MyGraph:
    def add_edge(self, i, j):
        if i not in self._vertices.keys():
            return
        if j not in self._vertices.keys():
            return
        self._vertices[i].append(j)

    def has_path_to_odd(self, k) -> []:
        list_odd = []
        visited = {}
        #recorre vertices del grafo
        for v in self._vertices.keys():

            #para cada vertice del grafo inicializa vertices visitados
            for m in self._vertices.keys():

                visited[m] = False
            #recorre el grafo en profundidad para cada vertice (con vertices visitados a false)
            if self._has_path_to_odd(v, k, visited, v):
                #si cumple condición añade vertice v a la lista
                list_odd.append(v)
        return list_odd

    def _has_path_to_odd(self, vertex, k, visited, origin) -> bool:
        visited[vertex] = True
        r = False
        if k == 0:
            r = False
        elif vertex % 2 != 0 and vertex != origin:
            r = True
        else:
            for u in self._vertices[vertex]:
                if not visited[u]:
                    r = r or self._has_path_to_odd(u, k - 1, visited, origin)
        return r

    def has_path_to_odd2(self, k) -> []:
        list_odd = []
        #recorre vertices del grafo
        for v in self._vertices.keys():
            #para cada vertice del grafo inicializa vertices visitados

            #recorre el grafo en profundidad para cada vertice (con vertices visitados a false)
            self._has_path_to_odd2(v, k, v, list_odd)

        return list_odd

    def _has_path_to_odd2(self, vertex, k, origin, lista_parcial):
        for u in self._vertices[vertex]:
            if k > 0:
                if vertex % 2 != 0 and vertex != origin:
                    if origin not in lista_parcial:
                        lista_parcial.append(origin)

                self._has_path_to_odd2(u, k - 1, origin, lista_parcial)
        return


    def __init__(self, list_vertices):
        self._vertices = {}
        for i in list_vertices:
            self._vertices[i] = []


if __name__ == '__main__':
    # We use the class to represent an undirected graph without weights :
    # <img src='https://computersciencesource.files.wordpress.com/2010/05/dfs_1.png' width='35%'/>

    labels = [0, 1, 2, 3, 4]
    g = MyGraph(labels)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(2, 2)

    print("g -----------")
    print(g.has_path_to_odd2(2))
    print(g.has_path_to_odd2(3))
    print(g.has_path_to_odd(2))
    print(g.has_path_to_odd(3))
    print("g -----------")
    l=[2,4,6,8,10,12,14,16,15]
    g1=MyGraph(l)

    g1.add_edge(4,6)
    g1.add_edge(4,8)
    g1.add_edge(6,12)
    g1.add_edge(8,10)
    g1.add_edge(12,16)
    g1.add_edge(10,14)
    g1.add_edge(14,15)
    g1.add_edge(12,15)

    print("g1 starts  -----------")
    print(g1.has_path_to_odd2(13))
    print(g1.has_path_to_odd(13))
    print("g1 end -----------")

    l=[2,4,6,8,10,12,14,16,17, 20, 22, 24, 25]
    g2=MyGraph(l)

    g2.add_edge(2,4)
    g2.add_edge(4, 6)
    g2.add_edge(2,10)
    g2.add_edge(8,10)
    g2.add_edge(8,12)
    g2.add_edge(8,6)
    g2.add_edge(6,12)
    g2.add_edge(6,14)
    g2.add_edge(10,16)
    g2.add_edge(16,12)
    g2.add_edge(16,20)
    g2.add_edge(20,12)
    g2.add_edge(20,17)
    g2.add_edge(20,25)
    g2.add_edge(17,14)
    g2.add_edge(17,22)
    g2.add_edge(14,22)
    g2.add_edge(22,24)
    g2.add_edge(24,17)
    g2.add_edge(25,24)
    print("g2 -----------")
    print(g2.has_path_to_odd2(2))
    print(g2.has_path_to_odd2(3))
    print(g2.has_path_to_odd2(13))

    print(g2.has_path_to_odd(2))
    print(g2.has_path_to_odd(3))
    print(g2.has_path_to_odd(13))
    print("g2 -----------")
   #
    # l = []
    # g3 = MyGraph(l)
    # print(g3.has_path_to_odd(0))
    # print(g3.has_path_to_odd(-1))
    #
    # l = [0]
    # g4 = MyGraph(l)
    # print(g4.has_path_to_odd(0))
    # print(g4.has_path_to_odd(-1))
    #
    l = [2,4,6,8,10,12,14,16,18,20]
    g5 = MyGraph(l)
    g5.add_edge(2, 4)
    g5.add_edge(4, 6)
    g5.add_edge(2, 10)
    g5.add_edge(8, 10)
    g5.add_edge(8, 12)
    g5.add_edge(8, 6)
    g5.add_edge(6, 12)
    g5.add_edge(6, 14)
    g5.add_edge(10, 16)
    g5.add_edge(16, 12)
    g5.add_edge(16, 20)
    g5.add_edge(20, 12)

    print("g5 -----------")
    print(g5.has_path_to_odd(0))
    print(g5.has_path_to_odd(12))
    print(g5.has_path_to_odd2(0))
    print(g5.has_path_to_odd2(12))
    print("g5 -----------")

