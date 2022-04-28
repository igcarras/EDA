# -*- coding: utf-8 -*-

import sys
from graph import Graph

class GraphDijkstra(Graph):
    """ # Dijkstra’s shortest path algorithm"""
    def min_distance(self, distances: dict, visited: dict) -> int:
        """returns the vertex (index) whose associated value in
        the dictionary distances is the smallest value. We
        only consider the set of vertices that have not been visited"""
        # Initialize minimum distance for next node
        min_distance = sys.maxsize
        min_vertex = None

        # returns the vertex with minimum distance from the non-visited vertices
        for vertex in self._vertices.keys():
            if distances[vertex] <= min_distance and not visited[vertex]:
                min_distance = distances[vertex]  # update the new smallest
                min_vertex = vertex      # update the index of the smallest

        return min_vertex

    def dijkstra(self, origin: object) -> None:
        """ This function takes a vertex v and
        obtains the minimum path from it
        to the rest of vertices by using the Dijkstra algorithm"""

        # visited is a dictionary whose keys are the vertices of our graph.
        # When we visit a vertex, we must mark it as True.
        # Initially, all vertices are defined as False (not visited)
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False

        # This dictionary will save the previous vertex for the key in the minimum path
        previous = {}
        for v in self._vertices.keys():
            # initially, we define the previous vertex for any vertex as None
            previous[v] = None

        # This dictionary will save the accumulated distance
        # from the origin to the vertex (key)
        distances = {}
        for v in self._vertices.keys():
            distances[v] = sys.maxsize

        # The distance from origin to itself is 0
        distances[origin] = 0

        for n in range(len(self._vertices)):
            # Pick the vertex with the minimum distance vertex.
            # u is always equal to origin in first iteration
            u = self.min_distance(distances, visited)
            visited[u] = True
            # Update distance value of the u's adjacent vertices only if the current
            # distance is greater than new distance and the vertex in not in the
            # shortest path tree
            # we must visit all adjacent vertices (neighbours) for u
            for adj in self._vertices[u]:
                i = adj.vertex
                w = adj.weight
                if not visited[i] and distances[i] > distances[u]+w:
                    # we must update because its distance is greater than the new distance
                    distances[i] = distances[u]+w
                    previous[i] = u

        # Finally, we print the minimum path from origin to the other vertices
        self.print_solution(distances, previous, origin)

    def print_solution(self, distances: dict, previous: dict, origin: object):
        print("Minimum path from ", origin)

        for i in self._vertices.keys():
            if distances[i] == sys.maxsize:
                print("There is not path from ", origin, ' to ', i)
            else:
                # minimum_path is the list which contains the minimum path from origin to i
                minimum_path = []
                prev = previous[i]
                # this loop helps us to build the path
                while prev is not None:
                    minimum_path.insert(0, prev)
                    prev = previous[prev]

                # we append the last vertex, which is i
                minimum_path.append(i)

                # we print the path from v to i and the distance
                print(origin, '->', i, ":", minimum_path, distances[i])


if __name__ == '__main__':
    # Now, we use the implementation to represent this graph:
    #  <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/CPT-Graphs-directed-weighted-ex1.svg/722px-CPT-Graphs-directed-weighted-ex1.svg.png' width='25%'/>

    labels = ['A', 'B', 'C', 'D', 'E']
    g = GraphDijkstra(labels)
    # Now, we add the edges
    g.add_edge('A', 'C', 12)  # A->(12)C
    g.add_edge('A', 'D', 60)  # A->(60)D
    g.add_edge('B', 'A', 10)  # B->(10)A
    g.add_edge('C', 'B', 20)  # C->(20)B
    g.add_edge('C', 'D', 32)  # C->(32)D
    g.add_edge('E', 'A', 7)  # E->(7)A
    print(g)

    g.dijkstra('A')

    # Exercise: Calculate the minimum path from
    # 'a' to the rest of the vertices in this graph:
    # <img src='https://www.bogotobogo.com/python/images/Dijkstra/graph_diagram.png' src='25%'/>

    labels = ['a', 'b', 'c', 'd', 'e', 'f']
    g = GraphDijkstra(labels, False)

    # Now, we add the edges
    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)
    print(g)

    g.dijkstra('a')
    g.dijkstra('f')
    g.dijkstra('b')

    # Exercise: Use the previous implementation to obtain the minimum path from X to Y in this graph:
    #  <img src='http://benalexkeen.com/wp-content/uploads/2017/01/Dijkstra.png'>
