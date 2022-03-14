"""Nerea De Vicente Serrano. Grupo 801. NIU: 100475386"""


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

        #Comprobamos que está ordenada
        if other.isSorted() and self.isSorted():
            #Creamos nueva lista que almacene resultados
            salida= MySList()
            #Creamos dos varaibles que recorren la lista l2 y other
            a = self._head
            b = other._head

            #Bucle que recorre las listas mientras tengan mismo tamaño
            while a and b:
                #La resta de los elementos, comparamos tamaño para que sea
                # valor absoluto
                if a.elem > b.elem:
                    NuevoElem= a.elem -b.elem
                else:
                    NuevoElem = b.elem - a.elem

                #Añadimos nuevo nodo a nuestra lista creada
                salida.append(NuevoElem)


                #Que pasen las variables al siguiente nodo de la lista
                a = a.next
                b = b.next

            #Que siga añadiendo los términos cuando la lista invocante es
            # más larga
            while a:
                salida.append(a.elem)
                a = a.next
            #Que siga añadiendo los terminos cuando la lista other es más larga
            while b:
                salida.append(b.elem)
                b= b.next

            return salida

        #Si una de las dos no está ordenada devuelve None
        else:
            return None


"""En la clase MySList, completa la función subtraction (other), que recibe una lista “other”.
La función debe restar el valor de las posiciones iguales de cada lista (lista invocante y lista other), almacenando en una nueva lista el resultado de la resta para cada posición. No se admiten valores negativos, por tanto, debe almacenarse el valor absoluto de la resta. Las listas pueden tener diferente tamaño o estar vacías.
La función devuelve la nueva lista generada. Si alguna de las listas no está ordenada la función devolverá None.
A continuación, tienes algunos ejemplos:


Lista invocante
[3, 4, 9, 10] [1,6,7,8,9,10] [3, 4, 9, 10] [6,1,7,9,3,10] [1,6,7,8,9,10] [3, 4, 9, 10]
(lista vacía) (lista vacía)"""



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

