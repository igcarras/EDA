from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    #
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        paths=[]
        self._min_number_edges(start,end,[start],paths)
        if  len(paths)==0:
            return 0
        else:
            #for para encontrar el menor de los caminos
            min=paths[0]
            for i in range(len(paths)-1):
                if paths[i+1]<min:
                    min=paths[i+1]
            return min

    #Método recursivo de min_number_edges
    def _min_number_edges(self,node:str,end:str,path:list,allpaths:list):
        #Recorremos los nodos adyacentes a node
        for i in self._vertices[node]:
            #Si uno de ellos es el fin del camino, añadimos la longitud del camino a allpaths
            if i.vertex == end:
                aux=list(path)
                aux.append(i.vertex)
                allpaths.append(len(aux)-1)
            elif i.vertex not in path:
                #Para no generar bucles solo llamamos recorremos nodos que no estén ya en path
                aux=list(path)
                aux.append(i.vertex)
                if len(allpaths)>0:
                #Si ya hemos encontrado un camino, si el camino actual es mayor que el que ya hemos encontrado, dejamos de recorrer
                    if len(aux)<allpaths[0]:
                        self._min_number_edges(i.vertex,end,aux,allpaths)
                else:self._min_number_edges(i.vertex,end,aux,allpaths)

    def transpose(self) -> 'Graph2':
        allvertices=list(self._vertices.keys())
        new_graph=Graph2(allvertices,self._directed)
        if self._directed:
            for i in allvertices:
                for n in self._vertices[i]:
                #Vamos invirtiendo las aristas de forma que si a está unido con b el grafo original, b estará unido con a
                #en el grafo auxiliar""""
                    new_graph.add_edge(n.vertex,i,n.weight)
        else:
            #Si el grafo es no dirigido, al trasponerlo no varía
            new_graph._vertices=self._vertices
        return new_graph

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        allverts=list(self._vertices.keys())
        for i in self._vertices.keys():
            bool=[False]
            verts=[]
            self._is_strongly_connected(i,verts,allverts,bool)
            if bool[0]==False:
                #Si hay un vértice que no esté conectado con todos los vértices restantes devolvemos False
                return False
        #Si cada vértice está unido con el resto de vértices del grafo,devolvemos true
        return True

    #Método recursivo
    def _is_strongly_connected(self,node,verts:list,allverts:list,bool:list):
        verts.append(node)
        if len(verts)==len(allverts):
            #Si el tamaño de verts es igual al tamaño de allverts(vertices del grafo), quiere decir que es conexo
            bool[0]=True
        #Miramos los vértices adyacentes a node
        for i in self._vertices[node]:
            if i.vertex not in verts:
                #Si no hemos visitado ese nodo lo recorremos
                self._is_strongly_connected(i.vertex,verts,allverts,bool)



