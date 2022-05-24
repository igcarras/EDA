    def quitar_arista(self, inicio: object, final: object):
        if inicio not in self._vertices.keys():
            return
        if final not in self._vertices.keys():
            return
        for adj1 in self._vertices[inicio]:
            if adj1 == final:
                self._vertices[inicio].remove(adj1)
        for adj2 in self._vertices[final]:
            if adj2 == inicio:
                self._vertices[final].remove(adj2)
    def existe_arista(self, inicio: object, final: object) -> int:
        if inicio not in self._vertices.keys():
            return None
        if final not in self._vertices.keys():
            return None
        for adj in self._vertices[inicio]:
            if adj == final:
                return True
        return None
    def is_connected(self) -> bool:
        for vertice_inicial in self._vertices:
            adj = [vertice_inicial, None]
            visitados = [vertice_inicial]
            fin_bucle = False
            while len(adj) != None and fin_bucle == False:
                vertice = adj.pop(0)
                if vertice == None:
                    adj.append(None)
                    if adj[0] == None:
                        fin_bucle = True
                else:
                    for adj2 in self._vertices[vertice]:
                        if adj2 not in visitados:
                            visitados.append(adj2)
                            adj.append(adj2)
            if len(visitados) < len(self._vertices):
                return False
        return True
    def is_bridge(self, v1: str, v2: str) -> bool:
        if self.existe_arista(v1,v2):
            if self.check_vertex(v1) and self.check_vertex(v2):
                self.quitar_arista(v1,v2)
                if self.is_connected() == True:
                    self.add_edge(v1, v2)
                    return False
                else:
                    self.add_edge(v1, v2)
                    return True
            else:
                return False
        else:
            return False
