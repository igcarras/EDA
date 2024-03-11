from dlist import DList, DNode

class DList2(DList):
    def add_duplicates(self, k):
        contador = 0
        if len(self) > 0:
            current = self._head
            while current:
                if current.elem < k:
                    nodo = DNode(current.elem)
                    nodo.next = current.next
                    anterior_siguiente = current.next
                    if current.next:
                        current.next.prev = nodo
                    else:
                        self._tail = nodo
                    current.next = nodo
                    nodo.prev = current
                    self._size +=1
                    contador += 1
                    current = anterior_siguiente
                else:
                    current = current.next
        return contador
