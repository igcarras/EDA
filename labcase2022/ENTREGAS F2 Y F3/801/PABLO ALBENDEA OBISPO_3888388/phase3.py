from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        aristas = 0
        if start == end:
            return aristas
        else:
            if self._vertices[start]:
                for adjunto in self._vertices[start]:
                    if not adjunto:
                        return aristas
                    elif adjunto.vertex == end:
                        aristas += 1
                        return aristas
                    else:
                        return self._min_number_edges(adjunto.vertex, end, aristas)
            else:
                return aristas

    def _min_number_edges(self, actual, end, aristas):
        for adjunto in self._vertices[actual]:
            if adjunto.vertex == end:
                aristas += 1
                if not self._directed:
                    aristas += 1
                return aristas
            else:
                aristas += 1
                return self._min_number_edges(adjunto.vertex, end, aristas)



    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        trans = Graph2(self._vertices.keys())

        for v in self._vertices.keys():
            for adj in self._vertices[v]:
                trans.add_edge(adj.vertex, v)

        return trans

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        #Utilizo los métodos auxiliares para comprobar si cada vértice tiene acceso a cada vértice, si alguno no tiene acceso devolvemos false, en caso contrario devolvemos true.
        for vertice in self._vertices:
            no_accesible = self.non_accessible(vertice)
            if len(no_accesible) != 0:
                return False
        return True





    def _dfs(self, vertex: str, visited: dict) -> None:
        visited[vertex] = True
        for adj in self._vertices[vertex]:
            # adj is an object of AdjacentVertex
            adj_vertex = adj.vertex
            if not visited[adj_vertex]:
                self._dfs(adj_vertex, visited)

    def non_accessible(self, vertex: str) -> list:
        """gets a vertex and returns the list of vertices
              that cannot be reached from vertex, that is, there is no path
              from vertex to these vertices"""
        # First, we need to obtain all vertices that can be
        # reached from vertex. To do this, we can apply
        # the algorithms of dfs or bfs
        visited = {}
        for v1 in self._vertices:
            visited[v1] = False
        self._dfs(vertex, visited)
        # The function _dfs will visit all vertices reachable
        # from vertex. Therefore, the non-visited vertices
        # will form the list of non-accessible vertices from vertex
        result = []  # list with the non-accessible vertices
        for v1 in self._vertices:
            if not visited[v1]:
                result.append(v1)

        return result



