# coding=utf-8
# #Fermín Martínez Cintas
from unittest import result


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
        "Subtraction of elements in two ordered lists."
        ord = 0
        a = 0
        #Me acabo de dar cuenta al final de que no hay forma de localizar el len
        long1 = 0
        long2 = 0
        for e in self:
            if self._head == None:
                long1 = 0
            else:
                while self._head.next == None:
                    long +=1
                    self._head = self._head.next
        for e in self:
            if other._head == None:
                long2 = 0
            else:
                while other._head.next == None:
                    long +=1
                    other._head = other._head.next
                

        result = MySList()
        #Implemento un comprobador para saber si ambas listas están ordenadas, la primera lista la compruebo con el método is sorted y la segunda con un método propio
        if a == 0:
            if self.isSorted() == False:
                return None
            else:    
                while ord in range(0, len(other)):
                    if other[ord] > other[ord + 1]:
                        return None
                    else:
                        ord += 1
                        if other [-2] < other[-1]:
                            a += 1
        #Una vez ya comprobadas y al ver que están ordenadas hago la nueva lista creada por la resta de ambas
        else:
            max = 0
            if len(self) > len(other):
                max = len(other)
                while max != 0:
                    if self._head.elem > other._head.elem:
                        resta = self._head.elem - other._head.elem
                        result.append(resta)
                        resta = 0
                        self._head = self._head.next
                        other._head = other._head.next
                    else:
                        resta = other._head.elem - self._head.elem
                        result.append(resta)
                        resta = 0
                        self._head = self._head.next
                        other._head = other._head.next
                result._tail.next = self._head
                result._tail = self._tail                  
            else:
                max = len(self)
                while max != 0:
                    if self._head.elem > other._head.elem:
                        resta = self._head.elem - other._head.elem
                        result.append(resta)
                        resta = 0
                        self._head = self._head.next
                        other._head = other._head.next
                    else:
                        resta = other._head.elem - self._head.elem
                        result.append(resta)
                        resta = 0
                        self._head = self._head.next
                        other._head = other._head.next
                result._tail.next = self._head
                result._tail = self._tail                    

        


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
