import math

"""
Name:
NIA:
group:
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
        accesibles = []
        if i < 0:
            return []
        if i > 99:
            return []
        resultado = self._dfs(i, h, accesibles)
        return resultado
    
    def _dfs(self, vertex, height, lista):
        
        if self._adjacent_islands[vertex] is not None:
            for adj in self._adjacent_islands[vertex]:
                if adj._height > height:
                    lista.append(adj._island)
                    self._dfs(adj._island, height, lista)
        else:
            return lista
        
        return lista
    
    
    
    def minimum_path(self, start: int, end: int, tide : int = 0) -> (list, int):
        ...
   
    



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
