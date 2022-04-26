from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return -1
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return -1

        visited_vertex = {}
        for vertex in self._vertices:
            visited_vertex[vertex] = False

        distances = {}
        for vertex in self._vertices:
            distances[vertex] = 0

        # mark the source start as visited
        visited_vertex[start] = True
        # and enqueue it
        queue = [start]

        while queue:
            vertex = queue.pop(0)
            # print(" visiting: ", vertex)

            # visit all its adjacent vertices of the dequeued index.
            for adj in self._vertices[vertex]:
                if not visited_vertex[adj.vertex]:
                    visited_vertex[adj.vertex] = True
                    distances[adj.vertex] = distances[vertex] + 1
                    queue.append(adj.vertex)

        return distances[end]

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        result = Graph2(self._vertices, self._directed)
        for u in self._vertices:
            for adj in self._vertices[u]:
                v = adj.vertex
                w = adj.weight
                result.add_edge(v, u, w)
        return result

    def dfs(self, vertex: str) -> list:
        """ returns the dfs traversal from vertex"""
        visited_vertex = {}
        for v in self._vertices:
            visited_vertex[v] = False

        path = []
        self._dfs(vertex, visited_vertex, path)
        return path, visited_vertex
        # return visited_vertex

    def _dfs(self, vertex: str, visited_vertex: dict, path: list) -> None:

        visited_vertex[vertex] = True
        path.append(vertex)
        # Recur for all the vertices  adjacent to this vertex
        for adj in self._vertices[vertex]:
            if not visited_vertex[adj.vertex]:
                self._dfs(adj.vertex, visited_vertex, path)

    def is_strongly_connected(self):
        """ a directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        This function checks if the graph is strongly connected"""

        for v in self._vertices:
            path, visited_vertex = self.dfs(v)
            for u in self._vertices:
                if u not in path:
                    return False

            # if any(i == False for i in visited_vertex.items()):
            #     return False

        # g = self.transpose()

        # for v in g._vertices:
            # path, visited_vertex = g.dfs(v)
            # for u in self._vertices:
            #    if u not in path:
            #        return False

            # if any(i == False for i in visited_vertex.items()):
             #    return False

        return True


