# coding=utf-8
# #Cristina López Alcázar
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

    def subtraction(self, other):
        #comprobamos si las listas están ordenadas
        if not self.isSorted() or not other.isSorted():
            #si no lo están devuelve None
            return None
        else:
            #si están ordenadas, creamos una nueva lista
            newList = MySList()
            current1 = self._head
            current2 = other._head
            # mediante bucles while recorremos las listas
            while current1 and current2:
                #restamos los elementos de las listas
                newElem =current1.elem - current2.elem
                # mediante un if comprobamos que el número sea positivo
                if newElem < 0:
                    newElem *= -1
                #añadimos el nuevo elemento a la nueva lista
                newList.append(newElem)
                current1 = current1.next
                current2 = current2.next
            #en el caso de que las listas sean de distinto tamaño comprobamos cuál de las dos es la más larga,
            # para añadir el resto de sus elementos a la nueva lista
            while current1:
                if current1.elem < 0:
                    current1.elem *= -1
                newList.append(current1.elem)
                current1 = current1.next
            while current2:
                if current2.elem < 0:
                    current2.elem *= -1
                newList.append(current2.elem)
                current2 = current2.next
            # una vez hemos recorrido ambas listas, devolvemos la nueva lista
            return newList

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
