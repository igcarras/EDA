from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def busqueda(self, vertice_inicio: str, final: str, camino: int, camino_corto: int):
        if vertice_inicio == final:
            return camino
        else:
            if camino_corto == None or camino +1 <= camino_corto:
                for adj in self._vertices[vertice_inicio]:
                    if camino_corto == None or camino +1 <= camino_corto:
                        nuevocamino = self.busqueda(adj.vertex, final, camino+1, camino_corto)
                        if camino_corto == None or nuevocamino < camino_corto:
                            camino_corto = nuevocamino
            return camino_corto

    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        camino = self.busqueda(start, end, 0, None)
        if camino:
            print(camino)
            return camino
        return 0

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        #If graph is not directed, we return the same graph
        if(self._directed==True):
            labels = [v for v in  self._vertices.keys()]
            #create new graph
            newGraph = Graph2(labels,self._directed)
            #Nested loop for exchanging edges
            for key,v in self._vertices.items():
                for adjacents in v:
                    newGraph.add_edge(adjacents.vertex,key)
            print(newGraph)
            return newGraph
        return self
        

    def is_strongly_connected(self) -> bool:
        labels = [v for v in self._vertices.keys()]
        visited_vertex = {}
        for v in labels:
            #this loop has to be nested because python dictionary copies are references to the original object in memory
            for i in  self._vertices.keys():
                visited_vertex[i] = False
            if not self.checkStrongConnexion(self._vertices[v],visited_vertex,v,None):
                return False
        return True

    def checkStrongConnexion(self,adjacents,visited_vertex_copy,principal_vertex,current_vertex):
        #we return if we are back in the initial vertex
        if (principal_vertex==current_vertex):
            #if false value in array then return false
            return all(visited_vertex_copy.values())
        #check adajacents and mark then down
        for v in adjacents:
            #do not check adajacents if they have been visited in previus recursion
            if not visited_vertex_copy[v.vertex]:
                visited_vertex_copy[v.vertex]=True
                self.checkStrongConnexion(self._vertices[v.vertex],visited_vertex_copy,principal_vertex,v.vertex)
        return all(visited_vertex_copy.values())

    def min_number_edges_iterative(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        #Ir recorriendo desde el vertice inicial por "oleadas", si nos encontramos con uno que tiene visited true, no seguimos
        visited_vertex = {}
        iteration = 0
        queue = [start]
        currentQueue=[]
        ##Create visited_vertex 
        for v in  self._vertices.keys():
            visited_vertex[v] = False
        visited_vertex[start]=True
        #We will loop until the queue is 0, if we have not find the vertex before quiting the loop then the vertex is not accesible. 
        #
        while len(queue)>0:
            for v in queue:
                queue.pop(0)
                #Check if end is the vertex of -v- in that case we have finish and we should exit the loops
                if end in [self._vertices[v][i].vertex for i in range(len(self._vertices[v]))]:
                    iteration+=1
                    print(iteration)
                    return iteration
                ##If -end- is not there, we must add to currentQueu the next vertex (only if they have not been visited yet)
                for v2 in self._vertices[v]:
                    if(not visited_vertex[v2.vertex]):
                        currentQueue.append(v2.vertex)
                #reseting values for next loop
                if(len(queue)==0):
                    queue=currentQueue
                    currentQueue=[]
                    iteration+=1
        print("end is not accessible from start or is not in the graph")
        return 0
        
    

# labels = ['A', 'B', 'C', 'D', 'E',"F","G","H","I","J","K"]
# labels = ['A', 'B', 'C', 'D', 'E',"F"]
undirected_graph = Graph2(['A', 'B', 'C','D'], True)
undirected_graph.add_edge('A', 'B')
undirected_graph.add_edge('B', 'C')
undirected_graph.add_edge('C', 'A')
undirected_graph.add_edge('C', 'D')
undirected_graph.add_edge('D', 'A')

print(undirected_graph.is_strongly_connected())
print(undirected_graph)

