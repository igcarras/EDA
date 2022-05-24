#Alberto Casas Ramirez Grupo 84
    def is_connected(self) -> bool:
        """returns True if the graph is connected, False eoc"""
        vissited = [list(self._vertices.keys())[0]]
        queue = [list(self._vertices.keys())[0]]
        while len(queue):
            for vertex in self._vertices[queue.pop(0)]:
                if vertex not in vissited:
                    vissited.append(vertex)
                    queue.append(vertex)
        return compare_lists(vissited, list(self._vertices.keys()))
    def is_bridge(self, v1: str, v2: str) -> bool:
        if v2 in self._vertices[v1] or v1 in self._vertices[v2]:
            newGraph = MyGraph(list(self._vertices.keys()))
            for k, v in self._vertices.items():
                for x in v:
                    if not (k==v1 and x==v2) and not(k==v2 and x==v1):
                        newGraph.add_edge(k, x)
            return not newGraph.is_connected()
        return False
