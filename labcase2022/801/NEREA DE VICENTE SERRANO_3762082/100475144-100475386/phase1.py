'''Cristina López y Nerea De Vicente, grupo 801'''

from slist import SList, SNode
import sys


class SList2(SList):

    def sumLastN(self, n):
        current = self._head
        suma = 0
        if self.isEmpty():
            return 0
        elif self.__len__() < n:
            while current:
                suma += current.elem
                current = current.next
            return suma
        elif n < 0:
            return None
        else:
            pos = self.__len__() - n
            for i in range(pos):
                current = current.next
            while current:
                suma += current.elem
                current = current.next
            return suma

    def insertMiddle(self, elem):
        current = self._head
        pos = int
        if self.isEmpty():
            self.addFirst(elem)
        else:
            if self.__len__() % 2 == 0:
                pos = len(self)//2
            elif self.__len__() % 2 != 0:
                pos = (len(self)+1)//2
            for i in range(1, pos):
                current = current.next
            newNode = SNode(elem)
            newNode.next = current.next
            current.next = newNode
        self._size += 1

    def insertList(self, inputList, start, end):
        if start >= 0 and start <= end and end < len(self):
            current1 = self._head
            current2 = self._head
            current3 = inputList._head
            for i in range(1, start):
                current1 = current1.next
            for j in range(0, end):
                current2 = current2.next
            while current3.next:
                current3 = current3.next
            if start == 0 and end == 0 or start == 0:
                current3.next = current2.next
                self._head = inputList._head
                self._size += inputList._size
            else:
                current1.next = inputList._head
                current3.next = current2.next
                eliminados = end - start + 1
                self._size -= eliminados
                self._size += inputList._size

    def reverseK(self, k):
        pos = 0
        i = 1
        currentpos = 0
        current = self._head
        current1 = self._head
        newList = SList()
        while current:
            if i*k > currentpos:
                newList.insertAt(pos, current.elem)
                current = current.next
                currentpos += 1
            else:
                i += 1
                pos += k
        current2 = newList._head
        while current2 and current1:
            current1.elem = current2.elem
            current2 = current2.next
            current1 = current1.next

    def maximumPair(self):
        if self.isEmpty():
            return None
        pos = self.__len__()//2
        suma_principio = 0
        suma_final = self.__len__()
        sumas = SList()
        while pos != 0:
            a = self.getAt(suma_principio)
            b = self.getAt(suma_final-1)
            suma = a + b
            sumas.addLast(suma)
            suma_principio += 1
            suma_final -= 1
            pos -= 1
        if (self.__len__() % 2) != 0:
            mitad = self.getAt(self.__len__()//2)
            sumas.addLast(mitad)
        for n in range((len(sumas)) - 1):
            prev = sumas._head
            current = prev.next
            if prev.elem > current.elem:
                sumas.removeAt(1)
            else:
                sumas.removeFirst()
        resultado = sumas._head
        return resultado.elem
