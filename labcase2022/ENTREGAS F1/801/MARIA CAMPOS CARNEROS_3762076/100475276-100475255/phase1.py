from slist import SList
import sys
from slist import SNode

class SList2(SList):

    def sumLastN(self, n):
        contador = 0
        if n < 0:
            return None
        elif n == 0:
            return 0           
        else:
            if self.isEmpty():
                return 'La lista está vacía'
            else:
                inicio = self._head
                restante = (self._size) - n
                if restante <= 0:
                    contador += inicio.elem
                    for i in range(self._size - 1):
                        inicio = inicio.next
                        contador += inicio.elem
                    return contador
                else:                
                    for i in range(restante-1):
                        inicio = inicio.next
                    for i in range(n): 
                        inicio = inicio.next
                        contador += inicio.elem
                       

                    return contador
    '''_____________________________________________________________________________________________________'''

    #method for inserting a new node in the middle
    def insertMiddle(self, elem):
        if self.isEmpty():
            self.addFirst(elem)
        else:
            prev=self._head
            #Listas con número par de elementos#
            if len(self) % 2 == 0:
                posicion=len(self)//2
                for i in range(posicion-1):
                    #Para localizar el nodo anterior al lugar en el que queremos insertar el nuevo#
                    prev=prev.next
                #Se crea el nuevo nodo#
                newNode=SNode(elem)
                #Ponemos punteros#
                newNode.next=prev.next
                prev.next=newNode
                self._size+=1
            #Listas con número impar de elementos
            else:
                posicion=(len(self)+1)//2
                for i in range(posicion-1):
                    #Para localizar el nodo anterior al lugar en el que queremos insertar el nuevo#
                    prev=prev.next
                #Se crea el nuevo nodo#
                newNode=SNode(elem)
                #Ponemos punteros#
                newNode.next=prev.next
                prev.next=newNode
                self._size+=1
    '''_________________________________________________________________________________________________________'''

    def insertList(self,inputList,start,end):
        
        inicio = self._head
        fin = self._head
        colaInput = inputList._head

        if start>=0 and start<=end and end<self._size:
            if self._size > 0:
                if end != self._size - 1:
                    if start != 0:
                        
                        for i in range(start - 1):  #puntero en el nodo anterior a start
                            inicio = inicio.next
                        for i in range(end + 1):    #puntero en el nodo siguiente a end
                            fin = fin.next
                        for i in range(inputList._size - 1):  #punturo al final de inputList
                            colaInput = colaInput.next
                            
                        inicio.next = inputList._head   #el puntero del nodo anterior a start ahora apunta al 1º de inputList
                        colaInput.next = fin            #el puntero del final de inputList ahora apunta al nodo después de end
                    else:
                        for i in range(end + 1):    
                            fin = fin.next
                        for i in range(inputList._size - 1):  
                            colaInput = colaInput.next
                            
                        self._head = inputList._head
                        colaInput.next = fin                   
                else:
                    if start == 0:
                        self._head = inputList._head
                        
                    else:                   
                        for i in range(start - 1):  
                            inicio = inicio.next                  
                        inicio.next = inputList._head                                       
            else:
                self._head = inputList._head 
        else:
            return 'Los valores de start o end son incorrectos'
    '''______________________________________________________________________________________________________________'''        
        
    def reverseK(self,k):
       nodo=self._head
       posicion=0
       m=0
       pos=0
       lista=SList()
       while nodo:
           #Insertamos m veces elementos en la lista auxiliar#
           lista.insertAt(pos, nodo.elem)
           m+=1
           posicion+=1
           nodo=nodo.next
           #Elementos colocados->Reiniciar ciclo#
           if m==k:
               m=0
               pos=posicion
       self._head=lista._head 
    '''_______________________________________________________________________________________________________________'''

    def maximumPair(self):
        resultado=None
        #Si la lista esta vacia#
        if self.isEmpty():
            return None
        #Si la lista tiene 1 solo elemento#
        elif len(self)==1:
            nodo=self._head
            resultado=nodo.elem
            return resultado
        #Si la lista tiene 2 elementos#
        elif len(self)==2:
            nodo1=self._head
            nodo2=nodo1.next
            resultado=(nodo1.elem+nodo2.elem)
            return resultado
        #Si la lista tiene >2 elementos#
        else:
            nodo=self._head
            posicion=0
            smax=0
            #Se recorre la mitad de la lista
            while posicion< len(self)//2:
                #Si la lista es par#
                opuesto=len(self)-posicion-1
                equi=self.getAt(opuesto)
                valor= nodo.elem + equi
                smax=max(smax, valor)
                posicion+=1
                nodo=nodo.next
            #Si la lista es impar#
            if len(self)%2 !=0:
                smax=max(smax, nodo.elem)

            return smax