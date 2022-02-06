# -*- coding: utf-8 -*-
"""graph-dictionaryWDFull.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U8a7G5QUKNcFFMaDaUn9ZTT9tCr7nMgL

# Graph implementation using a Python dictionary

This implementation allows to represent any kind of graphs. This includes graph traversals and shortest path algorithm (disjktra)
"""

import sys

class AdjacentVertex:
    def __init__(self,vertex,weight):
        self.vertex=vertex
        self.weight=weight
  
    def __str__(self):
        return '('+str(self.vertex)+','+str(self.weight)+')'

class Graph():
    def __init__(self,labels,directed=True):
        self.vertices={}
        for v in labels:
            self.vertices[v]=[]
        self.directed=directed
    
    def addEdge(self, start, end, weight=0):
        if start not in self.vertices:
            print(start,' does not exist!')
            return
        if end not in self.vertices:
            print(end,' does not exist!')
            return
        
        self.vertices[start].append(AdjacentVertex(end,weight))
        if self.directed==False:
            self.vertices[end].append(AdjacentVertex(start,weight))
      
    def containsEdge(self, start, end):
        if start not in self.vertices:
            print(start,' does not exist!')
            return 0
        if end not in self.vertices:
            print(end,' does not exist!')
            return 0

        for adj in self.vertices[start]:
            if adj.vertex==end:
                return adj.weight
        return 0

    def removeEdge(self,start,end):
        if start not in self.vertices:
            print(start,' does not exist!')
            return
        if end not in self.vertices:
            print(end,' does not exist!')
            return

        for adj in self.vertices[start]:
            if adj.vertex==end:
                self.vertices[start].remove(adj)
        if self.directed==False:
            for adj in self.vertices[end]:
                if adj.vertex==start:
                    self.vertices[end].remove(adj)
  
    def __str__(self):
        result=''
        for v in self.vertices:
            result+='\n'+str(v)+':'
            for adj in self.vertices[v]:
                result+=str(adj)
            
        return result

    def bfs(self):
        """This functions prints all vertices of the graph by BFS traversal"""
        print('bfs traversal:')
        # Mark all the vertices as not visited 
        visited={}
        for v in self.vertices.keys():
            visited[v]=False

        for v in self.vertices.keys():
            if visited[v]==False:
                self._bfs(v,visited)

    # Function to print a BFS of graph 
    def _bfs(self, v,visited): 
        """This functions obtains the BFS traversal from the vertex 
        whose index is indexV."""
        
        # Create a queue for BFS. It will save the indices of vertices to visit
        queue = [] 
    
        #mark the source vertex as visited 
        visited[v] = True
        # and enqueue it 
        queue.append(v)
        
        while queue: 
            # Dequeue an index from queue and print its corresponding vertex(label)
            s = queue.pop(0) 
            #print (s, end = " ") 
            #we print the vertex, so we need to get its label
            print (s, end = " ") 
        
            # Get all adjacent vertices of the dequeued index. 
            # If an adjacent vertex has not been visited, 
            # then mark it visited and enqueue it 
            for adj in self.vertices[s]: 
                if visited[adj.vertex] == False: 
                    queue.append(adj.vertex) 
                    visited[adj.vertex] = True
 
    # The function to do DFS traversal. It uses 
    # recursive _dfs() 
    def dfs(self): 
        """This function prints all vertices of the graph by the DFS traversal."""
        
        print('dfs traversal:')
        # Mark all the vertices as not visited 
        visited={}
        for v in self.vertices.keys():
            visited[v]=False

        for v in  self.vertices.keys():
            if visited[v]==False:
                self._dfs(v, visited)
        print() 

    def _dfs(self, v, visited): 
        """This funcion prints the DFS traversal from the vertex whose index is indexV"""
        # Mark the current node as visited and print it 
        visited[v] = True
        #print(v, end = ' ') 
        #Instead of printing the index, we have to print its label
        print(v,end=' ')
        # Recur for all the vertices  adjacent to this vertex 
        for adj in self.vertices[v]: 
            if visited[adj.vertex] == False: 
                self._dfs(adj.vertex, visited) 


    def minDistance(self, distances, visited): 
        """This functions returns the vertex (index) with the mininum distance. We 
        only consider the set of vertices that have not been visited"""
        # Initilaize minimum distance for next node 
        min = sys.maxsize 

        #returns the vertex with minimum distance from the non-visited vertices
        for i in self.vertices: 
            if distances[i] <= min and visited[i] == False: 
                min = distances[i] 
                min_index = i 
    
        return min_index 

    def dijkstra(self, origin): 
        """"This function takes a vertex v and calculates its mininum path 
        to the rest of vertices by using the Dijkstra algoritm"""  
        
        #we use a Python list of boolean to save those nodes that have already been visited  
        # Mark all the vertices as not visited 
        visited={}
        for v in self.vertices.keys():
            visited[v]=False

        #this list will save the previous vertex 
        previous={}
        for v in self.vertices.keys():
            previous[v]=-1

        #This array will save the accumulate distance from v to each node
        distances={}
        for v in self.vertices.keys():
            distances[v]=sys.maxsize

        #The distance from v to itself is 0
        distances[origin] = 0
        
        for n in range(len(self.vertices)): 
            # Pick the vertex with the minimum distance vertex.
            # u is always equal to v in first iteration 
            u = self.minDistance(distances, visited) 
            # Put the minimum distance vertex in the shotest path tree
            visited[u] = True
            
            # Update distance value of the u's adjacent vertices only if the current  
            # distance is greater than new distance and the vertex in not in the shotest path tree 
            for adj in self.vertices[u]:
                i=adj.vertex
                w=adj.weight
                if visited[i]==False and distances[i]>distances[u]+w:
                    distances[i]=distances[u]+w   
                    previous[i]=u       
                
        #finally, we print the minimum path from v to the other vertices

        self.printSolution(distances,previous,origin)

    def printSolution(self,distances,previous,v): 
        print("Mininum path from ",v)
        for i in self.vertices:
            if distances[i]==sys.maxsize:
                print("There is not path from ",v,' to ',i)
            else: 
                minimum_path=[]
                prev=previous[i]
                while prev!=-1:
                    minimum_path.insert(0,prev)
                    prev=previous[prev]
                
                minimum_path.append(i)  

                print(v,'->',i,":", distances[i],minimum_path)

