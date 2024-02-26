"""Fase 1 , trabajo en grupo Pablo Albendea Obispo y Daniel Gómez Magro."""

from slist import SList
from slist import SNode
import sys

class SList2(SList):


#función que toma un número entero n y devuelve la suma de
#los n últimos nodos de la lista invocante. Si n<0, la función debe devolver None.
    def sumLastN(self, n):
        nodeIt = self._head
        suma = 0
        if n < 0:
            suma = None
        else:
            if self._size == 0:
                suma = 0
            elif n >= self._size:
                while nodeIt.next != None:
                    suma += nodeIt.elem
                    nodeIt = nodeIt.next
                suma += nodeIt.elem
            else:
                cont = 0
                while self._size - n > cont:
                    nodeIt = nodeIt.next
                    cont += 1
                while nodeIt.next != None:
                    suma += nodeIt.elem
                    nodeIt = nodeIt.next
                suma += nodeIt.elem
        return suma
    
    #method for inserting a new node in the middle
    def insertMiddle(self, elem):

        newNode = SNode(elem)
        contador = 0
        node = self._head
        if len(self)==0:
            self._head = newNode
        else:
            while contador < len(self) / 2 -1:
                node = node.next
                contador+= 1
            #el menos 1 es para que tenga en cuenta que existe la posicion 0
            newNode.next = node.next
            node.next = newNode


    def insertList(self, inputList, start, end):
        # Pide una lista y dos posiciones de la que ya tengo,
        # elimina todo lo que hay entre esas dos pos (incluidas) y mete los elementos de la lista que ha metido
        nodestart = self._head
        nodeend = self._head
        if start >= 0 and start <= end and inputList._size > 0:
            ninputstart = inputList._head
            ninputend = ninputstart
            if self._size == 0:
                self._head = ninputstart
            else:
                if inputList._size >= 2:
                    while ninputend.next != None:
                        ninputend = ninputend.next
                if end == self._size - 1:
                    nodeend = ninputend
                if end != 0:
                    for i in range(end + 1):
                        if nodeend.next != None:
                            nodeend = nodeend.next
                else:
                    nodeend = nodestart.next
                # Ya tengo un puntero en cada extremo de la lista input y
                if start == 0:
                    self._head = inputList._head
                else:
                    for i in range(start - 1):
                        nodestart = nodestart.next
                    nodestart.next = ninputstart
                if nodeend != ninputend:
                    ninputend.next = nodeend
        else:
            return

    def reverseK(self, k):
        # Tengo que hacer 4 tipos,uno si k = len; otro si k es 1 o 0; y otras dos si son pares o impares
        # Me apoyo en dos listas auxiliares para ir introduciendo los grupos ordenados
        longitud = len(self)
        Auxlist1 = SList()
        Auxlist2 = SList()
        nodeit = self._head
        nodehelp = Auxlist1._head

        if k <= 1 :
            # En este caso no hay que invertir ni hacer nada
            return self
        elif k > 1 and k < len(self):
            # usamos una lista auxiliar en el que metemos los elementos de uno en uno con Add first
            # cuando len de esta llega a k , hacemos add last a cada elemento en Aux2 y vaciamos Aux1
            #Finalmente pones el self._head en el _head de aux 2
            while nodeit and len(Auxlist2) != longitud:
                Auxlist1.addFirst(nodeit.elem)
                nodeit = nodeit.next

                if len(Auxlist1) == k:
                    nodehelp = Auxlist1._head
                    for i in range(len(Auxlist1)):
                        Auxlist2.addLast(nodehelp.elem)
                        nodehelp = nodehelp.next
                    Auxlist1._head = None
                    Auxlist1._size = 0

            if len(Auxlist2) != longitud:
                nodehelp = Auxlist1._head
                if nodehelp != None:
                    for i in range(len(Auxlist1)):
                        Auxlist2.addLast(nodehelp.elem)
                        nodehelp = nodehelp.next
                    Auxlist1._head = None
                    Auxlist1._size = 0
            self._head = Auxlist2._head

        else:
            k = len(self)
            while nodeit and len(Auxlist2) != longitud:
                Auxlist1.addFirst(nodeit.elem)
                nodeit = nodeit.next
                if len(Auxlist1) == k:
                    nodehelp = Auxlist1._head
                    if nodehelp != None:
                        for i in range(len(Auxlist1)):
                            Auxlist2.addLast(nodehelp.elem)
                            nodehelp = nodehelp.next
                        Auxlist1._head = None
                        Auxlist1._size = 0

            self._head = Auxlist2._head



    def maximumPair(self):
        nodeIt = self._head
        node2 = self._head
        cont = 1
        suma = 0
        suma_max = 0
        # Hago todos los casos y si es impar lo compruebo con el que falta
        if self._size >= 2:
            for a in range(self._size // 2):
                node2 = self._head
                for i in range(int(self._size) - cont):
                    node2 = node2.next
                cont += 1
                suma = nodeIt.elem + node2.elem
                nodeIt = nodeIt.next
                if suma > suma_max:
                    suma_max = suma
            if self._size % 2 != 0:
                if nodeIt.elem > suma_max:
                    suma_max = nodeIt.elem
        elif self._size == 1:
            suma_max = self._head.elem
        else:
            suma_max = None
        return suma_max
 