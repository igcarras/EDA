from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    # Método "min_number_edges". Devuelve cuantas aristas conforman el camino mínimo entre dos vértices ("start" y
    # "end"). Devolverá "0" en el caso en el cual no exista dicho camino.
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        # Creamos un diccionario cuyas claves serán los vértices y, los contenidos, "True" (si hemos pasado por dicho
        # vértice) o "False" (si todavia no hemos pasado por él).
        vertices_visitados = {}
        # Creamos dos listas de python. Una auxiliar y otra que devolverá el valor final que estamos buscando. Esta
        # última lista contiene los caminos mínimos hacia todos los vértices, pero realmente nos interesa el del
        # vértice "end".
        aristas_minimas = []
        lista_aux = []
        # En este bucle inicializamos los valores del diccionario y el de las listas:
        # DICCIONARIO: Todos los valores a "False".
        # ARISTAS_MINIMAS: Todos los valores a "0". Si no hay un camino al vértice que estamos buscando, como el valor
        #                  no se actualiza, devolveremos "0" tal y como se pide.
        # LISTA_AUX: Guardamos en ella los vértices. Nos servirá a la hora de corresponder las posiciones de la lista
        #            "aristas_minimas" con dicho vértice (por ejemplo lista_aux[0] = 'A', y gracias a este dato podremos
        #            saber que aristas_minimas[0] corresponde al valor del camino mínimo hasta 'A'.
        for vertice in self._vertices.keys():
            vertices_visitados[vertice] = False
            aristas_minimas.append(0)
            lista_aux.append(vertice)
        # Ejecutamos el método auxiliar "_min_number_edges", que se encarga de actualizar la lista "aristas_minimas".
        self._min_number_edges(start, vertices_visitados, aristas_minimas, lista_aux)
        # Devolvemos el valor correspondiente al camino mínimo que empieza en "start" y acaba en "end".
        return aristas_minimas[lista_aux.index(end)]

    # Método auxiliar "_min_number_edges". Recibe como parámetros el vértice "start", el diccionario de vértices
    # visitados y las dos listas del método principal.
    def _min_number_edges(self, start: object, vertices_visitados: dict, aristas_minimas: list,
                          lista_aux: list) -> None:
        queue = []
        vertices_visitados[start] = True
        queue.append(start)
        # Mientras haya vértices encolados, querrá decir que no hemos terminado de recorrer el grafo.
        while queue:
            s = queue.pop(0)
            for adyacente in self._vertices[s]:
                if not vertices_visitados[adyacente.vertex]:
                    # Si el vértice no ha sido visitado, actualizamos el valor de las aristas mínimas para llegar a
                    # dicho vértice en la correspondiente lista. Lo que hacemos es sumar 1 a las aristas que había
                    # previamente en el vértice adyacente del cual partimos.
                    # Cabe destacar la suma importancia de la lista auxiliar, que gracias a el método index de las
                    # listas de python, podemos saber a ciencia cierta a qué posición de aristas_minimas debemos
                    # acceder para actualizar el valor del vértice.
                    aristas_minimas[lista_aux.index(adyacente.vertex)] = \
                        aristas_minimas[lista_aux.index(s)] + 1
                    queue.append(adyacente.vertex)
                    vertices_visitados[adyacente.vertex] = True

    # Método "transpose". Devuelve y sustituye el grafo original por un grafo transpuesto, que cambia la orientación
    # de los punteros en caso de ser un grafo dirigido y no hace nada si no lo es.
    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        # Como hemos dicho, si el grafo no es dirigido no hace falta hacer ninguna modificación, ya que el grafo
        # transpuesto coincidirá con el original.
        if not self._directed:
            grafo = Graph2(self._vertices.keys(), False)
            self._vertices = grafo._vertices
            return grafo
        grafo = Graph2(self._vertices.keys(), True)
        # Creamos un nuevo diccionario que tendrá como claves los vértices del grafo. Dichas claves contendrán listas
        # que almacenarán listas de python con los vértices adyacentes al mismo. Las listas se inicializan vacías.
        grafo._vertices = {}
        for vertice in self._vertices.keys():
            grafo._vertices[vertice] = []
        for vertice in self._vertices.keys():
            # Para construir el grafo transpuesto se ha de considerar los siguiente: en vez de añadir a "vértice" su
            # vértice adyacente, es a dicho vértice adyacente al cual se le añade "vértice". Si repetimos esto con
            # cada uno de los vértices, se creará el grafo transpuesto deseado.
            for adyacente in self._vertices[vertice]:
                grafo._vertices[adyacente.vertex].append(AdjacentVertex(vertice, 1))
        # Por último, decimos que el diccionario "self._vertices" es el nuevo diccionario manufacturado
        # "grafo._vertices".
        self._vertices = grafo._vertices
        return grafo

    # Método "is_strongly_connected", que dice si un grafo -sea dirigido o no- está fuertemente conectado.
    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        for vertice in self._vertices.keys():
            # Definimos una variable "camino" para cada vértice del grafo. Dicha variable vendrá dada por los métodos
            # auxiliares "_is_strongly_connected_1" y "_is_strongly_connected_2", que se basan en el recorrido de un
            # grafo en profundidad.
            camino = self._is_strongly_connected_1(vertice)
            for adyacente in self._vertices.keys():
                if vertice != adyacente:
                    # Si hay un único vértice que no aparece en el array "camino", quiere decir que no se puede trazar
                    # un camino desde "vértice" hasta él, con lo cual ya no es un grafo fuertemente conexo.
                    if adyacente not in camino:
                        return False
        # Sino, devolvemos que sí, en efecto se trata de un grafo fuertemente conexo.
        return True

    # Método "_is_strongly_connected_1", que está basado en el recorrido de un grafo en profundidad y que depende de
    # otro método auxiliar llamado "_is_strongly_connected_2".
    def _is_strongly_connected_1(self, vertice) -> list:
        vertices_visitados = {}
        for vertex in self._vertices.keys():
            vertices_visitados[vertex] = False
        # La variable "camino" se trata de nada más y nada menos que una lista que se rellenará con los vértices a los
        # que se pueden llegar a partir de "vértice". Si en "camino" no están todos los vértices, querrá decir que el
        # grafo no es fuertemente conexo.
        camino = []
        # Gracias al método "_is_strongly_connected_2" se rellena dicha lista.
        self._is_strongly_connected_2(vertice, vertices_visitados, camino)
        return camino

    # Método "_is_strongly_connected_2", que va añadiendo a la lista "camino" cada vértice adyacente del vértice
    # "vértice" gracias a consecutivas llamadas recursivas.
    def _is_strongly_connected_2(self, vertice: object, vertices_visitados: dict, camino: list) -> None:
        vertices_visitados[vertice] = True
        camino.append(vertice)
        for adyacente in self._vertices[vertice]:
            if not vertices_visitados[adyacente.vertex]:
                self._is_strongly_connected_2(adyacente.vertex, vertices_visitados, camino)
