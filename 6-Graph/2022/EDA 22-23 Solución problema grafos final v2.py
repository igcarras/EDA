# -*- coding: utf-8 -*-
"""
Created on Tue May 16 22:30:25 2023

@author: ishernanz
"""

class MyGraph:
  def __init__(self,L):
     self.vertices={}
     for i in L:
        self.vertices[i]=[]
  def addEdge(self,i,j):
     if i not in self.vertices.keys():
        return
     if j not in self.vertices.keys():
        return
     self.vertices[i].append(j)

  def shortPathToOdd(self, k):
      L=[]
      visited={}
      for v in self.vertices.keys():
          print(v)
          for m in self.vertices.keys():
              visited[m]=False
          print('\t',v)
          if self._shortPathToOdd(v,k,visited,v)==True:
              print('\t',v)
              L.append(v)
      return L
    
  def _shortPathToOdd(self,vertex,k,visited,origin):
      visited[vertex]=True
      R=False
      if k==0:
          R=False
      elif vertex%2!=0 and vertex!=origin:
          R=True
      else:
          for u in self.vertices[vertex]:
              print(u)
              if visited[u]==False:
                  R=R or self._shortPathToOdd(u,k-1,visited,origin)
      return R      

L=[2,4,6,8,10,12,14,16,15]
G=MyGraph(L)
print(G.vertices)
G.addEdge(4,6)
G.addEdge(4,8)
G.addEdge(6,12)
G.addEdge(8,10)
G.addEdge(12,16)
G.addEdge(10,14)
G.addEdge(14,15)
G.addEdge(12,15)

#print(G._shortPathToOdd(14,2,{2: [False], 4: [False], 6: [False], 8: [False], 10: [False], 12: [False], 14: [False], 16: [False], 15: [False]}))
print(G.shortPathToOdd(3))
