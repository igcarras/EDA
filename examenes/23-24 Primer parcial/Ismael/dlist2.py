from dlist import DList, DNode

class DList2(DList):
    def add_duplicates_last(self, k):
        if len(self) > 0:
            count = 0
            long_list = len(self)
            current_index = 0
            current = self._head
            for i in range(long_list):
                if current.elem < k:
                    nodo = DNode(current.elem)
                    nodo.prev = self._tail
                    self._tail.next = nodo
                    self._tail = nodo
                    self._size += 1
                    count += 1
                current = current.next
                current_index += 1
            return count
