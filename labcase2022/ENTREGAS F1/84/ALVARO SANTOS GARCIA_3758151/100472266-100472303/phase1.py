# -*- coding: utf-8 -*-

'''
Fase_1
@author: Ricardo y Álvaro
@date: 21-2.22
'''

from slist import SList


class SList2(SList):

    # Función que suma los últimos n números
    def sumLastN(self, n):
        result = 0
        # Si n es menor a 0 se ignora
        if n < 0:
            result = None
        # Si n es igual a 0 se devuelve 0
        elif n == 0:
            result = 0
        else:
            # Elegimos cuantos pasos tenemos que dar para llegar a las posiciones que queremos
            if n < len(self):
                steps = len(self) - n
            else:
                steps = 0
            # Bucle for para recorrer la lista y sumar los ultimos n números
            aux = self._head
            for i in range(len(self)):
                if i >= steps:
                    result += aux.elem
                aux = aux.next
        return result

    # Función que inserta un elemento en medio de una lista enlazada
    def insertMiddle(self, elem):
        # Si la lista esta vacía simplemnete se añade el elemento
        if self.isEmpty():
            self.addLast(elem)
        else:
            # Buscamos el medio en función si es par o impar
            if len(self) % 2 == 0:
                mid = len(self) // 2
            else:
                mid = (len(self) + 1) // 2
            # Recorremos la lista hasta llegar al medio
            previous = self._head
            for i in range(mid - 1):
                previous = previous.next
            # Introducimos el elemento
            newList = SList()
            newList.addLast(elem)
            newList._head.next = previous.next
            previous.next = newList._head
            self._size += 1

    # Funcion que inserta una lista en otra entre dos posiciones
    def insertList(self, inputList, start, end):
        # Con esta condición nos deshacemos de incoherencias
        if start < 0 or end < start or end >= len(self):
            print("Error")
        else:
            # Buscamos la posicion en donde vamos a conectar el incio de la lista
            aux1 = self._head
            for i in range(start - 1):
                aux1 = aux1.next
            # Buscamos la posicion en donde vamos a conectar el final de la lista
            aux2 = self._head
            for i in range(end + 1):
                aux2 = aux2.next
            # Buscamos el último elemento de la lista a insertar
            final_input = inputList._head
            for i in range(inputList.__len__() - 1):
                final_input = final_input.next
            # Introducimos la lista
            if start == 0:
                self._head = inputList._head
            else:
                aux1.next = inputList._head
            final_input.next = aux2

    # Función que cada k elementos se invierte respecto la original
    def reverseK(self, k):
        listaAux = SList2()
        listaAux2 = SList2()
        primera = True
        size2 = 0
        tail = None
        aux2 = None
        aux = self._head
        size = len(self)
        # Si queremos invertir elemento a elemento la lista se queda sin modificar
        if k <= 1:
            print("no cambia nada")
        else:
            # Bucle que finaliza cuando el tamaño de la lista auxiliar 2 es igual al original
            while size2 != size:
                # Añadimos k elementos a la lista auxiliar 1 mediante addFirst y nos quedamos el ultimo nodo
                listaAux.addFirst(aux.elem)
                if listaAux._size == 1:
                    aux2 =listaAux._head
                # Cuando la lista 1 alcanza el tamaño de k la intruducimos en la lista 2 y la borramos
                if listaAux._size == k:
                    # Se ejecuta cuando la lista 2 esta vacia
                    if primera == True:
                        listaAux2._head = listaAux._head
                        primera = False
                        tail = aux2
                    else:
                        tail.next = listaAux._head
                        tail = aux2
                    size2 += k
                    listaAux._head = None
                    listaAux._size = 0
                # Condición que se ejecuta cuando k es mayor al tamaño de la lista
                elif aux.next == None:
                    if primera == True:
                        listaAux2._head = listaAux._head
                    else:
                        tail.next = listaAux._head
                    size2 = size
                # Nos movemos por la lista original
                if aux.next != None:
                    aux = aux.next
            # Decimos que la lista original es la segunda lista auxiliar
            self._head = listaAux2._head

    # Función que devulve el valor máximo de la suma de elementos equidistantes en una lista
    def maximumPair(self):
        max = 0
        listaAux1 = SList2()
        fin1 = self._head
        listaAux2 = SList2()
        listaAux3 = SList2()
        # Si la lista esta vacía no devolvemos nada
        if self.isEmpty():
            max = None
        else:
            # En caso de que la lista sea impar cogemos el elemento del medio y lo elimnamos para que sea impar
            if len(self) % 2 != 0:
                max = self.removeAt((len(self) + 1) // 2 - 1)

            # Cabe la posibilidad que al eliminar el elemento del medio la lista quede vacía
            if self.isEmpty() == False:
                # Buscamos los dos elementos del medio de una lista
                for x in range(0,(len(self)//2) - 1):
                    fin1 = fin1.next
                # A continuación separamos la lista en dos del mismo tamaño
                inicio2 = fin1.next
                listaAux2._head = inicio2
                listaAux1._head = self._head
                fin1.next = None

                # Invertimos la segunda lista
                aux1 = listaAux2._head
                while aux1 != None:
                    listaAux3.addFirst(aux1.elem)
                    aux1 = aux1.next

                # Sumamos los elementos de cada lista que se encuentren en la misma posición
                aux1 = listaAux1._head
                aux2 = listaAux3._head
                while aux1 != None:
                    suma = aux1.elem + aux2.elem
                    if suma > max:
                        max = suma
                    aux1 = aux1.next
                    aux2 = aux2.next

        return max