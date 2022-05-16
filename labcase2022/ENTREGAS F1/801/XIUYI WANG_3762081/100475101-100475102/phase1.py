from slist import SList
from slist import SNode
import sys

class SList2(SList):

    def sumLastN(self, n):
        sum = 0
        if self.isEmpty():
            print("La lista está vacía.")
            return 0

        if n < 0:
            return None
        elif n == 0:
            return 0
        else:   # Cuando 0 < n <= len(self) or n > len(self)
            current = self._head
            i = 0
            while i < len(self) - n:
                current = current.next
                i += 1
            while current != None:
                sum += current.elem
                current = current.next
            return sum



    def insertMiddle(self, elem):
        if self.isEmpty():
            self.addFirst(elem)
        else:
            previous = self._head
            if len(self) % 2 == 0:
                for i in range((len(self) // 2) - 1):
                    previous = previous.next
                newNode = SNode(elem)
                newNode.next = previous.next
                previous.next = newNode
            else:
                for i in range(((len(self) + 1) // 2) - 1):
                    previous = previous.next
                newNode = SNode(elem)
                newNode.next = previous.next
                previous.next = newNode

            self._size += 1



    def insertList(self,inputList,start,end):
        if self.isEmpty():
            print("La lista está vacía")
        if start < 0 or start > len(self) or start > end or end >= len(self):
            print("Error, el rango está fuera de la lista")
        else:
            last = inputList._head
            current = self._head
            for i in range(len(inputList)-1):
                last = last.next
            for j in range(end+1):
                current = current.next

            if start == 0:
                self._head = inputList._head
                last.next = current
            else:
                previous = self._head
                for i in range(start - 1):
                    previous = previous.next
                last.next = current
                previous.next = inputList._head



    def reverseK(self,k):
        if self.isEmpty():
            print("La lista está vacía")
        if k <= 1:
            print(self)
        elif k >= len(self):
            aux = SList2()
            current = self._head
            while current:
                aux.addFirst(current.elem)
                current = current.next
            self._head = aux._head
        else:
            i = 0
            aux1 = SList2()
            aux2 = SList2()
            if len(self) % 2 == 0:
                grupo = len(self) // k
            else:
                grupo = (len(self) // k) + 1
            while i < grupo:
                current = self._head
                contador = 0
                while contador < k:
                    aux1.addFirst(self.removeFirst())
                    contador += 1
                    current = current.next

                if len(self) < k:
                    while len(self) > 0:
                        n = self.removeLast()
                        aux1.addLast(n)

                current1 = aux1._head
                for l in range(len(aux1)):
                    aux2.addLast(aux1.removeFirst())
                    current1 = current1.next
                i += 1
            self._head = aux2._head



    def maximumPair(self):
        if self.isEmpty():
            return None
        elif len(self) == 1:
            return self._head.elem
        else:
            aux = SList2()
            l = len(self)
            i = 0
            while i < (l//2):
                aux.addLast(self.removeLast())
                i += 1

            aux_suma = SList2()
            current = self._head
            currentaux = aux._head

            while current and currentaux:
                aux_suma.addLast(current.elem + currentaux.elem)
                current = current.next
                currentaux = currentaux.next

            while current: # Si la lista self es impar, se añade el último
                # elemento al final de la lista aux_suma para poder comparar.
                aux_suma.addLast(self.removeLast())
                current = current.next

            maximo = 0
            current1 = aux_suma._head
            while current1:
                if current1.elem > maximo:
                    maximo = current1.elem
                current1 = current1.next

            return maximo
