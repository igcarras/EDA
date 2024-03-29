# coding=utf-8
class SNode:
    def __init__(self, e, next=None):
        self.elem = e
        self.next = next


class MySList():

    def __init__(self):
        self._head = None
        self._tail = None

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

    def merge(self, other):
        "Merge of two ordered lists. No duplicates allowed."
        # Comprobar si están ordenadas
        if not self.isSorted():
            return None

        if not other.isSorted():
            return None

        # Si la original está vacia y la segunda llena
        if not self._head:
            if other._head:
                current = other._head
                siguiente = current.next
                while current:
                    if current.elem == siguiente.elem and siguiente.next:
                        current.next = siguiente.next
                    elif current.elem == siguiente.elem and not siguiente.next:
                        other._tail = current
                    else:
                        current = current.next

                self._head = other._head
                self._tail = other._tail

        # Si la original está vacía y la segunda también se queda igual
        # Si la original está llena
        else:
            # Original llena y segunda vacía
            if not other._head:
                current = self._head
                siguiente = current.next
                while current:
                    if current.elem == siguiente.elem and siguiente.next:
                        current.next = siguiente.next
                    elif current.elem == siguiente.elem and not siguiente.next:
                        self._tail = current
                    else:
                        current = current.next

            # Original llena y segunda llena
            else:
                current1 = self._head
                current2 = other._head

                while current2:
                    nuevoNodo = SNode(current2.elem)

                    if current1 and current2.elem > current1.elem:
                        current1 = current1.next
                    elif not current1:
                        self._tail.next = nuevoNodo
                        self._tail = nuevoNodo
                    else:
                        nuevoNodo = SNode(current2.elem)
                        if current1 == self._head:
                            nuevoNodo.next = self._head
                            self._head = nuevoNodo

                        else:
                            current1.next = nuevoNodo
                            nuevoNodo.next = current1.next

                    current2 = current2.next

                current = self._head
                siguiente = current.next
                while current:
                    if current.elem == siguiente.elem and siguiente.next:
                        current.next = siguiente.next
                    elif current.elem == siguiente.elem and not siguiente.next:
                        self._tail = current
                    else:
                        current = current.next

        return self



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

    print("List merged:", str(l2.merge(l3)))
    print("List merged:", str(l3.merge(l2)))

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
    print("List merged:", str(l2.merge(l3)))
    print("List merged:", str(l3.merge(l2)))
