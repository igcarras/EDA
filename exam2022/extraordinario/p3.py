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
        self._adjacent_islands = [None] * n# will be a list of lists
        #print(self._adjacent_islands)

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
        if h<=0:
            print(h, ' the height should be positive')
            return
        if d<=0:
            print(d, ' the length should be positive')
            return
        if self._adjacent_islands[i1] is not None:
            accessible_from_i1 = self._adjacent_islands[i1]
            for adj in accessible_from_i1:
                if adj._island == i2:
                    print("Error: it already exist a bridge between "+ str(i1) + " to " + str(i2))
                    return
        else:
            self._adjacent_islands[i1] = []

        if self._adjacent_islands[i2] is None:
            self._adjacent_islands[i2] = []

        # If we reach this line, it means that the two islands
        # do not have a bridge between them
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

    def non_accessible_islands(self) -> list:
        """returns a list with the islands that are
        non-accessible.
         Mark: 0.33"""
        result = []
        for i in range(self._num):
            if self._adjacent_islands[i] is None:
                result.append(i)
        return result

    def islands_k_bridges(self, k : int) -> list:
        """returns a list with the islands that exactly has
        k bridges.
        Mark: 0.5"""
        result = []
        for i in range(self._num):
            if self._adjacent_islands[i] is not None and len(self._adjacent_islands[i]) == k:
                result.append(i)
            elif self._adjacent_islands[i] is None and k==0 :
                result.append(i)
        return result

    def accessible_from(self, i: int, h: int) -> list:
        """Suppose that the tide has increased h metres,
        the methods has to return the list of islands that are accessible
        from i.
        Mark: 1.5"""

        if i not in range(self._num):
           return []
        
        visited = [False] * self._num
        accessible = []
        q=Queue()
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

                    if h >= tide and not visited[i] and distance[i] > distance[u]+w:
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
    
    g3 = Archipelago(4)
    g3.add_bridge(0, 1, 5, 1)
    g3.add_bridge(0, 2, 4, 1)
    g3.add_bridge(0, 3, 3, 10)
    g3.add_bridge(1, 2, 4, 1)
    g3.add_bridge(2, 3, 3, 1)
    print(g3)
    a,b = g3.dijkstra (0,1)
    print (a,b)
    path, d= g3.minimum_path (0,4,1)
    print (path, d)
 
       
    
    """
    archi = Archipelago(10)
    archi.add_bridge(0, 1, 5, 10)
    archi.add_bridge(0, 2, 4, 3)
    archi.add_bridge(0, 3, 3, 15)
    archi.add_bridge(2, 3, 4, 3)
    archi.add_bridge(3, 8, 3, 3)

    archi.add_bridge(6, 8, 2, 3)
    archi.add_bridge(8, 9, 2, 3)

    print("First graph: ", str(archi))

    print("non accessible islands", archi.non_accessible_islands())
    print("islands with k=1 bridges", archi.islands_k_bridges(1))
    print("islands with k=2 bridges", archi.islands_k_bridges(2))
    print("islands with k=3 bridges", archi.islands_k_bridges(3))
    print("islands with k=4 bridges", archi.islands_k_bridges(4))
    
    
    print("accessible_from 4, h = 1", archi.accessible_from(4, 1))
    print("accessible_from 0, h = 1", archi.accessible_from(0, 1))
    print("accessible_from 0, h = 2", archi.accessible_from(0, 2))
    print("accessible_from 0, h = 3", archi.accessible_from(0, 3))

    print("accessible_from 0, h = 4", archi.accessible_from(0, 4))

    print("accessible_from 0, h = 1", archi.accessible_from(0, 1))
    print("accessible_from 0, h = 2", archi.accessible_from(0, 2))
    print("accessible_from 0, h = 3", archi.accessible_from(0, 3))

    print("accessible_from 9, h = 4", archi.accessible_from(9, 4))
    print("accessible_from 9, h = 3", archi.accessible_from(9, 3))
    print("accessible_from 9, h = 2", archi.accessible_from(9, 2))
    print("accessible_from 9, h = 1", archi.accessible_from(9, 1))
    print("accessible_from 9, h = 0", archi.accessible_from(9, 0))

    print("min distance from 0 to 3", archi.minimum_path(0,3,0))
    print("min distance from 0 to 3", archi.minimum_path(0,8,0))
    """
