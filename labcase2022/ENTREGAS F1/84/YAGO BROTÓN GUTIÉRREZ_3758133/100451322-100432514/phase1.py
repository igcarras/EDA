from slist import SList, SNode
import sys


class SList2(SList):

    def sumLastN(self, n):
        if n < 0:
            return None
        elif n == 0 or self.isEmpty():
            return 0
        else:
            aux = 0
            nodo = self._head
            if n >= self._size:
                for i in range(self._size):
                    aux += nodo.elem
                    nodo = nodo.next
            else:
                for i in range(self._size - n):
                    nodo = nodo.next
                for j in range(n):
                    aux += nodo.elem
                    nodo = nodo.next
            return aux

    def insertMiddle(self, elem):

        if self.isEmpty() or (self._size == 1): # Usamos directamente, addLast.
            self.addLast(elem)
        else:
            nodo_aux = self._head
            if (self._size % 2) == 0:
                n = self._size//2
            else:
                n = (self._size + 1)//2

            for i in range(n-1):
                nodo_aux = nodo_aux.next

            newNode = SNode(elem)
            newNode.next = nodo_aux.next
            nodo_aux.next = newNode
            self._size += 1

    def insertList(self, inputList, start, end):
        if len(inputList)  == 0:
            return
        if (start > end) or (start < 0) or (end >= len(self)):
            print('Error: los parametros no son correctos')

        else:

            newList = SList2()
            nodo1 = self._head
            nodo2 = inputList._head
            nodoInsert = newList._head
            while nodo2:
                newNode = SNode(nodo2.elem)

                if newList._head is None:
                    newList._head = newNode
                    nodoInsert = newNode
                else:
                    nodoInsert.next = newNode
                    nodoInsert = nodoInsert.next

                self._size += 1
                nodo2 = nodo2.next

            final = newList._head
            while final.next:
                final = final.next
            tail = nodo1.next

            for i in range(start-1):
                nodo1 = nodo1.next
            for i in range(end):
                tail = tail.next
            nodo1.next = newList._head
            final.next = tail

            if start == 0:
                self._head = self._head.next

            print(self)



    def reverseK(self, k):
        if k <= 1:
            return
        elif k >= len(self):
            prev = None
            nodo_aux = self._head
            while nodo_aux:
                next = nodo_aux.next
                nodo_aux.next = prev
                prev = nodo_aux
                nodo_aux = next
            self._head = prev
        else:
            temp = SNode(None)
            temp.next = self._head
            curr = self._head
            lastPrev = temp
            lastCurr = curr
            cont = k
            while curr:
                prev = None
                while cont > 0 and curr:
                    next = curr.next
                    curr.next = prev
                    prev = curr
                    curr =next
                    cont -= 1
                lastPrev.next = prev
                lastCurr.next = curr
                lastPrev = lastCurr
                lastCurr = curr
                cont = k
            self._head = temp.next

    def maximumPair(self):
        if self.isEmpty():
            return None

        maximo = 0
        listaInv = SList2()

        nodo_aux = self._head
        n = 0 # Contamos el número de iteraciones
        par = (len(self) % 2) == 0
        while nodo_aux:
            prev = listaInv._head
            if (not par) and (n == (len(self) // 2)):  # Si la longitud de la lista es impar y estamos en el centro
                nodoInv = SNode(0) #  Insertamos un 0, así al sumar, el elemento central no cuenta doble
            else:
                nodoInv = SNode(nodo_aux.elem)
            nodoInv.next = prev
            nodo_aux = nodo_aux.next
            listaInv._head = nodoInv
            listaInv._size += 1
            n += 1

        nodo1 = self._head
        nodo2 = listaInv._head
        while nodo1 and nodo2:
            suma = nodo1.elem + nodo2.elem
            maximo = max(maximo, suma)
            nodo1 = nodo1.next
            nodo2 = nodo2.next
        return maximo
