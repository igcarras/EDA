class MyGraph:

    def __init__(self, lst_vertices: list) -> None:
        self._vertices = {}
        for vertex in lst_vertices:
            self._vertices[vertex] = []

    def check_vertex(self, vertex: str) -> bool:
        return vertex in self._vertices

    def add_edge(self, v1: str, v2: str) -> None:
        if not self.check_vertex(v1):
            print(v1, " is not a vertex!!!")
            return
        if not self.check_vertex(v2):
            print(v2, " is not a vertex!!!")
            return
        if v2 in self._vertices[v1] or v1 in self._vertices[v2]:
            print("({},{}) multiple edges are not allowed!".format(v1, v2))
            return

        self._vertices[v1].append(v2)

    def minDistance(self, start: str, end: str) -> int:
        ...

    def __str__(self) -> str:
        """ returns a string containing the graph"""
        result = ''
        for v in self._vertices:
            result += '\n' + str(v) + ':'
            for adj in self._vertices[v]:
                result += str(adj) + "  "
        return result

    def minDistance_DFS(self, start: str, end: str) -> int:
        if not self.check_vertex(start):
            print(start, " is not a vertex!!!")
            return
        if not self.check_vertex(end):
            print(end, " is not a vertex!!!")
            return
        if start == end:
            return 0

        visited = {}
        for i in self._vertices:
            visited[i] = False

        levels = []
        self._minDistance_DFS(start, end, visited, 0, levels)
        if len(levels) == 0:
            return -1
        else:
            return min(levels)

    def _minDistance_DFS(self, start, end, visited, level, levels):
        visited[start] = True
        if start == end:
            levels.append(level)
        for i in self._vertices[start]:
            if visited[i] == False:
                self._minDistance_DFS(i, end, visited, level + 1, levels)
        visited[start] = False

    def minDistance_DFS2(self, start: str, end: str) -> int:
        if not self.check_vertex(start):
            print(start, " is not a vertex!!!")
            return
        if not self.check_vertex(end):
            print(end, " is not a vertex!!!")
            return
        if start == end:
            return 0

        visited = {}
        for i in self._vertices:
            visited[i] = False


        result = self._minDistance_DFS2(start, end, visited, 0)
        return result

    def _minDistance_DFS2(self, start, end, visited, level):
        visited[start] = True
        for i in self._vertices[start]:
            if i == end:
                return level
            if visited[i] == False:
                self._minDistance_DFS2(i, end, visited, level + 1)
        return -1

    def minDistance_BFS_v1(self, start: str, end: str) -> int:
        if not self.check_vertex(start):
            print(start, " is not a vertex!!!")
            return
        if not self.check_vertex(end):
            print(end, " is not a vertex!!!")
            return

        Q = [start]
        D = 0
        found = False
        visited = {}
        distances = {}

        for i in self._vertices.keys():
            visited[i] = False
            distances[i] = 0

        while len(Q) > 0 and not found:
            w = Q.pop(0)
            if w == end:
                found = True
            else:
                for adj in self._vertices[w]:
                    if visited[adj] == False:
                        visited[adj] = True
                        Q.append(adj)
                        distances[adj] = distances[w] + 1

        if found == True:
            return distances[end]
        else:
            return -1

    def minDistance_BFS_v2(self, start, end):
        if not self.check_vertex(start):
            print(start, " is not a vertex!!!")
            return
        if not self.check_vertex(end):
            print(end, " is not a vertex!!!")
            return
        if start == end:
            return 0

        visited = {}
        for i in self._vertices:
            visited[i] = False

        # Create a queue for BFS. It will save the indices of vertices to visit
        queue = []
        # mark the source vertex as visited
        visited[start] = True
        # and enqueue it
        queue.append((start, 0))

        while queue:
            # Dequeue a vertex from queue
            first_tuple = queue.pop(0)
            s = first_tuple[0]
            level = first_tuple[1]

            for adj in self._vertices[s]:
                if visited[adj] == False:
                    if (adj == end):
                        return level + 1
                    queue.append((adj, level + 1))
                    visited[adj] = True

        if visited[end] == False:
            return -1

    def minDistance_BFS_v3(self, start, end):
        if not self.check_vertex(start):
            print(start, " is not a vertex!!!")
            return
        if not self.check_vertex(end):
            print(end, " is not a vertex!!!")
            return
        if start == end:
            return 0

        visited = {}
        for i in self._vertices:
            visited[i] = False

        if start == end:
            return 0

        # Create a queue for BFS. It will save the indices of vertices to visit
        queue = []
        # mark the source vertex as visited
        visited[start] = True
        # and enqueue it
        queue.append(start)

        # start with level 0
        # and one vertex
        level = 0
        numVerticesActualLevel = 1

        while queue:

            # variables to store the vertices next level
            numAddedVertices = 0
            level += 1

            # for all the vertices of the same level
            # we add adjacents to the queue
            while (numVerticesActualLevel > 0):

                # each time we pop a vertex
                # we decrease the number of vertices in the level
                s = queue.pop(0)
                numVerticesActualLevel -= 1

                for adj in self._vertices[s]:
                    if (adj == end):
                        return level
                    if visited[adj] == False:
                        queue.append(adj)
                        # we count the vertices of the next level
                        numAddedVertices += 1
                        visited[adj] = True

            # we update the number of vertices of next level
            numVerticesActualLevel = numAddedVertices

        return -1

    def minDistance_BFS_v4(self, start, end):
        if not self.check_vertex(start):
            print(start, " is not a vertex!!!")
            return
        if not self.check_vertex(end):
            print(end, " is not a vertex!!!")
            return
        if start == end:
            return 0

        visited = {}
        distances = {}
        for i in self._vertices:
            visited[i] = False
            distances[i] = 0

        # Create a queue for BFS. It will save the indices of vertices to visit
        queue = []
        # mark the source vertex as visited
        visited[start] = True
        # and enqueue it
        queue.append(start)

        while queue:
            # Dequeue a vertex from queue
            s = queue.pop(0)

            for adj in self._vertices[s]:
                if visited[adj] == False:
                    queue.append(adj)
                    visited[adj] = True
                    distances[adj] = distances[s] + 1

        if visited[end] == False:
            return -1
        else:
            return distances[end]
    def minDistance_BFS_v5(self, start, end):
        if not self.check_vertex(start):
            print(start, " is not a vertex!!!")
            return
        if not self.check_vertex(end):
            print(end, " is not a vertex!!!")
            return
        if start == end:
            return 0

        visited = {}

        for i in self._vertices:
            visited[i] = False


        # Create a queue for BFS. It will save the indices of vertices to visit
        queue = []
        # mark the source vertex as visited

        # and enqueue it
        queue.append(start)

        result = 0

        while queue:
            # Dequeue a vertex from queue
            s = queue.pop(0)

            for adj in self._vertices[s]:
                if visited[adj] == False:
                    queue.append(adj)
                    visited[adj] = True
                    result+=1
                    if adj==end:
                        return  result
        if visited[end] == False:
            return -1



