#Álvaro Moreno Martín y Luis González Pérez, Grupo 801

from graph import AdjacentVertex
from graph import Graph
import sys

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        
        #Método iterativo Breadth-First Search
        #Creamos variables auxiiares
        visitados = {}
        for v in self._vertices:
            visitados[v] = False
        visitados[start] = True
        adjuntos = [start, None]
        contador = 0
        #Búsqueda BFS: Por niveles, se miran los nodos adyacentes y luego los adyacentes a estos
        while len(adjuntos) != None:
            #Se comprueba el siguiente elemento de la cola, si es el final se termina
            v = adjuntos.pop(0)
            if v == end:
                return contador
            #Se marcan los niveles con Nones, y aumenta el contador
            elif v == None:
                contador += 1
                adjuntos.append(None)
                #Si se ha explorado todo sin encontrar el final
                if adjuntos[0] == None: 
                    return 0
            #Se añaden los nodos adyacentes si no se han recorrido
            else:
                for adj in self._vertices[v]:
                    if visitados[adj.vertex] == False:
                        visitados[adj.vertex] = True
                        adjuntos.append(adj.vertex)

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        grafot = Graph2(list(self._vertices.keys()), self._directed)
        #Si el grafo no está dirigido, es su mismo traspuesto
        if not self._directed:
            grafot._vertices = self._vertices.copy()
        else:
            #Creamos vértices en el sentido opuesto a los existentes
            for vertice in self._vertices:
                for arista in self._vertices[vertice]:
                    grafot._vertices[arista.vertex].append(AdjacentVertex(vertice, arista.weight))
        return grafot

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        #Algoritmo de Kosaraju simplificado, tipo DFS
        conexo = True
        
        if len(self._vertices)>0:
            #Si el grafo no es dirigido, basta con comprobar desde un nodo cualquiera
            visitados = []
            self._buscar(list(self._vertices.keys())[0], visitados)
            if len(visitados) < len(self._vertices):
                conexo = False
                
            #Si es dirigido, comprobamos que se puede acceder a todos los nodos también en el transpuesto
            if self._directed:
                grafot = self.transpose()
                visitados = []
                grafot._buscar(list(grafot._vertices.keys())[0], visitados)
                if len(visitados) < len(grafot._vertices):
                    conexo = False
        
        return conexo
    
    def _buscar(self, vertice : str, visitados : list):
        #Accedemos a cada nodo y si aun no se ha visitado, lo añadimos
        for arista in self._vertices[vertice]:
            if arista.vertex not in visitados:
                visitados.append(arista.vertex)
                #Seguimos buscando por este camino
                self._buscar(arista.vertex, visitados)