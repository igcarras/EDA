from dlist import DList, DNode

class DList2(DList):
    def copy_node_next(self, k):
        count = 0
        if len(self) > 0:
            current = self._head
            while current:
                if current.elem < k:
                    nodo = DNode(current.elem)
                    nodo.next = current.next
                    aux_prev_next = current.next
                    if current.next:
                        current.next.prev = nodo
                    else:
                        self._tail = nodo
                    current.next = nodo
                    nodo.prev = current
                    self._size +=1
                    count += 1
                    current = aux_prev_next
                else:
                    current = current.next
        return count
