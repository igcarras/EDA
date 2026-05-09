"""This file contains the solution for is_tree using dfs"""

class MyGraph:
    def __init__(self, list_vertices: list) -> None:
        self._vertices = {}
        for i in list_vertices:
            self._vertices[i] = []
    def add_edge(self, i, j):
        if i not in self._vertices.keys():
            return
        if j not in self._vertices.keys():
            return
        self._vertices[i].append(j)
        self._vertices[j].append(i)
        
    def is_tree(self) -> bool:
        if not self._vertices or len(self._vertices) == 0:
            return True
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False
            
        #we start from an arbitrary node
        vertex = next(iter(self._vertices))
        #we check for cycles
        isTree = self._dfs(vertex,visited,None)
        if not isTree:
            return False
        #we check for non visited nodes
        for vertex in self._vertices.keys():
            if not visited [vertex]:
                return False
        return isTree
        
    def _dfs(self, v, visited,previous): 
        # Mark the current node as visited 
        visited[v] = True
        # Recurse for all the vertices  adjacent to this vertex 
        for adj in self._vertices[v]: 
          if visited[adj] == False: 
              #if we have detected a cycle, we return False
              if not self._dfs(adj, visited,v):
                    return False
          #a cycle is detected if adjacent node have been visited 
          #through another path
          elif adj != previous:
             return False
        return True
            
 

# Some usage examples
if __name__ == '__main__':
    # first example in the exam
    g = MyGraph([1, 2,3,4,5])
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(2, 5)

    print(g.is_tree())

    # second example in the exam
    g = MyGraph([1, 2,3,4,5])
    g.add_edge(1, 3)
    g.add_edge(1, 2)
    g.add_edge(3, 2)
    g.add_edge(3, 4)
    g.add_edge(2, 5)

    print(g.is_tree())
    
    # thirde example in the exam
    g = MyGraph([1, 2,3,4,5])
    g.add_edge(1, 3)
    g.add_edge(1, 2)
    g.add_edge(3, 4)
    g.add_edge(2, 5)

    print(g.is_tree())

    
    