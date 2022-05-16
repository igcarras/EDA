from slist import SList, SNode
import sys
import math

class SList2(SList):

    def sumLastN(self, n):
        suma = 0
        if n < 0:
            return None
        elif n == 0:
            return 0
        else:
            i = self._size - n
            nodoAux = self._head
            while nodoAux:
                if i <= 0:
                    suma = suma + nodoAux.elem
                nodoAux = nodoAux.next
                i -= 1
            return suma


    
    #method for inserting a new node in the middle
    def insertMiddle(self, elem):
        if self.isEmpty():
            self.addFirst(elem)
        elif self._size%2 == 0:
            nuevoNodo = SNode(elem)
            posicion = self._size//2
            nodoAux = self._head
            i = 1
            while posicion != i:
                nodoAux = nodoAux.next
                i += 1
            next = nodoAux.next
            nodoAux.next = nuevoNodo
            nuevoNodo.next = next
            self._size += 1
        else:
            nuevoNodo = SNode(elem)
            posicion = (self._size // 2) + 1
            nodoAux = self._head
            i = 1
            while posicion != i:
                nodoAux = nodoAux.next
                i += 1
            next = nodoAux.next
            nodoAux.next = nuevoNodo
            nuevoNodo.next = next
            self._size += 1


    
    def insertList(self,inputList,start,end):
        if start >= 0 and start<=end<self._size:
            i = 0
            nodoAux = self._head
            prev = None
            nodo1 = None
            nodo2 = None
            while nodoAux.next:
                if i == start:
                    nodo1 = prev
                if i == end:
                    nodo2 = nodoAux.next
                i += 1
                prev = nodoAux
                nodoAux = nodoAux.next
            if inputList.isEmpty():
                if nodo1:
                    nodo1.next = nodo2
                else:
                    self._head = nodo2
            else:
                if nodo1:
                    nodo1.next = inputList._head
                else:
                    self._head = inputList._head
                nodoAux2 = inputList._head
                for i in range(inputList._size - 1):
                    nodoAux2 = nodoAux2.next
                nodoAux2.next = nodo2

        else:
            print("Error en los datos")


    def reverseK(self,k):
        if k <= 1:
            return None
        elif k >= self._size:
            k = self._size
            nodoAux = self._head
            prev = None
            sig = self._head.next
            while nodoAux.next:
                nodoAux.next = prev
                prev = nodoAux
                nodoAux = sig
                sig = sig.next
            nodoAux.next = prev
            self._head = nodoAux
        else:
            fin = False
            cont = k-1
            nodoAux = self._head.next
            prev = self._head
            final = self._head
            finalant = None
            sig = self._head.next.next
            while prev != nodoAux and not fin:
                nodoAux.next = prev
                prev = nodoAux
                if sig:
                    nodoAux = sig
                    sig = sig.next
                cont -= 1
                if cont == 0 or nodoAux == prev:
                    if finalant and sig:
                        finalant.next = prev
                        finalant = final
                        final = nodoAux
                    elif not sig:
                        finalant.next = prev
                        final.next = None
                        print("aaa")
                        fin = True
                    else:
                        self._head = prev
                        finalant = final
                        final = nodoAux
                    if sig:
                        sig = sig.next
                    prev = nodoAux
                    if nodoAux:
                        nodoAux = nodoAux.next
                    cont = k-1


    def maximumPair(self):

        if self.isEmpty():
            return None
        else:
            cont = 0
            nodoAux = self._head
            lista = SList2()

            while nodoAux:
                cont += 1
                if cont > self._size / 2:
                    lista.addFirst(nodoAux.elem)
                nodoAux = nodoAux.next

            nodolista = lista._head
            nodoAux = self._head
            if self._size >1:
                max = nodolista.elem + nodoAux.elem
            else:
                return nodoAux.elem

            for i in range(self._size // 2):
                if max < nodolista.elem + nodoAux.elem:
                    max = nodolista.elem + nodoAux.elem
                nodolista = nodolista.next
                nodoAux = nodoAux.next

            if self._size % 2 == 1 and max < nodolista.elem:
                max = nodolista.elem
            return max

        """max = 0
                if self.isEmpty():
                    return None
                elif self._size %2 == 0:
                    for i in range(self._size // 2):
                        nodosim = nodoAux = self._head
                        for j in range(i):
                            nodoAux = nodoAux.next
                        for j in range(self._size-i-1):
                            nodosim = nodosim.next
                        result = nodoAux.elem + nodosim.elem
                        if result > max:
                            max = result
                    return max
                else:
                    for i in range(self._size // 2):
                        nodosim = nodoAux = self._head
                        for j in range(i):
                            nodoAux = nodoAux.next
                        for j in range(self._size-i-1):
                            nodosim = nodosim.next
                        result = nodoAux.elem + nodosim.elem
                        if result > max:
                            max = result
                    nodoAux = self._head
                    for i in range(self._size//2):
                        nodoAux = nodoAux.next
                    result = nodoAux.elem
                    if result > max:
                        max = result
                    return max"""
