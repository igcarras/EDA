    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        # Usaremos bfs para intentar recorrer to do el grafo a partir de un solo vértice y ver si es conexo
        visitados = {}
        for v in self._vertices.keys():
            visitados[v] = False
        visitados = self._bfs(visitados, list(self._vertices.keys())[0]) # Con el diccionario de visitados podemos comprobar
        for e in visitados.keys(): #  si hay algun vértice que sea inaccesible
            if not visitados[e]:
                return False # Si hay alguno no visitado devolveremos False
        return True # Si se visitan todos se devuelve True
        # Al ser un grafo no dirigido  solo es necesario hacer una comprobacion, ya que las aristas tienen ambos sentidos
    def _bfs(self, visitados, v):
        cola = []
        cola.append(v) # Se añade a la cola el vertice inicial y se marca como visitado
        visitados[v] = True
        while cola:
            s = cola.pop(0)
            for ady in self._vertices[s]: # Se hace los mismo con cada vértice adyacente a el actual y asi sucesivamente,
                if not visitados[ady]:    # hasta que se agote la cola o no queden más vertices sin visitar
                    cola.append(ady)
                    visitados[ady] = True
        return visitados
    def is_bridge(self, v1: str, v2: str) -> bool:
        if not self.check_vertex(v1) or not self.check_vertex(v2): # Se comprueba que existen ambos vértices
            return False
        if v2 not in self._vertices[v1]: # Se comprueba que existe la arista
            return False
        self._vertices[v1].remove(v2) # Se elimina la arista
        self._vertices[v2].remove(v1)
        respuesta = not self.is_connected() #Se mira si es conexo el grafo modificado. Si lo es, la arista no era puente y viceversa
        self.add_edge(v1, v2) # Se vuelve a colocar la arista eliminada
        return (respuesta)
