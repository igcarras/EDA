import math


"""
Name: Inés Turrado
NIA: 100475307
group: 801
"""

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

    def _neigbours(self, vertex: int) -> list:
        lst_neigbours = []
        if self._adjacent_islands[vertex] is not None:
            for adj in self._adjacent_islands[vertex]:
                lst_neigbours.append(adj._island)
        return lst_neigbours

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

        # print("adding ", i1, i2, h, d)

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
        result_str = ''
        for v in range(self._num):
            result_str += '\n' + str(v) + ': '
            if self._adjacent_islands[v] is not None:
                for adj in self._adjacent_islands[v]:
                    result_str += str(adj) + ", "

            if result_str.endswith(", "):
                result_str = result_str[:-2]
        return result_str


    def accessible_from(self, i: int, h: int) -> list:
        if i is None or h is None:
            return None
        
        result = [] # list with the accessible vertices

        for adj in self._neigbours[i]: #Las islas a las que se puede llegar desde i son sus neighbours
            if self._height > h: #compruebo si la altura con cada adj a i es mayor
            
                result.append(adj.i)
        return result
          
               

    #def minimum_path(self, start: int, end: int, tide : int = 0) -> (list, int):
       # ...


    def min_distance(self, distances: dict, visited: dict) -> int:
        """returns the vertex (index) whose associated value in
        the dictionary distances is the smallest value. We
        only consider the set of vertices that have not been visited"""
        min_distance = math.inf
        min_vertex = None

        for vertex in self._adjacent_islands.keys():
            if distances[vertex] <= min_distance and not visited[vertex]:
                min_distance = distances[vertex]  
                min_vertex = vertex      

        return min_vertex

    def dijkstra(self, origin: object) -> None:
        visited = {}    
        previous = {}   
        distances = {}  

        for v in self._adjacent_islands.keys():
            visited[v] = False
            previous[v] = None
            distances[v] = math.inf

        distances[origin] = 0

        for _ in range(len(self._adjacent_islands)):
            u = self.min_distance(distances, visited)
            visited[u] = True
            for adj in self._adjacent_islands[u]:
                i = adj.vertex
                w = adj.weight
                if not visited[i] and distances[i] > distances[u]+w:
                    distances[i] = distances[u]+w
                    previous[i] = u


        return distances, previous
    
    def minimum_path(self, start: object, end: object, tide : int = 0) -> (list, int):
        """ returns a list containing the path from star to end.
        It also returns the distance of the path. If the path
        does not exist, it returns an empty list and infinitum"""
        if start not in self._adjacent_islands.keys():
            print(start, ' does not exist!!!')
            return None, None
        if end not in self._vertices.keys():
            print(end, ' does not exist!!!')
            return None, None

        distances, previous = self.dijkstra(start)
        if distances[end] == math.inf:
            return [], math.inf

        result = [end]
        prev = previous[end]
        while prev is not None:
            result.insert(0, prev)
            prev = previous[prev]

        return result, distances[end]


















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
        print()


    path, d = g3.minimum_path(0, 4, 1)
    print(path, d)

    print(g3.minimum_path(0, 3, 5))

    print(g3.minimum_path(2, 3, 1))
