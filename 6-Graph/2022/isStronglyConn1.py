# -*- coding: utf-8 -*-
"""
Created on Tue May 25 23:18:39 2021

@author: ishernanz
"""

class MyGraph:
    def __init__(self,n):
    	self.vertices={}
    	for i in range(n):
    		self.vertices[i]=[]

    def addConnection(self,i,j):
    	if i not in self.vertices.keys():
    		return
    	if j not in self.vertices.keys():
    		return
    	self.vertices[i].append(j)

    def isStronglyConn(self):
        visitados1 = {}
        for i in self.vertices.keys():
            visitados1[i] = False
        self._dfs(self.vertices[0], visitados1)
        for i in self.vertices.keys():
            if visitados1[i] == False:
                return False
        visitados2 = {}
        for i in self.vertices.keys():
            visitados2[i] = False
        self._dfs(self.vertices[-1], visitados2)
        for i in self.vertices.keys():
            if visitados2[i] == False:
                return False
    def _dfs(self, vertice, visitados):
        visitados[vertice] = True
        for adj in self.vertices[vertice]:
            if visitados[adj._vertex] == False:
                visitados[adj._vertex] = True
    def __str__(self):
        result=''
        for v in self.vertices:
            result+='\n'+str(v)+':'
            for adj in self.vertices[v]:
                result+=str(adj)+"  "
        return result

if __name__ == '__main__':

    g=MyGraph(5)
    g.addConnection(0,1) # A:0, B:1
    g.addConnection(0,2) # A:0, C:2
    g.addConnection(0,4) # A:0, E:5
    g.addConnection(1,4) # B:1, D:4
    g.addConnection(2,1) # C:2, B:1
    g.addConnection(4,3)
    g.addConnection(3,1)
    g.addConnection(3,0)

    #g.addEdge('A','H',8)

    print(g)
    print('................')
    print(g.isStronglyConn())
    print('..............................')
    g=MyGraph(4)
    g.addConnection(0,1) # A:0, B:1
    g.addConnection(1,2) # A:0, C:2
    g.addConnection(2,4) # A:0, E:5
    g.addConnection(4,2) # B:1, D:4
    g.addConnection(2,1) # C:2, B:1
    g.addConnection(2,3)
    g.addConnection(3,0)


    #g.addEdge('A','H',8)

    print(g)
    print('................')
    print(g.isStronglyConn())
    print('..............................')
    g=MyGraph(5)
    g.addConnection(0,1) # A:0, B:1
    g.addConnection(1,2) # A:0, C:2
    g.addConnection(2,3) # A:0, E:5
    g.addConnection(3,4) # B:1, D:4
    g.addConnection(4,5) # C:2, B:1



    #g.addEdge('A','H',8)

    print(g)
    print('................')
    print(g.isStronglyConn())