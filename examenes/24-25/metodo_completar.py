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

    print("Lista original:", slist)
    slist.completar()
    print("Lista después de mover duplicados al final:", slist)