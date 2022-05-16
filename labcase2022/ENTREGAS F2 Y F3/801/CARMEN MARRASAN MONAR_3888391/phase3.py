from graph import AdjacentVertex
from graph import Graph


class Graph2(Graph):    
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        return self._min_number_edges(start, end, 0, 0 )
        
    def _min_number_edges(self, vertice:str, end: str, cont: int, camino: int):
        if vertice == end:
            return cont
        else:
            if camino == 0 or cont + 1 <= camino:
                for v in self._vertices[vertice]:
                    if camino == 0 or cont + 1 <= camino:
                        new = self._min_number_edges(v.vertex, end, cont + 1, camino)
                        if camino == 0 or new < camino:
                            camino = new
            return camino

            
    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        if self._directed == False:
            return self
        else:
            vertices = []
            for key in self._vertices.keys():
                vertices.append(key)
            Graphsol = Graph2(vertices)
            for k in self._vertices.keys():
                for v in self._vertices[k]:
                    Graphsol.add_edge(v.vertex, k)
            return Graphsol


    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        for vertex in self._vertices:   
            visited = {}
            for v in self._vertices.keys():
                visited[v] = False
            result = self._is_strongly_connected(vertex, visited)
            if not result:
                return False
        return True
    
    def _is_strongly_connected(self, vertex, visited):
        visited[vertex] = True
        for adj in self._vertices[vertex]:
            if not visited[adj.vertex]:
                self._is_strongly_connected(adj.vertex, visited)
        for v in visited:
            if visited[v] == False:
                return False
        return True
        
            
            
        
        
        

