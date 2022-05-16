#Jorge Ramos Santana 100451001
#Marina Perez Barbero 100472115


from graph import AdjacentVertex
from graph import Graph
import sys
class Graph2(Graph):

    #Pseudo-dikjstra contando todos los pesos como 1 
    def minAristas(self, aristas, visited):
        min = sys.maxsize
        for v in self._vertices.keys():
            if aristas[v] <= min and visited[v] == False:
                min = aristas[v]
                min_vertex = v
        return min_vertex

    def min_number_edges(self, start, end) -> int:
        visited = {}
        #marcar todos los vertices como no visitados para inicializar
        for v in self._vertices.keys():
            visited[v] = False
            aristas = {}
        #marcar todos los distancias como infinito para el "pseudo-dikjstra"
        for v in self._vertices.keys():
            aristas[v] = sys.maxsize

        aristas[start] = 0
        
        for n in range(len(self._vertices)):
            u = self.minAristas(aristas, visited)
            visited[u] = True
            for adj in self._vertices[u]:
                if visited[adj.vertex] == False and aristas[adj.vertex] > aristas[u]:
                    aristas[adj.vertex] = aristas[u] + 1

        if aristas[end] == sys.maxsize:
            return 0
        else:
            return aristas[end]
 
    # Usando un grafo auxiliar, se va comprobando vertice a vertice del grafo inicial, y los vertices adyacentes se añaden al
    # segundo grafo de manera que los lados queden cambiados de sentido
    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        if self._directed:
            graph_aux = Graph2(self._vertices)

            for n in self._vertices:
                for adj in self._vertices[n]:
                    graph_aux._vertices[adj.vertex].append(AdjacentVertex(n,adj.weight))

            return graph_aux

        else:
            return self


    # Si el grafo es fuertemente conexo, al ejecutar dfs UNA sola vez se podran visitar todos los vertices.
    # Para estar seguros de que esto se cumple para todos los vertices, basta con ejecutar dfs una sola vez partiendo de cada vertice.
    # Si en cualquiera de estas iteraciones dfs no es capaz de visitar todos los vertices, entonces el grafo no es fuertemente conexo.
    def is_strongly_connected(self) -> bool:
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False

        for n in self._vertices:
            print("ver", n)
            u = self.dfs(n)

            if len(u) != len(self._vertices):
                return False

        return True

    def dfs(self,ver):
        """This function prints all vertices of the graph by the DFS traversal."""
        print('dfs traversal:')
        # Mark all the vertices as not visited
        camino = []
        visited={}
        for v in self._vertices.keys():
            visited[v] = False
        self._dfs(ver, visited, camino)
        '''
        for v in  self._vertices.keys():
            if visited[v] == False:
                self._dfs(v, visited,camino)
        '''
        print()
        return camino

    def _dfs(self, v, visited, camino):
        """This funcion prints the DFS traversal from the vertex whose index is indexV"""
        # Mark the current node as visited and print it
        visited[v] = True
        camino.append(v)
        #print(v, end = ' ')
        #Instead of printing the index, we have to print its label
        print(v,end=' ')
        # Recur for all the vertices  adjacent to this vertex
        for adj in self._vertices[v]:
          if visited[adj.vertex] == False:
            self._dfs(adj.vertex, visited, camino)
        return camino






labels = ['A', 'B', 'C', 'D', 'E','F','G']
g = Graph2(labels, False)
g.add_edge('A', 'B')  # A:0,  B:1
g.add_edge('C', 'A')  # A:0,  C:2
g.add_edge('C', 'E')  # A:0,  E:5
g.add_edge('F', 'D')  # B:1,  D:4
g.add_edge('D', 'G')  # C:2,  B:1
g.add_edge('B', 'C')
g.add_edge('G', 'F')
g.add_edge('E', 'D')
# .add_edge('A', 'H', 8)
print(g)
print()
#print("Grado traspuesto",g.transpose())
print(g.min_number_edges('A','F'))

'''
labels = ['A', 'B', 'C']
d = Graph2(labels, False)
d.add_edge('A', 'B')
d.add_edge('A', 'C')
d.add_edge('B','C')
print(d)
print()
print("Grado traspuesto", d.transpose())

labels = ['A', 'B', 'C','D']
f = Graph2(labels, True)
f.add_edge('A', 'B')
f.add_edge('A', 'C')
#d.add_edge('A', 'C')
f.add_edge('B','C')
#f.add_edge('C','D')
f.add_edge('B','D')
print(f)
print("Minimo numero de aristas:",f.min_number_edges('A','C'))
#print("Minimo numero de aristas:",f.min_number_edges('B','C'))

labels = ['A', 'B', 'C','D']
g = Graph2(labels, True)

g.add_edge('A','C')
g.add_edge('A','B')
g.add_edge('C', 'D')
#g.add_edge('D', 'A')
g.add_edge('B', 'D')
#g.is_strongly_connected()
print(g.is_strongly_connected())

lave = ['A','B','C','G','F','E']
a = Graph2(lave, False)
a.add_edge('A','G')
a.add_edge('A','F')
a.add_edge('C', 'F')
a.add_edge('B', 'E')
a.add_edge('G', 'C')
a.add_edge('C', 'G')
#print(a)
print(a.is_strongly_connected())
'''