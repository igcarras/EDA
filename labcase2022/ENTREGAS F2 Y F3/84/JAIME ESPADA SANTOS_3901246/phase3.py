from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        

    def transpose(self) -> 'Graph2':
        """returns a new graph that is the transpose graph of self"""
        for i in range(len(self._vertices)): # Copiamos los vertices del grafo invocante en el grafo traspuesto
            transpuesto = Graph(self._vertices.keys())
        for i in self._vertices.keys(): # Nos movemos por cada vertice del grafo
            for j in self._vertices.keys():
                if self.contain_edge(i, j): # Comprobamos la direccion de la arista
                    transpuesto.add_edge(j, i) # Añadimos la arista compraba anteriormete pero en dirección contraria
        return transpuesto

    def possible(self, v, visited):
        """Comprueba si es posible ir de un vertice a otro"""
        visited[v] = True
        for v_adjacent in self._vertices[v]: # Comprueba para cada vertice
            adjacent = v_adjacent.vertex     # si hay arista que los una
            if not visited[adjacent]:
                self.possible(adjacent, visited)

    def no_conect(self, v):
        """Lista con los vertice a los que no puede llegar"""
        visited = {}  
        no_conec = []  
        for i in self._vertices: # Visitamos cada nodo
            visited[i] = False
        self.possible(v, visited) # Comprobamos si es posible llegar desde otro vertice
        for i in self._vertices: # En caso de que se hayan quedado vertices sin visitar,
            if not visited[i]:   # significa que no se ha podido llegar desde otro vertice
                no_conec.append(i) # por tanto se añade a la lista
        return no_conec

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any v to any other v
        in the graph.
        """
        for i in self._vertices:
            if len(self.no_conect(i)): # Si la lista de los no conectados tiene algún valor,
                return False           # significa que no es fuertemente conexo
        return True

    
