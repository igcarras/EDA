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
        # now, we must update the tail reference
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
        #En la clase MySList, completa la función subtraction (other), que recibe
#una lista “other”.
#La función debe restar el valor de las posiciones iguales de cada lista (lista invocante
#y lista other), almacenando en una nueva lista el resultado de la resta para cada
#posición. No se admiten valores negativos, por tanto, debe almacenarse el valor
#absoluto de la resta. Las listas pueden tener diferente tamaño o estar vacías.
#La función devuelve la nueva lista generada. Si alguna de las listas no está ordenada
#la función devolverá None.

        lista = MySList()
        resultado = 0
        nuevoResultado  = 0
        if self.isSorted() and other.isSorted():
            nodo_other = other._head
            nodo_lista = self._head
            while nodo_lista and nodo_other:
                nodo_lista = nodo_lista.next
                nodo_other = nodo_other.next
                if nodo_other == None and nodo_lista == None:
                    return lista
                else:
                    resultado = nodo_lista.elem - nodo_other.elem
                    nuevoResultado = resultado * -1
                    lista.append(nuevoResultado)

                return lista
        else:
            return None

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
