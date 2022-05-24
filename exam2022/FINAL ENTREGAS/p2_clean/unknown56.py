"""100451322 - Yago Brotón Gutiérrez"""
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        visitados = {}
        for i in self._vertices:
            visitados[i] = False
        comp = []  # Lista con las distintas componentes conexas
        for i in visitados:
            palabra = ''
            if visitados[i] is False:
                palabra += self.dfs(i, visitados)
                comp.append(palabra)
        # print(comp)
        return len(comp) == 1  # Si es conexo, solo hay una componente
    def dfs(self, v, visitados):
        """Recorrido depth-first"""
        visitados[v] = True
        # print(v, end='\t')
        for adj in self._vertices[v]:
            if visitados[adj] is False:
                self.dfs(adj, visitados)
        return v
    def is_bridge(self, v1: str, v2: str) -> bool:
        inicial = self.is_connected()
        if inicial is False:  # Si inicialmente el grafo no es conexo, no tiene aristas puente
            return False
        # Comprobamos que la unión v1 -- v2 existe
        if v1 not in self._vertices[v2]:
            return False
        if v2 not in self._vertices[v1]:
            return False
        # Borramos la arista, y comprobamos si el grafo resultante sigue siendo conexo
        self._vertices[v1].remove(v2)
        self._vertices[v2].remove(v1)
        borrado = self.is_connected()
        # Como hemos borrado la conexión, hay que volver a añadirla
        self.add_edge(v1, v2)
        return borrado == False  # Si es falso, primero era conexo, y al borrar ya no lo era
