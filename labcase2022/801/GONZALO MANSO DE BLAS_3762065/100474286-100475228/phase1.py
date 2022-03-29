import math

from slist import SList
from slist import SNode
import sys


class SList2(SList):

    def sumLastN(self, n):
        if n < 0: #si "n" es menor que cero devolvemos None puesto que es un valor incorrecto
            return None
        if n == 0: #si "n" devolvemos 0 puesto que no hay elementos para sumar
            return 0
        if n > 0:
            aux = self._head #puntero auxiliar
            i = 0 #contador de saltos
            suma = 0 #la suma de los últimos términos
            while aux: #recorremos la lista entera mientras que aux!=None
                if i >= len(self)-n:#mientras que el contador de saltos sea mayor que la longitud de la lista-"n" sumamos los elementos
                    suma+=aux.elem
                aux = aux.next #seguimos recorriendo la lista
                i += 1
            return suma


    # method for inserting a new node in the middle
    def insertMiddle(self, elem):
        if self.isEmpty(): #analizamos si la lista está vacía
            self.addFirst(elem)
        else:
            if len(self) % 2 == 0: #par
                posicion1 = len(self) // 2 #creamos la posicion
                # we need to reach the previous node (the node at the index-1 position)
                aux = self._head #puntero auxiliar
                for i in range(posicion1 - 1):
                    aux = aux.next
                newNode = SNode(elem)
                newNode.next = aux.next
                aux.next = newNode
                self._size += 1
            elif len(self) % 2 != 0: #impar
                posicion2 = (len(self) + 1) // 2
                previous = self._head
                for i in range(posicion2 - 1):
                    previous = previous.next
                newNode = SNode(elem)
                newNode.next = previous.next
                previous.next = newNode
                self._size += 1

    def insertList(self, inputList, start, end):
        # analizar casos imposibles
        if start > end or start < 0:
            return None
        if end >= len(self) :
            return None
        else:
            aux = self._head #puntero auxiliar
            cont = 1 #contador de saltos
            aux1 = inputList._head #puntero auxiliar objeto SList2
            if start == 0:
                self._head = inputList._head
            else:
                while aux and cont != start: #hasta que cont!=start recorremos la lista
                    aux = aux.next
                    cont += 1
                if cont == start: #hacemos que el puntero de aux apunte a la otra lista
                    aux.next = inputList._head
            while aux and cont <= end: #mientras que cont<end recorremos la lista
                aux = aux.next
                cont += 1
            while aux1.next: #recorremos la lista inputList
                aux1 = aux1.next
            aux1.next = aux.next #el ultimo nodo de inputList lo unimos con end de la lista self




    def reverseK(self, k):
        aux = self._head
        cont = 0
        indice = 0
        pos = 0
        aux_list = SList2() #lista vacía donde meteremos los valores invertidos
        while aux and cont!=k:
            aux_list.insertAt(indice, aux.elem)#introducimos los elementos de forma invertida
            cont+=1
            pos+=1
            aux = aux.next
            if cont == k: # reiniciamos el proceso
                cont = 0
                indice = pos
        self._head = aux_list._head





    def maximumPair(self):
        if self.isEmpty():
            return None
        else:
            aux = self._head
            pos = 0
            sumamax= 0
            while pos<len(self)//2: #recorremos la mitad de la lista
                suma1 = self.getAt(len(self)-pos-1) #cogemos la posicion opuesta a la posicion en la que nos encontramos
                suma = aux.elem+suma1 #sumar elementos equidistantes
                if suma > sumamax:
                    sumamax = suma
                pos+=1
                aux = aux.next
            if len(self)%2!=0: #si la lista es impar tenemos en cuenta el valor que se encuentra en la posicion central
                if aux.elem > sumamax:
                    sumamax = aux.elem
            return sumamax