#ALEJANDRO ASENCIO BECERRA

from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):

    def find(self, v: str, final: str, counter: int, min_way: int):

        if v == final:
            return counter

        else:
            if min_way == None or counter + 1 <= min_way:
                for i in self._vertices[v]:
                    if min_way == None or counter + 1 <= min_way:
                        aux_way = self.find(i.vertex, final, counter+1, min_way)
                        if min_way == None or aux_way < min_way:
                            min_way = aux_way

            return min_way


    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        way = self.find(start, end, 0, None)

        if way:
            return way

        else:
            return 0


    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        v = []
        if self._directed == False:
            return self
        else:
            for i in self._vertices.keys():
                v.append(i)

            tgraph = Graph2(v)

            for a in self._vertices.keys():
                for u in self._vertices[a]:
                    tgraph.add_edge(u.vertex, a)

        return tgraph


    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        for i in self._vertices:
            visited = [i]
            attached = [i, None]
            while len(attached) != None:
                aux = attached.pop(0)
                if aux == None:
                    attached.append(None)

                    if attached[0] == None:
                        break

                else:
                    for a in self._vertices[aux]:
                        if a.vertex not in visited:
                            visited.append(a.vertex)
                            attached.append(a.vertex)

            if len(visited) < len(self._vertices):
                return False

        return True


