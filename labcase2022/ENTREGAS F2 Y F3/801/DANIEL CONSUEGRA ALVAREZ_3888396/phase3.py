from graph import AdjacentVertex
from graph import Graph
"""Author: Daniel Consuegra Álvarez"""
class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
    # para obtener el camino con menor numeros de aristas haremos un recorrido bfs "por niveles" entre dos vertices
    #con este recorrido nos aseguramos que el camino sea minimo
        queue =[]  # lista de phyton con comportamiento de TAD cola
        #diccionarios
        #visitados
        visited={}   # para no repetir el recorrido por vertices ya visitados
        for v in self._vertices.keys():
            visited[v]=False
        #distancias
        distancias={}  # un diccionario para guardar las distancias de cada nivel con respecto al vertice start
        for d in self._vertices.keys():
            distancias[d]=0

        #mark the source vertex as visited
        visited[start] = True
        # añadimos el vertice incial a la cola
        queue.append(start)
        while queue:
            # Dequeue y guardamos el valor
            s= queue.pop(0)
            # obtenemos sus adyacentes
            # Si un adj no ha sido visitado se añade a la cola y se marca como visitado
            for adj in self._vertices[s]:
                if visited[adj.vertex] == False:
                    queue.append(adj.vertex)
                    distancias[adj.vertex]=distancias[s]+1  # cambiamos el valor de la distancia asignada a este vertice por el valor del anterior +1
                    visited[adj.vertex]=True
                if adj.vertex==end:  # cuando el vertice adj es el end devolvemos la distancia guardada en el dicc con key end
                    return distancias[end]
        return 0

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        gtranspose=Graph2(self._vertices.keys())  # creamos el objeto de la clase Graph2 que sera el traspuesto del grafo invocante
        # Para cada vertice del grafo invertimos los parametros start y end del metodo add_edge para invertir la direccion del grafo
        # (el grafo traspuesto de un grafo no drigido es el mismo grafo)
        for v in self._vertices.keys():
            for adj in self._vertices[v]:
                gtranspose.add_edge(adj.vertex,v)
        return gtranspose

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        visited={} # creamos un diccionario para los vertices visitados y que pasaran por parametro al metodo dfs recursivo
        Vertices=[]  # lista que contiene los vertices de las claves del diccionario del grafo para así poder iterar con sus posiciones
        for i in self._vertices.keys():
            Vertices.append(i)
        # comprobamos primero si en el grafo original desde un vertice cualquiera se puede llegar a cualquier otro
        for v in self._vertices.keys():
            visited[v]=False
        self._dfs(Vertices[0],visited) # en este caso con el recorrido dfs del primer vertice, podemos comprobar en el diccionario de visitados
        for v in visited.keys():       # si despues del recorrido queda algun vetice sin visitar(eso significa que no hay camino a ese vertice
            if visited[v]==False:      #luego no seria un grafo conexo
                return False
        for v in self._vertices.keys(): # volvemos a poner el diccionario de visitados a False y hacemos otro dfs con el grafo traspuesto
            visited[v]=False
        gtranspose = self.transpose()
        gtranspose._dfs(Vertices[0],visited) # si en el grafo traspuesto hay algun vertice en false significa que hay algun camino desde cualquier vertice
        for v in visited.keys():             # que no llega hasta nuestro vertice v (luego no seria conexo)
            if visited[v]==False:
                return False
        return True    # si se puede llegar desde el vertice v a cualquier vertice y desde cualquier vertice a el vertice v
                       # significa que el grafo es fuertemente conexo
    def _dfs(self,v,visited): # método recursivo dfs
        visited[v]=True
        for adj in self._vertices[v]:
            if visited[adj.vertex] == False:
                self._dfs(adj.vertex,visited)

""""#Otra manera de hacer el metodo is_strongly_conected con matriz de caminos minimos entre vertices
        # lista de  vertices
        Vertices=[]
        for v in self._vertices.keys():
            Vertices.append(v)
        Matriz=[] #Matriz de caminos del grafo
        N=len(Vertices)
        #Crear la matriz
        for i in range(N):
            Matriz.append([])
            for j in range(N):
                Matriz[i].append(self.min_number_edges(Vertices[i],Vertices[j]))
        # printear la Matriz
        for i in range(N):
            print(Matriz[i])
        #comprobar si hay algun camino nulo distinto de la diagonal principal
        for i in range(N):
            for j in range(N):
                if i!=j:
                    if Matriz[i][j]==0:
                        return False
        return True"""





