def is_connected(self) -> bool:
    """returns True if the graph is connected, False eoc"""
    for vertex in self._vertices:
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False
        result = self._is_connected(vertex, visited)
        if not result:
            return False
    return True


def _is_connected(self, vertex, visited):
    visited[vertex] = True
    for a in self._vertices[vertex]:
        if not visited[a]:
            self._is_connected(a, visited)
    for ver in visited:
        if visited[ver] == False:
            return False
    return True


def is_bridge(self, v1: str, v2: str) -> bool:
    if self.is_connected() == False:
        return False
    contador1 = 0
    contador2 = 0
    for a in self._vertices[v1]:
        contador1 += 1
    for a in self._vertices[v2]:
        contador2 += 1
    if contador1 == 1 or contador2 == 1:
        return True
    grafonuevo = self.remove_edge(v1, v2)
    if self.is_connected() == False:
        return True
        grafonuevo = self.add_edge(v1, v2)
    return False


def remove_edge(self, start: object, end: object):
    for a in self._vertices[end]:
        if a == start:
            self._vertices[end].remove(a)
