from slist import SList, SNode
import sys

class SList2(SList):

    def sumLastN(self, n):

        result = 0
        if self.isEmpty():
            print("Error, la lista está vacía")
            result = 0
        else:
            if n == 0:
                result = 0
            elif n < 0:
                print("Error, el número a intruducir debe ser mayor a 0")
                result = None
            elif n > 0:
                naux = self._head
                times = 0
                while naux:
                    if times >= len(self)-n:
                        result = result + naux.elem
                    times += 1
                    naux = naux.next
        return result




    
    #method for inserting a new node in the middle
    def insertMiddle(self, elem):

        node = self._head

        if self.isEmpty():
            self.addFirst(elem)

        else: #lista par
            if len(self) % 2 == 0:
                for a in range((len(self) // 2) - 1):
                    node = node.next
                node2 = SNode(elem)
                node2.next = node.next
                node.next = node2
                self._size += 1
            else: #lista impar
                for a in range((len(self) + 1) // 2 - 1):
                    node = node.next
                node2 = SNode(elem)
                node2.next = node.next
                node.next = node2
                self._size += 1

    
    def insertList(self,inputList,start,end):

        if start > end or start < 0 or end>=len(self):
            print("Error. \n Requisitos: \n "
                  "Start < End | Start > 0 | End <= Longitud de la lista")
        else:
            node = self._head
            if start > 0:
                for a in range(start-1):
                    node = node.next
            node2 = self._head
            for a in range(end):
                node2 = node2.next
            node3 = inputList._head
            while node3.next:
                node3 = node3.next
            if start > 0:
                node.next = inputList._head
            else:
                self._head = inputList._head
            node3.next = node2.next



    def reverseK(self,k):

        aux = SList2()

        if self.isEmpty():
            print("Error, la lista está vacía")
        else:

            node = self._head
            timing = 0
            position = 0
            n = 0

            while node:
                aux.insertAt(position, node.elem)
                node = node.next
                timing+=1
                n+=1
                if n == k:
                    n = 0
                    position = timing
            self._head = aux._head
        return aux



    def maximumPair(self):

        suma = None

        if self.isEmpty():
            print("Error, la lista está vacía")
            return suma

        elif len(self) == 1:
            suma = self._head.elem

        else:
            node = self._head
            timing = 0
            suma = 0

            while timing < (len(self)//2):
                fwd = node.elem
                naux = self._head
                for a in range (len(self) - 1 - timing):
                    naux = naux.next
                bck = naux.elem
                node = node.next
                total = fwd + bck
                timing+=1
                suma = max(suma, total)

            if len(self)%2 != 0:
                node2 = self._head
                for a in range(len(self)//2):
                    node2 = node2.next
                odd = node2.elem
                suma = max(suma, odd)

        return suma







