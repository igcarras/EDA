from dlist import DList

class DList2(DList):
    def quicksort(self):
        if self._head is None or len(self) <= 1:
            return self
        self._quicksort(self._head, self._tail)
        return self

    def _quicksort(self, inicio, fin):
        if inicio is None or fin is None or inicio == fin or inicio.prev == fin:
            return
        piv = inicio.elem
        i, j = inicio, fin
        while j.next is not i:
            while i.elem < piv:
                i = i.next
            while j.elem > piv:
                j = j.prev
            if i != j and j.next != i:
                i.elem, j.elem = j.elem, i.elem
                i = i.next
                j = j.prev
        inicio.elem, j.elem = j.elem, inicio.elem
        if inicio.next is not j.prev:
            print("recursion izq")
            print("inicio:", inicio.elem)
            print("fin:", j.prev.elem)
            self._quicksort(inicio, j.prev)
        if fin.prev is not j.next:
            print("recursion der")
            print("inicio:",j.next.elem)
            print("fin:",fin.elem)
            self._quicksort(j.next, fin)


if __name__ == "__main__":

    b = DList2()
    b.addLast(8)
    b.addLast(4)
    b.addLast(3)
    b.addLast(10)
    b.addLast(15)
    b.addLast(1)
    b.addLast(9)
    b.addLast(13)
    print(b)
    b.quicksort()
    print(b)