if __name__ == '__main__':
    labels = ['A', 'B', 'C', 'D', 'E']

    g = MyGraph(labels)

    # Now, we add the edges
    g.add_edge('A', 'C')
    g.add_edge('A', 'D')
    g.add_edge('C', 'D')
    g.add_edge('B', 'C')
    g.add_edge('D', 'E')

    print(g)
    print()

    print("Solution based on DFS:")
    print(g.minDistance_DFS('A', 'A'))
    print(g.minDistance_DFS('A', 'B'))
    print(g.minDistance_DFS('A', 'C'))
    print(g.minDistance_DFS('A', 'D'))
    print(g.minDistance_DFS('A', 'E'))

    print("Solution based on DFS2:")
    print(g.minDistance_DFS2('A', 'A'))
    print(g.minDistance_DFS2('A', 'B'))
    print(g.minDistance_DFS2('A', 'C'))
    print(g.minDistance_DFS2('A', 'D'))
    print(g.minDistance_DFS2('A', 'E'))

    print()
    print("Solution based on BFS v1:")
    print(g.minDistance_BFS_v1('A', 'A'))
    print(g.minDistance_BFS_v1('A', 'B'))
    print(g.minDistance_BFS_v1('A', 'C'))
    print(g.minDistance_BFS_v1('A', 'D'))
    print(g.minDistance_BFS_v1('A', 'E'))

    print()
    print("Solution based on BFS v2:")
    print(g.minDistance_BFS_v2('A', 'A'))
    print(g.minDistance_BFS_v2('A', 'B'))
    print(g.minDistance_BFS_v2('A', 'C'))
    print(g.minDistance_BFS_v2('A', 'D'))
    print(g.minDistance_BFS_v2('A', 'E'))

    print()
    print("Solution based on BFS v3:")
    print(g.minDistance_BFS_v3('A', 'A'))
    print(g.minDistance_BFS_v3('A', 'B'))
    print(g.minDistance_BFS_v3('A', 'C'))
    print(g.minDistance_BFS_v3('A', 'D'))
    print(g.minDistance_BFS_v3('A', 'E'))

    print()
    print("Solution based on BFS v4:")
    print(g.minDistance_BFS_v4('A', 'A'))
    print(g.minDistance_BFS_v4('A', 'B'))
    print(g.minDistance_BFS_v4('A', 'C'))
    print(g.minDistance_BFS_v4('A', 'D'))
    print(g.minDistance_BFS_v4('A', 'E'))


    print()
    print("Solution based on BFS v5:")
    print(g.minDistance_BFS_v5('A', 'A'))
    print(g.minDistance_BFS_v5('A', 'B'))
    print(g.minDistance_BFS_v5('A', 'C'))
    print(g.minDistance_BFS_v5('A', 'D'))
    print(g.minDistance_BFS_v5('A', 'E'))

    G = MyGraph(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
    G.add_edge('A', 'B')
    G.add_edge('B', 'C')
    G.add_edge('C', 'A')
    G.add_edge('D', 'B')
    G.add_edge('C', 'E')
    G.add_edge('E', 'F')
    G.add_edge('C', 'F')
    G.add_edge('C', 'D')
    G.add_edge('F', 'G')
    G.add_edge('G', 'H')
    G.add_edge('H', 'A')
    G.add_edge('I', 'H')

    print(G)
    print("Solution based on BFS v1:")
    print(G.minDistance_BFS_v1('C', 'G'))
    print(G.minDistance_BFS_v1('I', 'D'))

    print("Solution based on BFS v2:")
    print(G.minDistance_BFS_v2('C', 'G'))
    print(G.minDistance_BFS_v2('I', 'D'))

    print("Solution based on BFS v3:")
    print(G.minDistance_BFS_v3('C', 'G'))
    print(G.minDistance_BFS_v3('I', 'D'))

    print("Solution based on BFS v4:")
    print(G.minDistance_BFS_v4('C', 'G'))
    print(G.minDistance_BFS_v4('I', 'D'))

    print("Solution based on BFS v5:")
    print(G.minDistance_BFS_v5('C', 'G'))
    print(G.minDistance_BFS_v5('I', 'D'))