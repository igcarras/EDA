from dlist import DList
from dlist import DNode


class DList2(DList):
    def add_duplicates_last(self, k):
        if len(self) > 0:
            count = 0
            current = self._head
            final = self._tail
            while current.prev != final:
                if current.elem < k:
                    nodo = DNode(current.elem)
                    nodo.prev = self._tail
                    self._tail.next = nodo
                    self._tail = nodo
                    count += 1
                current = current.next

            return count

    def removeSmaller(self, x):
        current = self._head
        while current:
            next_node = current.next  # Guardar la referencia al siguiente nodo
            if current.elem < x:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self._head = current.next  # Actualizar cabeza si se elimina el primero

                if current.next:
                    current.next.prev = current.prev
                else:
                    self._tail = current.prev  # Actualizar cola si se elimina el último
            current = next_node  # Avanzar al siguiente nodo

if __name__ == '__main__':
    l = DList2()
    l.addLast(41)
    l.addLast(12)
    l.addLast(30)
    l.addLast(6)
    l.addLast(21)
    l.addLast(1)

    print(l)
    #print("Number duplicates:", l.add_duplicates_last(3))
    print(l)

    print("Lista original:", l)
    l.removeSmaller(3)
    print("Lista después de removeSmaller(3):", l)
