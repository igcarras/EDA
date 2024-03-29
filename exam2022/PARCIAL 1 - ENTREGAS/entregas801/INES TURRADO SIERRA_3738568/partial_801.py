# coding=utf-8
class SNode:
    def __init__(self, e, next=None):
        self.elem = e
        self.next = next


class MySList():

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __str__(self):
        """Returns a string with the elements of the list"""
        ###This functions returns the same format used
        ###by the Python lists, i.e, [], ['i'], ['a', 'b', 'c', 'd']
        ###[1], [3, 4, 5]
        nodeIt = self._head
        result = '['
        while nodeIt:
            result += str(nodeIt.elem) + ", "
            nodeIt = nodeIt.next

        if len(result) > 1:
            result = result[:-2]

        result += ']'
        return result

    def __len__(self):
        return self._size

    def append(self, e):
        """Adds a new element, e, at the end of the list"""
        # create the new node
        newNode = SNode(e)
        # the last node must point to the new node
        # now, we must update the _tail reference
        if self._head == None:
            self._head = newNode
        else:
            self._tail.next = newNode

        self._tail = newNode

    def isSorted(self):
        "returns True if self is sorted"
        if self._head == None:
            return True
        else:
            node1 = self._head
            node2 = node1.next
            while node2:
                if node1.elem > node2.elem:
                    return False
                node1 = node2
                node2 = node2.next

        return True

    def subtraction(self, other):
        "Subtraction of elements in two ordered lists."
        noteIt = self._head
        nuevalista = []
        contador = 0
        if self.isSorted() == False or other.isSorted() == False:
            return None
        else:
            if len(self) == 0:
                return other
            elif len(other) == 0:
                for h in range(len(self)):
                    nuevalista.append(noteIt.elem)
                    noteIt = noteIt.next
                return nuevalista

            elif len(self) == 0 and len(other) == 0:
                print("Lista vacía")
            else:
                while noteIta:
                    numero = noteIt.elem - other[contador]
                    if numero < 0:
                        numero = numero // (-1)
                        nuevalista.append(numero)
                    else:
                        nuevalista.append(numero)
                    contador += 1
                    noteIt = noteIt.next
                if len(self) != len(other):
                    if len(self) > len(other):
                        for j in range(len(self)-len(other)):
                            nuevalista.append(noteIt)
                            noteIt = noteIt.next
                    else:
                        for l in range(len(other)- len(self)):
                            nuevalista.append(other[contador:])
        return nuevalista








import random

if __name__ == '__main__':
    # Please, uncomment the code for test each function
    l2 = MySList()

    for i in range(10):
        l2.append(random.randint(0, 20))
    print(l2)

    l3 = MySList()
    for i in range(10):
        l3.append(i)

    print('l2:', str(l2))
    print('l3:', str(l3))

    print("List subtraction:", str(l2.subtraction(l3)))
    print("List subtraction:", str(l3.subtraction(l2)))

    data = []
    for i in range(5):
        x = random.randint(0, 10)
        if x not in data:
            data.append(x)

    data.sort()
    l2 = MySList()
    for x in data:
        l2.append(x)

    data = []
    for i in range(7):
        x = random.randint(0, 10)
        if x not in data:
            data.append(x)

    data.sort()
    l3 = MySList()
    for x in data:
        l3.append(x)

    print('l2:', str(l2))
    print('l3:', str(l3))
    print("List subtraction:", str(l2.subtraction(l3)))
    print("List subtraction:", str(l3.subtraction(l2)))
