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


if __name__ == '__main__':
    l = DList2()
    l.addLast(4)
    l.addLast(1)
    l.addLast(3)
    l.addLast(1)
    l.addLast(2)
    l.addLast(1)

    print(l)
    print("Number duplicates:", l.add_duplicates_last(3))
    print(l)
