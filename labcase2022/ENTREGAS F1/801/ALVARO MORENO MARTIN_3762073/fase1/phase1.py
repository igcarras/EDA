from slist import SList, SNode
import sys
import time

class SList2(SList):

    def sumLastN(self, n):     #O(n)
        #Si la lista está vacía devuelve None
        if n < 0:
            return None
        
        #recorremos la lista añadiendo a la suma los valores después de la posición n
        node, suma_total, pos = self._head, 0, 0
        while node:                           
            if pos >= len(self) - n:
                suma_total += node.elem
            node = node.next
            pos += 1
        return suma_total
    
    #method for inserting a new node in the middle
    def insertMiddle(self, elem):     #O(n)
        if self.isEmpty():
            #Si la lista esta vacía lo colocamos directamente
            self.addFirst(elem)
        else:
            #elegimos la posición del valor según sea par o impar
            if len(self) % 2 == 0:
                posicion = len(self) // 2
            else:
                posicion = (len(self) +1 ) // 2
            
            #Recorremos la lista hasta la posición en cuestión
            node, x = self._head, 0
            while x < posicion -1:
                node = node.next
                x += 1
            
            #Insertamos un nuevo nodo entre los elementos
            newnode = SNode(elem)
            newnode.next = node.next
            node.next = newnode
            self._size += 1
        
    def insertList(self, inputList, start, end):     #O(n)
        if start >= 0 and end < len(self) and start <= end:           #comprobamos valores
            self.addFirst(0)   #nodo de apoyo por si el valor de start es 0
            
            #localizamos el nodo antes del primero que se borra y el que está después del ultimo que se borra
            node, nextpos = self._head, 0
            while nextpos != end+1:
                if nextpos == start:
                    startnode = node
                nextpos += 1
                node = node.next
            endnode = node.next

            #localizamos el último nodo de la lista a insertar
            inputnode = inputList._head
            while inputnode.next:
                inputnode = inputnode.next
            
            #reorganizamos los punteros para que quede la lista final
            startnode.next = inputList._head      
            inputnode.next = endnode
            
            self.removeFirst()        #eliminamos el nodo de apoyo
            self._size = self._size + inputList._size - (end-start+1)   #ajustamos el tamaño

    def reverseK(self, k):            #O(n)
        #Lista auxiliar
        nlist = SList2()
        #Nodo auxiliar que funciona como cabeza de la lista reordenda
        newhead = SNode(0)
        prevtail, node, n = newhead, self._head, 0
        
        #Recorremos la lista original
        while node:
            newnode = SNode(node.elem)
            #Introducimos el siguiente elemento como cabeza en la lista auxiliar, por lo que se colocan al revés
            if n == 0:
                tail = newnode
                nlist._head = newnode
            else:
                newnode.next = nlist._head
                nlist._head = newnode
            node = node.next
            n += 1
            
            #Cada k elementos, la lista auxiliar se añade a la anterior y se vacía
            if n == k:                
                prevtail.next = nlist._head
                prevtail = tail
                n = 0
                nlist = SList2()
        
        #Si la longitud de la lista no es múltiplo de k, algunos elementos se quedan en la auxiliar, por lo que los añadimos
        prevtail.next = nlist._head
                
        self._head = newhead.next
            
    def maximumPair(self):              #O(n)

        #Si está vacía no devuelve nada
        if self.isEmpty():
            return None
        
        #Creamos una lista que contiene los elementos a partir de la mitad colocados al revés
        node, pos = self._head, 0
        reversehalf = SList2()
        while node:
            if pos >= (len(self)+1)//2:
                reversehalf.addFirst(node.elem)
            node = node.next
            pos += 1
        
        #Comparamos la suma de los dos elementos en la misma posición de cada lista
        node1, node2 = self._head, reversehalf._head
        sumamax = 0
        while node2:
            suma = node1.elem + node2.elem
            if suma > sumamax:
                sumamax = suma
            node1 = node1.next
            node2 = node2.next
        
        #Tenemos en cuenta el elemento extra si es impar
        if len(self)%2 != 0 and node1.elem > sumamax:
            sumamax = node1.elem
            
        return sumamax
