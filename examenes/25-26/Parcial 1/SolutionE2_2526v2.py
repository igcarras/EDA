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
        self._size += 1

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

                return other

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
                self._size = self._size - s

                return other

            return other

        return None


def print_list(lst):
    """Print a normal doubly linked list"""
    current = lst._head
    print("size =", lst._size, "|", end=" ")
    while current is not None:
        print(current.elem, end=" ")
        current = current.next
    print()


def print_ring(lst):
    """Print a circular list"""
    if lst is None:
        print("None")
        return

    if lst._head is None:
        print("size = 0 | empty")
        return

    current = lst._head
    print("size =", lst._size, "|", end=" ")

    for _ in range(lst._size):
        print(current.elem, end=" ")
        current = current.next

    print("(circular)")


def build_list(values):
    """Helper function to build a list"""
    lst = DList()
    for v in values:
        lst.addLast(v)
    return lst


def main():
    print("\nCASE 1: s < size")
    l1 = build_list([1, 2, 3, 4, 5])
    print("Original list:")
    print_list(l1)

    s=3
    other1 = l1.ringList3(s)

    print("RingList with s=", s)
    print("Remaining list:")
    print_list(l1)

    print("Returned ring list (other):")
    print_ring(other1)

    print("\nCASE 2: s >= size")
    l2 = build_list([10, 20, 30])
    print("Original list:")
    print_list(l2)

    s=5
    other2 = l2.ringList3(s)


    print("RingList with s=", s)
    print("Remaining list:")
    print_list(l2)

    print("Returned ring list (other):")
    print_ring(other2)

    print("\nCASE 3: s == size")
    l3 = build_list([7, 8, 9])
    print("Original list:")
    print_list(l3)

    s=3
    other3 = l3.ringList3(s)
    print("RingList with s=", s)
    print("Returned ring list (other):")
    print_list(l3)

    print("Returned ring list:")
    print_ring(other3)

    print("\nCASE 4: s == 0")
    l4 = build_list([100, 200, 300])
    print("Original list:")
    print_list(l4)

    s=0
    other4 = l4.ringList3(s)
    print("RingList with s=", s)
    print("Remaining list:")
    print_list(l4)

    print("Returned ring list (other):")
    print_ring(other4)

    print("\nCASE 5: empty list")
    l5 = DList()
    print("Original list:")
    print_list(l5)

    s=2
    other5 = l5.ringList3(s)
    print("RingList with s=", s)
    print("Remaining list:")
    print_list(l5)

    print("Returned ring list (other):")
    print_ring(other5)


if __name__ == "__main__":
    main()