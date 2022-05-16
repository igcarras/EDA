# Daniel Sánchez de la Cruz. NIA: 100475344
# Simón Benzaquén Aserraf. NIA: 100475237

from graph import AdjacentVertex
from graph import Graph


class Graph2(Graph):
    # Algoritmo basado en BFS. Complejidad O(V + E)
    def min_number_edges(self, start: str, end: str) -> int:
        # La distancia de un vértice a él mismo es 0
        if start == end:
            return 0

        # Inicializamos los vértices a no visitados
        visited_vertex = {}
        for vertex in self._vertices:
            visited_vertex[vertex] = False

        # Creamos una cola para BFS y añadimos el vértice start
        queue = [] 
        visited_vertex[start] = True
        queue.append((start, 0))
        
        # Recorremos el grafo mediante BFS
        while queue:
            # s es una tupla (vértice, distancia a start)
            s = queue.pop(0) 

            for adj in self._vertices[s[0]]:
                if adj.vertex == end:
                        return s[1] + 1

                if not visited_vertex[adj.vertex]:
                    queue.append((adj.vertex, s[1] + 1))
                    visited_vertex[adj.vertex] = True

                    
        # No hay ningún camino desde start a end
        return 0
   
    # Complejidad O(V + E)
    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        # Copiamos el grafo, transponiéndolo en el proceso
        transposed = Graph2(self._vertices.keys(), self._directed)
        for v in self._vertices:
            for u in self._vertices[v]:
                transposed._vertices[u.vertex].append(AdjacentVertex(v, u.weight))

        return transposed

    # Algoritmo basado en DFS. Complejidad O(V + E)
    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        # Inicializamos diccionario de visitados a False
        visited_vertex = {}
        for vertex in self._vertices:
            visited_vertex[vertex] = False

        # Seleccionamos un único vértice del grafo y lo recorremos con DFS
        origin = list(visited_vertex.keys())[0]
        self._dfs(origin, visited_vertex)

        # Si hay algún vértice no visitado después de hacer DFS, el grafo no es fuertemente conexo,
        # pues no hay ningún camino desde el vértice origin hasta el vértice no visitado
        for vertex in visited_vertex:
            if visited_vertex[vertex] == False:
                return False
        
        # Si el grafo no es dirigido, no necesitamos hacer otro recorrido por DFS, el grafo es fuertemente conexo
        if not self._directed:
            return True
        
        # Trasponemos el grafo
        transposed = self.transpose()

        # Inicializamos diccionario de visitados a False de nuevo
        visited_vertex = {}
        for vertex in transposed._vertices:
            visited_vertex[vertex] = False

        # Recorremos el grafo traspuesto desde el mismo vértice que antes
        transposed._dfs(origin, visited_vertex)

        # Si hay algún vértice no visitado después de hacer DFS, el grafo no es fuertemente conexo,
        # pues no hay ningún camino desde el vértice no visitado hasta el vértice origin (en el grafo original)
        for vertex in visited_vertex:
            if visited_vertex[vertex] == False:
                return False
        
        # Si los dos recorridos por DFS son "satisfactorios", el grafo es fuertemente conexo
        return True
    
    # Implementación de recorrido DFS
    def _dfs(self, vertex: object, visited_vertex: dict) -> None:
        visited_vertex[vertex] = True
        for adj in self._vertices[vertex]:
            if not visited_vertex[adj.vertex]:
                self._dfs(adj.vertex, visited_vertex)