"""Now, we use the implementation to represent and trasverse this graph: 

<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/CPT-Graphs-directed-weighted-ex1.svg/722px-CPT-Graphs-directed-weighted-ex1.svg.png' width='25%'/>
"""

#we use this dictionary to represent the vertices with numbers:
labels=['A','B','C','D','E']

g=Graph(labels)

#Now, we add the edges
g.addEdge('A','C',12) #A->(12)C
g.addEdge('A','D',60) #A->(60)D
g.addEdge('B','A',10) #B->(10)A
g.addEdge('C','B',20) #C->(20)B
g.addEdge('C','D',32) #C->(32)D
g.addEdge('E','A',7)  #E->(7)A


print(g)


g.bfs()
print()


g.dfs()
print()


g.dijkstra('A')
print()

"""## Exercise: 

Calculate the minimum path from a to the rest of the vertices in this graph:

<img src='https://www.bogotobogo.com/python/images/Dijkstra/graph_diagram.png' src='25%'/>
"""

#we use this dictionary to represent the vertices with numbers:

labels=['a','b','c','d','e','f']

g=Graph(labels,False)

#Now, we add the edges
g.addEdge('a','b',7) 
g.addEdge('a','c',9) 
g.addEdge('a','f',14) 
g.addEdge('b','c',10) 
g.addEdge('b','d',15) 
g.addEdge('c','d',11)  
g.addEdge('c','f',2)
g.addEdge('d','e',6)
g.addEdge('e','f',9)

print()
print(g)
print()
g.bfs()
print()
g.dfs()
print()
g.dijkstra('a')
print()
g.dijkstra('f')
print()
g.dijkstra('b')
print()
