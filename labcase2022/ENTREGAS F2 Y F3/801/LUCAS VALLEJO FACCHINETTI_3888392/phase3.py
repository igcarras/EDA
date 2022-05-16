from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        camino = self._buscador(start, end, 0)
        if camino:
            return camino
        else:
            return 0
    def _buscador(self, vertice:str, final:str, cuenta:int, camino_minimo:int = None):
        if vertice != final:   #miramos si el vertice inicial no es el mismo que el final
            if camino_minimo == None or cuenta +1 <= camino_minimo:
                for n in self._vertices[vertice]:   #buscamos todos los vertices del grafo con v
                    if camino_minimo == None or cuenta +1<=camino_minimo:
                        nuevo_camino = self._buscador(n.vertex, final, cuenta+1, camino_minimo) #sumamos uno a la cuenta porque todavia no hemos llegado al final
                        if camino_minimo == None or nuevo_camino < camino_minimo:    #si el nuevo camino es mas corto que el camino minimo, este se cambia al nuevo camino minimo
                            camino_minimo = nuevo_camino
            return camino_minimo    #hasta que no llegamos al final seguimos con el return de camino_minimo
        else:
            return cuenta       #nos devuelve el resultado que estamos buscando


    def transpose(self) -> 'Graph2':
        traspuesto = Graph2(self._vertices.keys(), self._directed)    #crea el segundo grafo

        for x, vertices in self._vertices.items():       # x es la clave y adjuntos son los vertices x vertice adjuntos aristas coge adjunto.vertex
            for vertice in vertices:        #selecciona cada verice dentro del diccionario de vertices
                peso = vertice.weight     #coge el valor del vertice
                nombre = vertice.vertex  # coge el nombre del vertice que queremos
                traspuesto._vertices[nombre].append(AdjacentVertex(x, peso))     #da valores al nuevo grafo

        return traspuesto

    def is_strongly_connected(self) -> bool:    #la funcion devuleve un true or false
        for primer_vert in self._vertices:     #buscamos en todos los vertices del grafo
            vert_visitados = [primer_vert]
            adjuntos_vert = [primer_vert, None]      #establecemos cuales son los adjuntos y los vertices visitados
            while len(adjuntos_vert):     #miramos si el diccionario de adjuntos esta lleno
                x = adjuntos_vert.pop(0)
                if x != None:
                    for adjuntos in self._vertices[x]:       #en caso de que este lleno
                        if adjuntos.vertex not in vert_visitados:
                            adjuntos_vert.append(adjuntos.vertex)
                            vert_visitados.append(adjuntos.vertex)


            if len(self._vertices) > len(vert_visitados):     #comparamos si es el mismo len entre los visitados y los que de verdad tenemos
                return False
        return True

                

