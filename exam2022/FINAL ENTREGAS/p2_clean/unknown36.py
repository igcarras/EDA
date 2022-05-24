import math
    def is_connected(self) -> bool:
        if self == None:
            # aqui comprueba que el grafo existe o no
            print('El grafo no existe')
            return False
        else:
            for v in self._vertices.keys():
                for n in self._vertices.keys():
                    if self.are_connected(v, n) == True:
                        return True
                    return False
            return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        vertice1 = self.find(v1)
        vertice2 = self.find(v2)
        if vertice1 != -1 and vertice2 != -1:
            if not self.is_connected:
                pass
            # aqui comprueba que esta conectado o no
            # y realiza un bucle u otro
            else:
                v1 = None
                if self.are_connected():
                    return True
                return False
            return True
        return False
#FUNCIONES QUE NOS AYUDAN A OBTENER LAS PRINCIPALES
    def find(self, v):
        # Busca el v que nos piden mediante
        for i in self._vertices.keys():
            if self._vertices[i] != v:
                continue
            return i
        return -1
    def are_connected(self, v1, v2):
        #comprueba que estan conectados dos vertices
        vertice1 = self.find(v1)
        vertice2 = self.find(v2)
        #como podemos ver en la funcion anterior, podemos ver que si nos devuelve -1 esta mal
        # y ese vertice no esta por lo tanto a partir de ahi se desarrolla el codig
        if vertice1 != -1:
            if vertice2 == -1:
                return False
            for adj in self._vertices[vertice1]:
                if adj.vertex == vertice2:
                    return True
            return False
        return False
