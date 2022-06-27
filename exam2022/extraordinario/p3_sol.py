from queue import Queue
import math

class AdjacentIsland:
        def __init__(self, i: int, h: int, d: int) -> None:
            """This constructor creates a 3-tuple where
            we save the connected island, the height of the
            bridge, and the length of the bridge"""
            self._island = i
            self._height = h
            # height
            self._distance = d  # length of the bridge
        def __str__(self):
            return '('+str(self._island) + ", " + str(self._height)+ ", " + str(self._distance)+')'

class Archipelago:

    def __init__(self, n: int) -> None:
        """As the (names) ids of islands are number from 0
        to n-1, we do not need a dictionary.
        We simply need to use a Python list
        where we can save the adjacent islands for each island"""
        self._num = n
        self._adjacent_islands = [None] * n  # will be a list of lists
        print(self._adjacent_islands)

    def _neigbours(self, island) -> list:
        result = []
        if self._adjacent_islands[island] is not None:
            for adj in self._adjacent_islands[island]:
                result.append(adj._island)
        return result
    def add_bridge(self, i1: int, i2: int, h: int, d: int) -> None:
        """i1, i2: islands to be connected.
            h: height of the bridge that connects both islands
            d: length of the bridge that connects both islands"""
        if i1 not in range(self._num):
            print(i1, " is not an island!!!")
            return
        if i2 not in range(self._num):
            print(i2, " is not an island!!!")
            return
        if i1 == i2:
            print('loops are not allowed')
            return
        if h <= 0:
            print(h, ' the height should be positive')
            return
        if d <= 0:
            print(d, ' the length should be positive')
            return
        print("adding ", i1,i2,h,d)

        if i1 in self._neigbours(i2):
            print("Error: already exist bridge between {} and {}".format(i1,i2))
            return
        if i2 in self._neigbours(i1):
            print("Error: already exist bridge between {} and {}".format(i2,i1))
            return

        if self._adjacent_islands[i1] is None:
            #  create the empty list
            self._adjacent_islands[i1] = []
        if self._adjacent_islands[i2] is None:
            #  create the empty list
            self._adjacent_islands[i2] = []

        self._adjacent_islands[i1].append(AdjacentIsland(i2, h, d))
        self._adjacent_islands[i2].append(AdjacentIsland(i1, h, d))


    def __str__(self) -> str:
        """ returns a string containing the graph"""
        result = ''
        for island in range(self._num):
            result += '\n' + str(island) + ': '
            if self._adjacent_islands[island] is not None:
                for adj in self._adjacent_islands[island]:
                    result += str(adj) + ", "

            if result.endswith(", "):
                result = result[:-2]
        return result

    def accessible_from(self, i: int, h: int) -> list:
        return self.accessible_from_bfs(i,h)
        # return self.accessible_from_dfs(i,h)

    def accessible_from_bfs(self, i: int, h: int) -> list:
        """Suppose that the tide has increased h metres,
        this method has to return the list of islands that are accessible
        from i.
        """
        if i not in range(self._num):
           return []
        
        visited = [False] * self._num
        accessible = []
        q = Queue()
        q.put(i)
        visited[i] = True
        while not q.empty():
            island = q.get()
            accessible.append(island)
            if self._adjacent_islands[island] is not None:
                for adj in self._adjacent_islands[island]:
                    if not visited[adj._island] and adj._height > h:
                        q.put(adj._island)
                        visited[adj._island] = True

        return accessible[1:]
    
    def accessible_from_dfs(self, i: int, h: int) -> list:
        if i not in range(self._num):
            return []
        
        visited = [False] * self._num
        accessible = []
        self._accessible_from_dfs(i, h, visited, accessible)
        return accessible[1:]
    
    def _accessible_from_dfs(self, i: int, h: int, visited: list, accessible: list) -> None:
        visited[i] = True
        accessible.append(i)
        if self._adjacent_islands[i] is not None:
            for adj in self._adjacent_islands[i]:
                if not visited[adj._island]  and adj._height > h:
                    self._accessible_from_dfs(adj._island, h, visited, accessible)


    def min_distance(self, distances: dict, visited: dict) -> int:
        """returns the island with the minimum distance accumulated"""
        min_distance = math.inf
        min_vertex = None

        for i in range(self._num):
            if distances[i] <= min_distance and not visited[i]:
                min_distance = distances[i]  # update the new smallest
                min_vertex = i      # update the index of the smallest

        return min_vertex
    
    
    def dijkstra(self, origin: int, tide: int) -> (list, list):
        visited = [False] * self._num
        previous = [None] * self._num
        distance = [math.inf] * self._num

        distance[origin] = 0

        for n in range(self._num):
            u = self.min_distance(distance, visited)
            visited[u] = True

            if self._adjacent_islands[u] is not None:
                for adj in self._adjacent_islands[u]:
                    i = adj._island
                    w = adj._distance
                    h = adj._height

                    if h > tide and not visited[i] and distance[i] > distance[u]+w:
                        # we must update because its distance is greater than the new distance
                        distance[i] = distance[u]+w
                        previous[i] = u

        # Finally, we print the minimum path from origin to the other vertices
        return distance, previous
    
    
      
        
    def minimum_path(self, origin: int, target: int, tide : int = 0) -> (list, int):
        
        if origin not in range(self._num):
            return [],math.inf
        if target not in range(self._num):
            return [],math.inf
        
        distance, previous = self.dijkstra(origin, tide)
        if distance[target] == math.inf:
            print("There is no possible path between ", origin, " and ", target)
            return [], math.inf

        minimum_path = []
        prev = previous[target]
        # this loop helps us to build the path
        while prev is not None:
            minimum_path.insert(0, prev)
            prev = previous[prev]

        minimum_path.append(target)

        return minimum_path, distance[target]


if __name__ == '__main__':
    g3 = Archipelago(7)
    g3.add_bridge(0, 1, 2, 3)

    g3.add_bridge(0, 2, 5, 10)
    g3.add_bridge(1, 2, 3, 2)
    g3.add_bridge(1, 3, 3, 3)
    g3.add_bridge(2, 3, 4, 10)
    g3.add_bridge(2, 4, 5, 3)
    g3.add_bridge(3, 4, 4, 4)

    print(g3)

    island = 0
    for island in range(7):
        for height in range(6):
            print('accessible_from {} with height {}'.format(island, height))
            result = g3.accessible_from(island, height)
            print(result)
            result = g3.accessible_from_dfs(island, height)
            print(result)
        print()


    path, d = g3.minimum_path(0, 4, 1)
    print(path, d)

    print(g3.minimum_path(0, 3, 5))

    print(g3.minimum_path(2, 3, 1))
