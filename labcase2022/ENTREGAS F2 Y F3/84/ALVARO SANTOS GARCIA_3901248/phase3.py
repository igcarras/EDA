from graph import Graph


class Graph2(Graph):

    def min_number_edges(self, start: str, end: str) -> int:
        visited = {}
        lista = []
        aux = []
        # ponemos todos los vertices como no visitados
        for v in self._vertices.keys():
            visited[v] = False
        arista = 0
        visited[start] = True
        lista.append(start)
        # mientras que no hayamos recorrido todos el grafo o hayamos encontrado el vértice end se sigue ejecutando
        # Recorremos el grafo mediante recorrido por amplitud
        while len(lista) != 0 and end not in lista:
            a = lista.pop(0)
            for adj in self._vertices[a]:
                if not visited[adj.vertex]:
                    aux.append(adj.vertex)
                    visited[adj.vertex] = True
            # Una vez que se haya recorrido todos los vértices de un mismo nivel se suma uno a la arista
            # y se pasa al siguiente nivel
            if len(lista) == 0:
                lista = aux.copy()
                aux.clear()
                arista += 1

        # Si end está en la lista quiere decir que hemos encontrado un camino
        if end in lista:
            return arista
        # Si end no esta quiere decir que no existe camino entre start y end
        else:
            return 0

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        g = Graph2(self._vertices.keys(), self._directed)
        # Si el grafo es dirigido modificamos el nuevo grafo
        if self._directed:
            # Con ayuda de dos bucles invertimos la dirección de las aristas
            for v in self._vertices:
                for adj in self._vertices[v]:
                    g.add_edge(adj.vertex, v, adj.weight)
        # Si el grafo no es dirigido el nuevo grafo es el mismo
        else:
            g._vertices = self._vertices

        return g

    def is_strongly_connected(self) -> bool:
        visited = {}
        # ponemos todos los vertices como no visitados
        for v1 in self._vertices:
            visited[v1] = False
        aux = visited.copy()
        # Bucle con el que vamos a hacer que el recorrido empiece desde todos los vertices posibles
        for v in self._vertices.keys():
            # Reseteamos el diccionario visited
            visited = aux.copy()
            # Llamamos a una función recursiva para recorrer el grafo
            self._is_strongly_connected(v, visited)
            # Si hay falso en visited quiere decir que no es fuertemente conexo
            if False in visited.values():
                return False
        return True

    def _is_strongly_connected(self, vertex: str, visited: dict) -> None:
        visited[vertex] = True
        # Recorremos el grafo mediante un recorrido en profundidad
        for adj in self._vertices[vertex]:
            # adj is an object of AdjacentVertex
            adj_vertex = adj.vertex
            if not visited[adj_vertex]:
                self._is_strongly_connected(adj_vertex, visited)
