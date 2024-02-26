from slist import SList
from slist import SNode
import sys

class SList2(SList):

    def sumLastN(self, n): #Función que suma los n últimos números
       nodeIt = self._head
       result = 0
       if n<0: #Caso con n negativo imposible
           return None
       if self.isEmpty() or n == 0: #Caso en que la lista esté vacía o n sea 0, se duelve 0
           return 0
       elif n>len(self): #Si n es mayor a la longitud de la lista sumo todos los elementos
           while nodeIt:
               result += nodeIt.elem
               nodeIt = nodeIt.next
           return result
       else: #Si n es un número entre 0 y la longitud de la lista
           for e in range(len(self)):
               if e >= (len(self)-n):
                   result += nodeIt.elem
               nodeIt = nodeIt.next #Recorre la lista hasta llegar a la primera posición que suma
           return result
        
                
                
            
    
    #Método que inserta nuevo nodo en el medio
    def insertMiddle(self, elem):
        nodeIt = self._head
        if self.isEmpty(): #Si la lista está vacía
            self.addFirst(elem)
        else:
            if len(self)%2 == 0: #Si la longitud es par
                for i in range((len(self)//2)-1): #Llega a la posición donde insertar
                    nodeIt = nodeIt.next
            else: #Impar
                for i in range((len(self)+1)//2-1):
                    nodeIt = nodeIt.next
            #Hemos llegado a la posición donde queremos insertar en nodo
            newNode = SNode(elem) #Crea el nuevo nodo
            newNode.next = nodeIt.next #Recoloca puntero siguiente y el del nodo anterior hacia él
            nodeIt.next = newNode
            self._size +=1

                    
                

    
    #Función que inserta lista entre dos puntos start y end
    def insertList(self,inputList,start,end):
        if start<0 or start>end or end>=len(self): #Casos imposibles
            return("Error")           
        else:
            prev = self._head 
            if start > 0: #Llega a posición Start con puntero1
                for i in range(start-1):
                    prev = prev.next             
            nodel1 = self._head
            for j in range(end): #Llega a la posición de end con puntero2
                nodel1 = nodel1.next
            nodel2 = inputList._head
            while nodel2.next:
                nodel2 = nodel2.next
            if start > 0: #Puntero del prev apuntando al _head de la lista
                prev.next = inputList._head
            else: #Si start es cero, insertar al principio
                self._head = inputList._head
            nodel2.next = nodel1.next #Recolocar el puntero del último elemento de inputlist a la lista inicial


        

    
    def reverseK(self,k):
        if k<= 1:
            print("No se realiza ninguna transformacion")
            return self
        else:
            nodeIt = self._head
            nuevaLista = SList2() #Creamos lista auxiliar, donde se van a realizar los cambios
            count = 0
            e = 0
            pos = 0
            while nodeIt:
                nuevaLista.insertAt(pos, nodeIt.elem)
                #El índice es 0 al recorrer la lista hasta que llega a la posición k (va insertando delante)
                #En la posición k "divide la lista" y vuelve a insertar delante
                count += 1
                e += 1
                nodeIt = nodeIt.next
                if count == k:
                    pos = e
                    count = 0
            self._head = nuevaLista._head #Así devuelve la lista inicial modificada
            return self
            

            


    def maximumPair(self):
        result = 0
        nodeIt = self._head
        pos = 0
        if self.isEmpty(): 
            print( "La lista está vacía")
            return None
        # Si la longitud de la lista es 1, el resultado será directamente el único elemento
        elif len(self) == 1:
            result = self._head.elem             
        else:
            #Vamos moviendo el puntero hasta la mitad de la lista, sumando cada elemento con el de su posición simétrica
            while pos < len(self)//2: 
                elemSum = self.getAt(len(self)-pos-1)
                suma = nodeIt.elem + elemSum
                if suma > result:
                    result = suma
                nodeIt = nodeIt.next
                pos +=1
            if not len(self)%2 == 0: #En el caso de ser impar, ya tenemos colocado el nodo en la mitad 
                if nodeIt.elem > result:
                    result = nodeIt.elem
        return result

        
 