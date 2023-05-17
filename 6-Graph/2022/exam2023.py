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
        for v in self._vertices.keys():
            for m in self._vertices.keys():
                visited[m] = False
            if self._has_path_to_odd(v, k, visited, v):
                list_odd.append(v)
        return list_odd

    def _has_path_to_odd(self, vertex, k, visited, origin) -> []:
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


    print(g.has_path_to_odd(2))
    print(g.has_path_to_odd(3))

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


    print(g1.has_path_to_odd(13))
