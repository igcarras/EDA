import sys

from graph import AdjacentVertex
from graph import Graph


class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """Algoritmo parecido al de Dijkstra pero en grafos con weight = 1"""
        # Si comparten arista start y end return 1
        if self.contain_edge(start, end) != 0:
            return 1
        # Si son la misma return 0
        elif start == end:
            return 0
        # Si el grafo es dirigido y de su inicio no salen aristas
        elif self._directed and len(self._vertices[start]) == 0:
            return 0
        else:
            visitado = {}  # Para cada vértice si está visitado
            distacias = {}  # Para cada vértice se guarda la distacia mínima hasta start

            for v in self._vertices.keys():
                visitado[v] = False
                distacias[v] = sys.maxsize

            # Distancia de start a start es 0
            distacias[start] = 0

            # Hasta q se visite end
            while not visitado[end]:
                # Método para elegir el vértice no elegido con menor distancia hasta start
                u = self.min_distance(distacias, visitado)

                # Marcar como visitado
                visitado[u] = True

                # Vértices adyacentes a u
                for adj in self._vertices[u]:
                    i = adj.vertex
                    w = adj.weight
                    # Actualizar si es necesario la distancia de los vértices adyacentes no visitados
                    if not visitado[i] and distacias[i] > distacias[u] + w:
                        # Actualizar distancia
                        distacias[i] = distacias[u] + w
            return distacias[end]

    def min_distance(self, distances: dict, visited: dict) -> int:
        #Devuelve el vértice no visitado cuya distancia al inicio es menor
        min_distance = sys.maxsize
        min_vertex = None

        for vertex in self._vertices.keys():
            if distances[vertex] <= min_distance and not visited[vertex]:
                min_distance = distances[vertex]  # update the new smallest
                min_vertex = vertex  # update the index of the smallest

        return min_vertex

    def transpose(self) -> 'Graph2':
        vertices = []
        for a in self._vertices.keys():
            vertices.append(a)
        nuevoGrafo = Graph2(vertices, self._directed)
        for a in self._vertices.keys():
            for adj in self._vertices[a]:
                b = adj.vertex
                c = adj.weight
                adyacente = AdjacentVertex(a, c)
                if adyacente not in nuevoGrafo._vertices[b]:
                    nuevoGrafo.add_edge(b, a, c)

        return nuevoGrafo

    def is_strongly_connected(self) -> bool:
        resultado = True
        for v in self._vertices.keys():
            if not resultado:
                return resultado
            resultado = resultado and self.connected(v)
        return resultado

    def connected(self, inicio):
        listaInicial = []
        listaFinal = []
        visitado = {}
        for a in self._vertices.keys():
            visitado[a] = False
            listaInicial.append(a)

        visitado[inicio] = True
        listaFinal.append(inicio)
        self.visitarTodosAdy(inicio, visitado, listaFinal)

        return len(listaFinal) == len(listaInicial)

    def visitarTodosAdy(self, vertice, visitado, listaFinal: list):
        for adj in self._vertices[vertice]:
            if not visitado[adj.vertex]:
                visitado[adj.vertex] = True
                listaFinal.append(adj.vertex)
                self.visitarTodosAdy(adj.vertex, visitado, listaFinal)

    '''def is_strongly_connected2(self) -> bool:
        for i in self._vertices:
            visited = {}
            for v1 in self._vertices:
                visited[v1] = False
            visited[i] = True
            queue = [i]
            while len(queue) > 0:
                u = queue.pop(0)
                for adj in self._vertices[u]:
                    r = adj.vertex
                    if visited[r] == False:
                        queue.append(r)
                        visited[r] = True
            for v1 in self._vertices:
                if visited[v1] == False:
                    return False
        return True'''