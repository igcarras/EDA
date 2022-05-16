from graph import AdjacentVertex
from graph import Graph


class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        if len(self._vertices) <= 1: # Se devuelve 0 si no hay más de un vértices
            return 0
        distancias = self.camino_dijkstra(start, False) # Se calculan las distancias del vértide de origen a los demás con dijkstra
        if distancias[end] == float('inf'): # Se escoge la distancia adecuada (si es "inf" es que no hay camino)
            return 0
        return distancias[end] # Esta distancia se calcula haciendo dijkstra con todos los pesos iguales a 1

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        if not self._directed: # Si el grafo no es dirigido el método no tiene sentido y se devuelve directamente el grafo original
            print("El grafo no es dirigido")
            return self
        nuevo_grafo = Graph2(self._vertices.keys()) # Se crea un nuevo grafo que será el traspuesto

        for clave in self._vertices: # En este nuevo grafo se crea una arista invertida por cada una que tenga el grafo original
            for elemento in self._vertices[clave]:
                nuevo_grafo.add_edge(elemento.vertex, clave, elemento.weight)

        return nuevo_grafo

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        if len(self._vertices) <= 1: # Primero se devuelve True si hay menos de dos vértices
            return True
        # Ahora haremos dijsktra para ver la distancia al resto de vértices desde uno arbitrario que hayamos elegido, en este caso el primero
        vector_dijkstra = self.camino_dijkstra(list(self._vertices.keys())[0], False)
        for elemento in vector_dijkstra:
            if vector_dijkstra[elemento] == float('inf'): # Si hay alguno con el que no haya camino ya sabemos que es falso
                return False
        if self._directed: 
            """ Si el grafo es dirigido tenemos que hacer una comprobación adicional, y es ver si se puede llegar al vértice
             original partiendo de los otros. Para ello volvemos hacer dijsktra, pero esta vez con el grafo traspuesto""" 
            vector_dijkstra = self.transpose().camino_dijkstra(list(self._vertices.keys())[0], False)
            for elemento in vector_dijkstra:
                if vector_dijkstra[elemento] == float('inf'):
                    return False
        return True # Si todas las distancia son un valor finito, entonces el grafo es fuertemente conexo

    def camino_dijkstra(self, nodo_inicial, ponderado=True):
        if len(self._vertices) <= 1:
            return None

        nodo_actual = nodo_inicial # Para este método se usa una lista para marcar los vértices visitados y un diccionario para
        sin_visitar = []    # guardar las distancias
        distancias = {}

        for clave in self._vertices:
            distancias[clave] = float('inf')
            sin_visitar.append(clave)
        distancias[nodo_inicial] = 0

        while len(sin_visitar) > 0: # Mientras queden elementos sin visitar se escoge uno y se actualizan las distancias al resto de vértices
            for indice, elemento in enumerate(self._vertices[nodo_actual]):
                if ponderado:
                    distancia_tentativa = distancias[nodo_actual] + self._vertices[nodo_actual][indice].weight    
                else:
                    distancia_tentativa = distancias[nodo_actual] + 1

                if distancia_tentativa < distancias[elemento.vertex]:
                    distancias[elemento.vertex] = distancia_tentativa   
            
            sin_visitar.remove(nodo_actual) # Se marca el nodo ya visitado (eliminándolo de la lista)
            if len(sin_visitar) > 0: # Se escoge a otro elemento que será el que tenga una distancia almacenada menor
                nodo_actual = sin_visitar[0]
                
            for elemento in sin_visitar:
                if distancias[elemento] < distancias[nodo_actual]:
                    nodo_actual = elemento
                    
            
        return(distancias) # Por último se devuelve el diccionario con todas las distancias



labels = ['A', 'B', 'C', 'D', 'E']
g = Graph2(labels)
# Now, we add the edges
g.add_edge('A', 'C', 12)  # A->(12)C
g.add_edge('A', 'D', 60)  # A->(60)D
g.add_edge('B', 'A', 10)  # B->(10)A
g.add_edge('C', 'B', 20)  # C->(20)B
g.add_edge('C', 'D', 32)  # C->(32)D
g.add_edge('E', 'A', 7)   # E->(7)A
