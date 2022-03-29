from slist import SNode
from slist import SList
import sys

class SList2(SList):

    def sumLastN(self, n):
        #método que me suma los últimos n elementos de la lista
        suma = 0

        if n < 0:
            return None

        if n == 0:
            return suma

        if n > 0:
            longitud = len(self) - n
            saltos = 0
            Nodo = self._head
            while Nodo:
                if saltos >= longitud:
                    suma += Nodo.elem
                Nodo = Nodo.next
                saltos += 1

            return suma
    
    #method for inserting a new node in the middle
    def insertMiddle(self, elem):
        #Método que inserta un elemento elem en la mitad de una lista
        if len(self) == 0:
            self.addFirst(elem)
        else:    
            previous = self._head
            if len(self)%2 == 0:
                a = (len(self)//2) - 1
                while a != 0:
                    previous = previous.next
                    a -= 1
                newNode=SNode(elem)
                newNode.next = previous.next
                previous.next = newNode
                self._size+=1
    
            else:
                a = ((len((self))+1)/2)-1
                while a != 0:
                    previous = previous.next
                    a -= 1
                newNode=SNode(elem)
                newNode.next = previous.next
                previous.next = newNode
                self._size+=1

    
    def insertList(self,inputList,start,end):
        #Método que borra los elementos de self entre start y end y mete en ese lugar la inputlist
        following=None
        if start < 0 or start > end or start > len(self) or end > len(self):
            return None
        else:
            if start  == 0 and end != len(self):
                end += 1
                following = self._head
                while end != 0:
                    following = following.next
                    end -=1
                node = inputList._head
                while node.next != None:
                    node = node.next
                node.next = following
                self._head = inputList._head
                self._size += (len(inputList) - (end - start))

            elif end == len(self) and start != 0:
                previuos = self._head
                while start !=1:
                    previuos = previuos.next
                    start -=1
                node = inputList._head
                while node.next != None:
                    node = node.next
                previuos.next = node
                self._size += (len(inputList) - (end - start))

            elif start == 0 and end == len(self):
                self = inputList

            elif self.isEmpty():
                self = inputList
                
            else:
                following = self._head
                previuos = self._head
                end +=1
                while end != 0:
                    following = following.next
                    end -=1
                if start == 1:
                    previuos = self._head
                else:
                    while start !=1:
                        previuos = previuos.next
                        start -=1

                previuos.next = inputList._head
                node = inputList._head
                while node.next != None:
                    node = node.next
                node.next = following
                self._size += (len(inputList)-(end - start))

    def reverseK(self,k):
        #Método que da la vuelta de k en k elementos a todos los de la lista
        Nodo = self._head
        saltos = 0
        indice = 0
        ciclos = 0
        lista2 = SList2()
        if k == 1:
            pass
        elif self.isEmpty():
            pass
        else:
            #Añade los k elementos de self a lista2 en la posicion indice siempre, por ejemplo el primero en posicion 0 y el segundo en posicion 0
            while Nodo:
                lista2.insertAt(indice, Nodo.elem)
                ciclos += 1
                saltos += 1
                Nodo = Nodo.next
            #sumamos 1 a ciclos y a saltos, cuando ciclos llegue a k se reinicia y empezamos de cero, pero con la posicion indice cambiada a la variable saltos
                if ciclos >= k:
                    ciclos = 0
                    indice = saltos

            self._head = lista2._head

    def maximumPair(self):
        #Método que recorre la lista y suma los elementos equivalentes y devuelve la máxima suma
        suma = 0
        aux = 1
        node=self._head
        pair = (len(self)) // 2

        if len(self) == 0:
            return None
        elif len(self) == 1:
            suma = self._head.elem
            return suma
        else:
            while pair != 0:
                
                valor = self.getAt(len(self)-aux)
                valor += node.elem
                suma = max(suma, valor)
                node = node.next
                aux += 1
                pair-=1
            if len(self) % 2 != 0:
                suma = max(suma, node.elem)

            return suma

                

        


 