#Ignacio Tordable y Eduardo Faro
from slist import SList
from slist import SNode
import sys
import math

class SList2(SList):

    def sumLastN(self, n):
        if self.isEmpty():
            print("Error: list is empty")
            return 0
        else:
            if n < 0:
                return None
            elif n > self._size:
                suma = 0
                for a in range(self._size):
                    ultimo = self.getAt(a)
                    suma += ultimo
                return suma
            else:
                suma = 0
                for a in range(n):
                    ultimo = self.getAt(self._size - a - 1)
                    suma += ultimo
                return suma

    # method for inserting a new node in the middle
    def insertMiddle(self, elem):
        if self._size % 2 == 0:
            index = self._size // 2
        else:
            index = (self._size // 2) + 1
        if self.isEmpty():
            self.addFirst(elem)
        else:
            nodeIt = self._head
            siguiente = nodeIt.next
            i = 1
            while nodeIt and i < index:
                nodeIt = nodeIt.next
                siguiente = siguiente.next
                i += 1
            newNode = SNode(elem)
            nodeIt.next = newNode
            newNode.next = siguiente
            self._size += 1

    def insertList(self, inputList, start, end):
        if 0 <= start <= end < len(self):
            current = self._head
            for a in range(start - 1):
                current = current.next
            current3 = self._head
            for a in range(end + 1):
                current3 = current3.next
            current2 = inputList._head
            while current2.next:
                current2 = current2.next
            if start != 0:
                current.next = inputList._head
            else:
                self._head = inputList._head
            current2.next = current3
            self._size -= end - start + 1
            self._size += inputList._size
        elif end == -1 and start == -1: #para poder añadir al final sin eliminar nada
            if self._head:
                current = self._head
                while current.next:
                    current = current.next
                current.next = inputList._head
            else:
                self._head = inputList._head
            self._size += inputList._size
        else:
            print("Error: la mínima posición es 0 y la máxima posición es: len(lista) - 1")

    def reverseK(self, k):
        nuevaLista = SList2()
        resultado = len(self) // k
        for a in range(resultado):
            nuevaLista2 = SList2()
            for b in range(k):
                nuevaLista2.addFirst(self.getAt(0 + b + a*k))
            nuevaLista.insertList(nuevaLista2, -1, -1)
        resto = len(self) % k
        if resto != 0:
            nuevaLista2 = SList2()
            for b in range(resto):
                nuevaLista2.addFirst(self.getAt(resultado*k + b))
            nuevaLista.insertList(nuevaLista2, -1, -1)
        self.insertList(nuevaLista, 0 , len(self) - 1)

    def maximumPair(self):
        if len(self) > 0:
            max = 0
            for a in range(self._size // 2):
                suma = self.getAt(0 + a) + self.getAt(self._size - 1 - a)
                if suma > max:
                    max = suma
            if self._size % 2 != 0:
                medio = self.getAt(self._size // 2) # 5 / 2 = 2,5 = 2 = posición del medio si se empiza por 0
                if medio > max:
                    max = medio
            return max
        else:
            return None

s = SList2()
s.addLast(10)
s.addLast(2)
s.addLast(40)
s.addLast(8)
s.addLast(9)
#s.insertMiddle(4)
print(s)
print(s._size)
p = SList2()
p.addLast(99)
p.addLast(88)
#s.insertList(p, 0, 5)
print(s)
#print(s._size)
s.reverseK(3)
print(s)
print(s.maximumPair())