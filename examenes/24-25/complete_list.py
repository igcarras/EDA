from slistHT import SList, SNode

class SList2(SList):
    def completar(self):
        current = self._head
        while current and current.next:
            if current.elem + 1 < current.next.elem:
                new_node = SNode(current.elem + 1)
                new_node.next = current.next
                current.next = new_node
                self._size += 1  # Actualizar tamaño de la lista
            else:
                current = current.next  # Avanzar al siguiente nodo
        # Si el número de nodos es impar, añadir un nodo extra al final
        if self._size % 2 == 1:
            extra_node = SNode(self._tail.elem + 1)
            self._tail.next = extra_node
            self._tail = extra_node
            self._size += 1  # Actualizar tamaño

if __name__ == '__main__':
    slist = SList2()
    slist.add_last(1)
    slist.add_last(3)
    slist.add_last(4)

    print("Lista original:", slist)
    slist.completar()
    print("Lista después de mover duplicados al final:", slist)

    slist = SList2()
    slist.add_last(1)
    slist.add_last(5)

    print("Lista original:", slist)
    slist.completar()
    print("Lista después de mover duplicados al final:", slist)

    slist = SList2()
    slist.add_last(7)
    slist.add_last(8)
    slist.add_last(9)

    print("Lista original:", slist)
    slist.completar()
    print("Lista después de mover duplicados al final:", slist)

    slist = SList2()
    slist.add_last(2)
    slist.add_last(3)
    slist.add_last(4)
    slist.add_last(6)

    print("Lista original:", slist)
    slist.completar()
    print("Lista después de mover duplicados al final:", slist)