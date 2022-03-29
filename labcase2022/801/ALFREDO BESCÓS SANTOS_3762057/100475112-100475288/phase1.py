from slist import SList
from slist import SNode
import sys


class SList2(SList):

    def sumLastN(self, n):
        contador = self._head
        suma = 0
        if self.isEmpty():
            return (0)
        elif n > 0:
            if n > len(self):
                n = len(self)
            contador = self._head
            suma = 0
            for i in range(len(self)-n):
                contador = contador.next
            for i in range(n):
                e = contador.elem
                suma += e
                contador = contador.next
            return(suma)
        else:
            return None
        ...

    # method for inserting a new node in the middle
    def insertMiddle(self, elem):
        newNode = SNode(elem)
        if self.isEmpty():
            self.addFirst(elem)
        else:
            pos = 0
            previous = self._head
            siguiente = self._head
            if ((len(self)) % 2) == 0:
                pos = (len(self))//2
            else:
                pos = (len(self)+1)//2
            for i in range(pos-1):
                previous = previous.next
            for i in range(pos):
                siguiente = siguiente.next
            previous.next = newNode
            newNode.next = siguiente
        ...

    def insertList(self, inputList, start, end):
        if 0 <= start <= end < len(self):
            previous = self._head
            for i in range(start-1):
                previous = previous.next
            sucesor = self._head
            for i in range(end+1):
                sucesor = sucesor.next
            primero = inputList._head
            while primero.next:
                primero = primero.next
            if start > 0:
                previous.next = inputList._head
            else:
                self._head = inputList._head
            primero.next = sucesor
            self._size -= (end-start)
            self._size += len(inputList)
        else:
            print('los parámetros no cumplen los requerimientos básicos')
        ...

    def reverseK(self, k):
        Aux1 = SList2()
        numCambios = len(self)//k
        for i in range(numCambios):
            Aux2 = SList2()
            for j in range(k):
                Aux2.addFirst(self.getAt(j+i*k))
            for j in range(k):
                Aux1.addLast(Aux2.getAt(j))
        resto = len(self) % k
        if resto > 0:
            Aux2 = SList2()
            for i in range(resto):
                Aux2.addFirst(self.getAt(numCambios*k+i))
            for j in range(resto):
                Aux1.addLast(Aux2.getAt(j))
        self.insertList(Aux1, 0, len(self)-1)
        ...

    def maximumPair(self):
        if self.isEmpty():
            return None
        lastNode = self._head
        suma = 0
        maximo = 0
        nmedio = self._head
        if len(self) == 1:
            e = lastNode.elem
            return(e)
        else:
            if len(self) % 2 != 0:
                for i in range(len(self)//2):
                    nmedio = nmedio.next
                if nmedio.elem > maximo:
                    maximo = nmedio .elem
            for n in range(len(self)//2):
                first = lastNode.elem
                last = self.getAt((len(self)-n-1))
                suma = first + last
                if suma > maximo:
                    maximo = suma
                    suma = 0
                lastNode = lastNode.next

            return maximo
        ...
