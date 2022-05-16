'''
FASE 3
Nombre1: Iván Merchán Ruiz
NIA1:100451135
Nombre2: Rubén Zorrilla
NIA2:100451173
'''

from graph import AdjacentVertex
from graph import Graph
import math

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """devuelve el número mínimo de aristas de 'start' a 'end'"""
        if start in self._vertices.keys():
            if end in self._vertices.keys():
                distancia, previa = self.dijkstra(start)
                if distancia[end] != math.inf:
                    resultado = [end]
                    prev = previa[end]
                    while prev is not None:
                        resultado.insert(0, prev)
                        prev = previa[prev]
                    return distancia[end]
                return 0
            print("end no existe")
            return -1
        print("start no existe")
        return -1
    # La complejidad de este método es O(n^2) ya que posee bucles anidados (2).
    # El mejor caso se dará si start o end no existen, y el peor si se trata de un grafo muy extenso.

    def transpose(self) -> 'Graph2':
        """devuelve el grafo traspuesto del original de entrada"""
        # creamos un grafo nuevo (traspuesto) y guardamos en el los vértices del grafo original
        for i in range(len(self._vertices)):
            traspuesto = Graph(vertices=self._vertices.keys())

        # ahora reorganizamos las aristas y lo devolvemos
        for v in self._vertices.keys():
            for j in self._vertices.keys():
                if self.contain_edge(v, j):
                    traspuesto.add_edge(j, v)
        return traspuesto
    # La complejidad de este método es O(n + n^2) ya que posee bucles anidados (2) y otro suelto a parte.
    # El mejor caso se dará si el grafo de entrada no existe, y el peor si este es muy grande.

    def is_strongly_connected(self) -> bool:
        """Esta función verifica si el grafo está fuertemente conectado.
         Un grafo dirigido es fuertemente conexo cuando para cualquier
         par de vértices u y v, siempre hay un camino de u a v.
         Si el grafo no es dirigido, la función devuelve True si el grafo es
         conexo, es decir, hay un camino desde cualquier vértice a cualquier otro.
        """
        if self != None:
            for v in self._vertices.keys():
                for n in self._vertices.keys():
                    if self.areConnected(v,n) != True:
                        return False
            return True
        else:
            print('El grafo no existe')
            return False
    # La complejidad de este método es O(2n + n^2) ya que posee bucles anidados (2) y otros dos por otra parte.
    # El mejor caso se dará cuando no exista el grafo o alguno de los vértices, y el peor será si el grafo es de
    # gran tamaño.

    '''Funciones AUXILIARES'''

    def dijkstra(self, origin: object) -> None:
        '''Devuelve una lista con las distancias y una lista con los vértices anteriores a uno dado
         en el camino mínimo'''
        visited = {}
        previous = {}
        distances = {}

        # crea los diccionarios
        for v in self._vertices.keys():
            visited[v] = False
            previous[v] = None
            distances[v] = math.inf

        # Distancia al origen, como inicia desde origen por eso es 0
        distances[origin] = 0

        for _ in range(len(self._vertices)):
            # elige el vertice no visitado de menor distanca
            u = self.distancia_minima(distances, visited)
            visited[u] = True
            # elige los adyacentes de u
            for adj in self._vertices[u]:
                i = adj.vertex
                w = 1
                # comprobamos si es menor distancia
                if not visited[i] \
                        and distances[i] > distances[u] + w:
                    # actualizamos la distancia
                    distances[i] = distances[u] + w
                    previous[i] = u

        # imprimos la solucion
        self.solution(distances, previous, origin)

        return distances, previous

    def distancia_minima(self, distancia: dict, visited: dict) -> int:
        ''' La función devuelve el menor de los vértices no visitados'''
        # variables necesarias para recorrer el grafo
        min_d = math.inf
        min_v = None

        for v in self._vertices.keys():
            if distancia[v] <= min_d \
                    and not visited[v]:
                min_d = distancia[v]  # actualiza el valor min
                min_v = v  # actualiza el index del minimo

        return min_v

    def solution(self, distances: dict, previous: dict, origin: object):
        ''' Imprime el camino mínimo entre dos vértices existentes'''
        for i in self._vertices.keys():
            if distances[i] == math.inf:
                print("There is not path from ", origin, ' to ', i)
            else:
                # creamos la variable 'minimun path' para guardar los vértices
                minimum_path = []
                prev = previous[i]
                while prev is not None:
                    minimum_path.insert(0, prev)
                    prev = previous[prev]
                # añadimos el ultimo vértice
                minimum_path.append(i)

                # hacemos print a minimum_path y distances[i]
                print(origin, 'to', i, ":", minimum_path, distances[i])

    def _getIndice(self,vertice):
        ''' Esta función comprueba si un vértice existe en el grafo'''
        for index in self._vertices.keys():
            if self._vertices[index]==vertice:
                return index
        return -1

    def areConnected(self,vertice1,vertice2):
        ''' Determina si dos vértices existentes están conectados'''
        index1=self._getIndice(vertice1)
        index2=self._getIndice(vertice2)
        if index1==-1:
            print(vertice1,' not found!')
            return False
        if index2==-1:
            print(vertice2,' not found!!')
            return False
        for adj in self._vertices[index1]:
            if adj.vertex==index2:
                return adj.weight
        return True