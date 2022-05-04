from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False

        distance = {}
        queue = []
        # distance[start] = 0
        for v in distance.keys():
            distance[v] = 0

        queue.append(start)
        visited[start] = True
        while queue:
            s = queue.pop(0)
            for i in self._vertices[s]:
                if visited[i.vertex] is not True:
                    continue

                distance[end] = distance[i.vertex] + 1
                queue.append(i.vertex)
                visited[i.vertex] = True

        return distance[end]


    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        # Gtranspose = Graph2(self._vertices, self._directed)
        ...

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        ...

