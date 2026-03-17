class DNode:
    def __init__(self, e, n=None, p=None):
        self.elem = e
        self.next = n
        self.prev = p


class DList:
    def __init__(self):
        """creates an empty list"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        """Checks if the list is empty"""
        return len(self) == 0

    def addLast(self, e):
        """Add a new elem, e, at the end of the list"""
        newNode = DNode(e)

        if self.isEmpty():
            self._head = newNode
        else:
            newNode.prev = self._tail
            self._tail.next = newNode

        self._tail = newNode
        self._size = self._size + 1

    def ringList3(self, s):
        if self._size > 0:
            other = DList()

            if s >= self._size:
                other._head = self._head
                other._tail = self._tail
                other._size = self._size

                other._tail.next = other._head
                other._head.prev = other._tail

                self._head = None
                self._tail = None
                self._size = 0

                #return other

            elif s > 0:
                current = self._head
                i = 1
                while i < s:
                    current = current.next
                    i += 1

                other._head = self._head
                other._tail = current

                self._head = current.next
                self._head.prev = None

                other._tail.next = other._head
                other._head.prev = other._tail

                other._size = s
                self._size  = self._size - s

                #return other

            return other

        return


def print_list(lst):
    """Imprime una lista doblemente enlazada normal"""
    current = lst._head
    print("size =", lst._size, end=" | ")
    while current is not None:
        print(current.elem, end=" ")
        current = current.next
    print()


def print_ring(lst):
    """Imprime una lista circular recorriendo exactamente _size nodos"""
    if lst is None:
        print("None")
        return

    if lst._head is None:
        print("size = 0 | empty")
        return

    current = lst._head
    print("size =", lst._size, end=" | ")
    for _ in range(lst._size):
        print(current.elem, end=" ")
        current = current.next
    print("(ring)")


def build_list(values):
    lst = DList()
    for x in values:
        lst.addLast(x)
    return lst


def main():
    print("CASO 1: s < size")
    l1 = build_list([1, 2, 3, 4, 5])
    print("Lista original:")
    print_list(l1)

    other1 = l1.ringList3(3)

    print("Lista self tras ringList3(3):")
    print_list(l1)

    print("Lista other devuelta:")
    print_ring(other1)
    print("-" * 40)

    print("CASO 2: s >= size")
    l2 = build_list([10, 20, 30])
    print("Lista original:")
    print_list(l2)

    other2 = l2.ringList3(5)

    print("Lista self tras ringList3(5):")
    print_list(l2)

    print("Lista other devuelta:")
    print_ring(other2)
    print("-" * 40)

    print("CASO 3: s == size")
    l3 = build_list([7, 8, 9])
    print("Lista original:")
    print_list(l3)

    other3 = l3.ringList3(3)

    print("Lista self tras ringList3(3):")
    print_list(l3)

    print("Lista other devuelta:")
    print_ring(other3)
    print("-" * 40)

    print("CASO 4: s == 0")
    l4 = build_list([100, 200, 300])
    print("Lista original:")
    print_list(l4)

    other4 = l4.ringList3(0)

    print("Lista self tras ringList3(0):")
    print_list(l4)

    print("Lista other devuelta:")
    print_ring(other4)
    print("-" * 40)

    print("CASO 5: lista vacía")
    l5 = DList()
    print("Lista original:")
    print_list(l5)

    other5 = l5.ringList3(2)

    print("Lista self tras ringList3(2):")
    print_list(l5)

    print("Lista other devuelta:")
    print_ring(other5)
    print("-" * 40)


if __name__ == "__main__":
    main()