    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        for v in self._vertices:
            lista_visitados = [v]
            unidos = [v]
            while len(lista_visitados) != 0:
                primero = lista_visitados.pop(0)
                for adj in self._vertices[primero]:
                    if adj not in unidos:
                        lista_visitados.append(adj)
                        unidos.append(adj)
            if len(unidos) < len(self._vertices):
                return False
        return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        if v1 not in self._vertices:
            return False
        if v2 not in self._vertices or v2 not in self._vertices[v1]:
            return False
        else:
            for adj in self._vertices[v1]: #vemos todos los vértices adyacentes de v1
                if adj == v2: #en el caso de que sea v2
                    #quitamos la arista {v1,v2}
                    self._vertices[v1].remove(v2)
                    self._vertices[v2].remove(v1)
                    #comprobamos si es conexo o no
                    is_connected = self.is_connected()
                    #volvemos a añadir la arista
                    self._vertices[v1].append(v2)
                    self._vertices[v2].append(v1)
                    #si no es conexo significa que la arista si era una arista puente
                    if is_connected == False:
                        return True
                return False
