# -*- coding: utf-8 -*-
"""
Created on Sat May 14 21:34:46 2022

@author: abesc
"""

import sys

from graph import AdjacentVertex
from graph import Graph

class Graph2(Graph):
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        return self._min_number_edges(start, end, 0, 0)
        
    def _min_number_edges(self, actual, end, path, suma):
        
        if actual == end:
            return suma
        else:
            if path == 0 or suma + 1 <= path:
                for v in self._vertices[actual]:
                    if path == 0 or suma + 1 <= path:
                        other_path = self._min_number_edges(v.vertex, end, path, suma + 1)
                        if path == 0 or other_path < path:
                            path = other_path
            return path
                    
                    
    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        auxGraph = []
        for v in self._vertices.keys():
            auxGraph.append(v)
        GraphT = Graph2(auxGraph)
        for v in self._vertices.keys():
            for w in self._vertices[v]:
                GraphT.add_edge(w.vertex, v)
        return GraphT

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        for vertice in self._vertices:
            visited = {}
            for v in self._vertices.keys():
                visited[v] = False
            if not self._is_strongly_connected(vertice, visited):
                return False
        return True
    def _is_strongly_connected(self, actual, visited):
        
        visited[actual] = True
        for adj in self._vertices[actual]:
            if not visited[adj.vertex]:
                self._is_strongly_connected(adj.vertex, visited)
        for v in visited:
            if visited[v] == False:
                return False
        return True