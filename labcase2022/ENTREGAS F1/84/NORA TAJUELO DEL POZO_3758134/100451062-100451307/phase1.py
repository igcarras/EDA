from slist import SList
from slist import SNode
import sys

class SList2(SList):

    def sumLastN(self, n):
        # compruebo que n esta dentro del rango
        if n < 0:
            print(n, "no está en el rango permitido")
            return None
        if n == 0:
            print("La suma de los n=0 últimos elementos de la lista es 0 ")
            return n

        # calculo cuántos nodos tengo que recorrer antes de los n últimos
        node = self._head
        m = (len(self)) - n
        # contador
        c = 0
        sum = 0
        if n > len(self):
            # sumo todos los elementos
            node = self._head
            while node:
                sum += node.elem
                node = node.next
        else:
            while node:
                if c < m:
                    node = node.next
                    c += 1
                else:
                    sum += node.elem
                    node = node.next
        return sum

    def insertMiddle(self, elem):
        # si está vacia no puedo encontrar la posición central
        # if self.isEmpty():
        #   print('An empty list does not have middle!!!')
        #  self._head = newNode
        # posición central
        middle = len(self) // 2
        # si es impar, añado una posición
        if len(self) % 2 != 0:
            middle += 1
        if middle == 0:
            # está al inicio de la lista
            self.addFirst(elem)
        else:
            newNode = SNode(elem)
            node = self._head

            # recorre la lista hasta middle
            for i in range(middle - 1):
                node = node.next
            newNode.next, node.next = node.next, newNode

            self._size += 1
        return


    def insertList(self,inputList,start,end):

     # tener en cuenta que la posición  primera es 0
     # compruebo que los parámetros son correctos
        if start < 0 or end >= len(self) or end < start:
            print("Los parámetros", start, end, "no sirven")
            return -1
        
        #sustituir toda la lista
        if start==0 and end==(len(self)-1):
            newNode = inputList._head
            self._head = SNode(newNode.elem)
            self._size = 1
            newNode=newNode.next
            nStart=self._head

            while newNode is not None:
                nStart.next = SNode(newNode.elem)
                self._size += 1
                nStart = nStart.next
                newNode = newNode.next

        elif start==0:
            # contador
            i = 0
            nActual = self._head
            # el nodo que está en la posición end se elimina
            while i < end + 1:
                nActual = nActual.next
                i += 1
            nEnd = nActual
            
            newNode = inputList._head
            self._head = SNode(newNode.elem)
            self._size -=  end - 1
            newNode = newNode.next
            nStart = self._head

            while newNode is not None:
                nStart.next = SNode(newNode.elem)
                self._size += 1
                nStart = nStart.next
                newNode = newNode.next

            nStart.next = nEnd

        elif end==(len(self)-1):
            i = 0
            nActual = self._head
            while i < start - 1:
                nActual = nActual.next
                i += 1
            nStart = nActual

            self._size = start
            newNode = inputList._head
            while newNode is not None:
                nStart.next = SNode(newNode.elem)
                self._size += 1
                nStart = nStart.next
                newNode = newNode.next
            
        #se borra toda la lista salvo la cabeza y la cola (un grupo de nodos que están al inicio y final)
        else:
            # contador
            i = 0
            nActual = self._head
            while i < start-1:
                nActual = nActual.next
                i += 1
            nStart = nActual
            #el nodo que está en la posición end se elimina
            while i < end+1:
                nActual = nActual.next
                i += 1
            nEnd = nActual

            self._size -= end-start + 1
            newNode=inputList._head
            while newNode is not None:
                nStart.next=SNode(newNode.elem)
                self._size += 1
                nStart=nStart.next
                newNode = newNode.next
            nStart.next = nEnd
        return  

    def reverseK(self,k):
        if k <= 1:
            print(k, "no es admisible")
            return
        #colocamos el nodo en la cabecera
        node = self._head
        prev =  None
        #si k es mayor que los elementos de la lista, la invertimos entera
        if k >= len(self):
            while node is not None:
                node.next = prev
                prev = node
                node = node.next
            self._head = prev

        else:
            #si k se encuentra en medio de la lista, creamos una lista auxiliar
            #para ir introduciendo los valores invertidos
            lista = SList()
            posicion = 0
            contador = 0
            while node is not None:
                element = node.elem
                lista.insertAt(posicion, element)
                contador += 1
                #si el contador es igual a k, sumamos a la posicion, el numero de 
                #k para que introduzca los elementos de la lista invocante en la 
                #siguiente posicion 
                if contador == k:
                    posicion += k
                    #reiniciamos el contador
                    contador = 0
                
                node = node.next
            
            self._head = lista._head
                

        """invierte los elementos de la lista en grupos de k
        otra forma de hacerlo para que no tenga complejidad cuadratica, 
        pero no funciona
        if k <= 1:
            print(k, "no es admisible")
            return
        
        # en caso de que tenga que invertir la lista entera
        node = self._head
        sig = None
        prev = None
        #hay que estudiar el caso de que k sea mayor = que la lista
        if k>=len(self):
            while node:
                sig = node.next
                node.next = prev
                prev = node
                node = sig
            self._head = prev
    
        
        else:
            #creo una variable para reestablecer _head
            cabeza = False
            lista = SList()
            c=0
            while node!=None:
                if c<=k and cabeza == False:
                    if c < k:
                        if lista.isEmpty():
                            lista._head = node
                            nodeIt = lista._head
                            nextNode = nodeIt.next
                        else:
                            node.next = lista._head
                            lista._head = node
                            #guardo el nodo para enlazarle con el siguiente
                            #último que me he encontrado
                        c+=1
                        node = node.next
                    if c==k:
                        cabeza = True
                        c = 0
    
                elif c<=k and cabeza == True:
                    if c < k:
                        if nextNode == None:
                            node.next = None
                        else:
                            node.next = nextNode
                        nextNode = node
                        c+=1
                        if c == k:
                            nextNode = node.next
                        node = node.next
                    if c == k:
                        c = 0  
            self._head = lista._head
            
"""
    def maximumPair(self):
        """la función debe devolver el valor máximo de la suma de elementos equidistantes en una lista"""
    #la distancia de n al inicio y de m al fin tiene que ser la misma
    #if len(self) % 2 == 0:
        #es par
        i = 0
        j= len(self) - 1
        #colocamos el nodo en la cabecera
        node = self._head
        valor_maximo = 0
        #si la lista no tiene elementos, no devolvemos nada
        if len(self) == 0:
            return None
        #si solo tiene un elemento, devolvemos el valor
        elif len(self) == 1:
            return node.elem

        else:
            while i <= j:
                node = self._head
                contador = 0
                while i > contador:
                    node = node.next
                    contador += 1
                n = node.elem
                while j > contador:  # se recorre pq queremos llegar hasta el segundo valor, hay que avanzar la diferencia
                    node = node.next
                    contador+= 1
                m = node.elem
                if i == j:
                    suma = (n + m) / 2
                else:
                    suma = n + m
                if valor_maximo < suma:
                    valor_maximo = suma
                i += 1
                j -= 1

        return valor_maximo
