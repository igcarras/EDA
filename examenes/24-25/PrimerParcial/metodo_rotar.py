from dlist import DList
from dlist import DNode


class DList2(DList):
    def rotar(self, p):
        if self._size <= 1 or p <= 0 or p >= self._size:
            return  # No es necesario girar

        # Encontrar el nuevo head después de girar
        current = self._head
        for _ in range(p - 1):
            current = current.next

        new_head = current.next
        new_tail = current

        # Actualizar la nueva cabeza y cola
        new_head.prev = None
        new_tail.next = None

        self._tail.next = self._head
        self._head.prev = self._tail

        self._head = new_head
        self._tail = new_tail

    def rotarv2(self, p):
        if self._size <= 1 or p <= 0 or p >= self._size:
            return  # No es necesario girar

        # Encontrar el nuevo head después de girar
        current = self._head
        for _ in range(p):
            self._head.prev=self._tail
            self._tail.next = self._head
            self._head = self._head.next
            self._head.prev.next = None
            self._head.prev = None
            self._tail = self._tail.next

    def rotarv3(self, p):
        if self._size > 1:
            while p > 0:
                p -= 1
                newNode = self._head

                self._head = self._head.next
                self._head.prev = None

                newNode.next = None
                newNode.prev = self._tail
                self._tail.next = newNode

                self._tail = newNode


if __name__ == '__main__':
    l = DList2()
    l.addLast(3)
    l.addLast(4)
    l.addLast(5)
    l.addLast(1)

    print(l)
    l.rotar(1)
    print("New DList con p=1:", l)

    l = DList2()
    l.addLast(3)
    l.addLast(4)
    l.addLast(5)
    l.addLast(1)
    print(l)
    l.rotar(3)
    print("New DList con p=3:", l)

    l = DList2()
    l.addLast(1)
    l.addLast(2)
    l.addLast(3)
    l.addLast(7)
    print(l)
    l.rotar(2)
    print("New DList con p=2:", l)

    l = DList2()
    print(l)
    l.rotar(2)
    print("New DList con p=2:", l)

    #---------v2----------

    print("------------------------------")

    l = DList2()
    l.addLast(3)
    l.addLast(4)
    l.addLast(5)
    l.addLast(1)

    print(l)
    l.rotarv2(1)
    print("V2 New DList con p=1:", l)

    l = DList2()
    l.addLast(3)
    l.addLast(4)
    l.addLast(5)
    l.addLast(1)
    print(l)
    l.rotarv2(3)
    print("V2 New DList con p=3:", l)

    l = DList2()
    l.addLast(1)
    l.addLast(2)
    l.addLast(3)
    l.addLast(7)
    print(l)
    l.rotarv2(2)
    print("V2 New DList con p=2:", l)

    l = DList2()
    print(l)
    l.rotarv2(2)
    print("V2 New DList con p=2:", l)

 #---------v3----------

    print("------------------------------")

    l = DList2()
    l.addLast(3)
    l.addLast(4)
    l.addLast(5)
    l.addLast(1)

    print(l)
    l.rotarv3(1)
    print("V3 New DList con p=1:", l)

    l = DList2()
    l.addLast(3)
    l.addLast(4)
    l.addLast(5)
    l.addLast(1)
    print(l)
    l.rotarv3(3)
    print("V3 New DList con p=3:", l)

    l = DList2()
    l.addLast(1)
    l.addLast(2)
    l.addLast(3)
    l.addLast(7)
    print(l)
    l.rotarv3(2)
    print("V3 New DList con p=2:", l)

    l = DList2()
    print(l)
    l.rotarv3(2)
    print("V3 New DList con p=2:", l)
