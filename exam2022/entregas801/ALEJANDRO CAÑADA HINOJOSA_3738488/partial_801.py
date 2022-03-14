# coding=utf-8
# #ALEJANDRO CAÑADA HINOJOSA (100431297)
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
    #ALEJANDRO CAÑADA HINOJOSA (100431297)
    def subtraction(self, other):
        "Subtraction of elements in two ordered lists."
        result = MySList()
        #Si las dos listas están vacias retornamos result empty
        if(self._head==None and other._head==None):
            #print("ambas listas están vacias")
            return result
        #chequear que las listas está ordenada
        #si no está ordenada alguna retorno None
        if(self.isSorted()==False):
            #print("list SELF no está ordenada")
            return None
        if(other.isSorted()==False):
            #print("list OTHER no está ordenada")
            return None
        #print("both lists are sorted")
        #Ahora que ya sabemos que las listas están ordenadas y que por lo menos una no está vacia, procedemos a hacer la suma

        #Lo primero de todo, con dos punteros auxialres seleccionamos las cabezas de ambas listas
        aux1=self._head
        aux2=other._head

        #En el caso de que una lista esté vacia, retornamos la que no está vacia
        if self._head==None:
            while aux2!=None:
                result.append(aux2.elem)
                aux2=aux2.next
            #print("SELF is empty")
            #print(result)
            return result
        #Repetimos el mismo proceso para la otra lista
        if other._head==None:
            while aux1!=None:
                result.append(aux1.elem)
                aux1=aux1.next
            #print("OTHER is empty")
            #print(result)
            return result
        #Ahora vamos con el último caso (las listas están ordenadas y ninguna lista está vacia)
        #Haremos un loop hasta que lleguemos al final de ambas listas
        while aux1!=None or aux2!=None:
            #En el caso de que ya hallamos llegado al final de la PRIMERA lista, nos limitamos a hacer append() de los elementos de la otra
            if(aux1==None):
                result.append(abs(aux2.elem))
                aux2=aux2.next
                continue
            #En el caso de que ya hallamos llegado al final de la SEGUNDA lista, nos limitamos a hacer append() de los elementos de la otra
            if(aux2==None):
                result.append(abs(aux1.elem))
                aux1=aux1.next
                continue
            #En caso de que halla valores en los dos, hacemos una resta con valor absoluto
            result.append(abs(aux1.elem-aux2.elem))
            aux1=aux1.next
            aux2=aux2.next

        #print(result)
        return result
        

import random

if __name__ == '__main__':
    # Please, uncomment the code for test each function
    l2 = MySList()

    for i in range(12):
        # l2.append(random.randint(0, 20))
        l2.append(i)
    print(l2)

    l3 = MySList()
    for i in range(10):
        l3.append(i)
    l3.subtraction(l2)
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



