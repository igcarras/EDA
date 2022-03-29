#Francisco Torija Jimenez, 100429111
#Daniel Telo Fernández, 100405908
 
from slist import SList
from slist import SNode
import sys

class SList2(SList):

    def sumLastN(self, n):
        
        if n < 0:                      #Si n < 0, devolvemos "None"
            return None
        
        elif n == 0:                   #Si n == 0, devolvemos "0"
            return 0
      
        else:                          #Para n > 0, recorremos la lista con un nodeIt y un cont para
            nodeIt = self._head        #situarnos en el nodo desde el que debemos sumar
            i = 0
            cont = len(self) - n       
            while nodeIt and i < cont:
                nodeIt = nodeIt.next
                i += 1
            none_check = 0
            suma = 0                   #Una vez en el nodo, sumaremos los elementos  
                                       #desde dicho nodo hasta el final
           
            for i in range(int((len(self)-n)), int(len(self))):
                none_check = self.getAt(i)                       #con este contador nos aseguraremos
                if none_check != None:                           #de que no se anaden 'None' a la lista
                    suma += none_check                           #en los casos donde n > len(self)
    
        return suma





    def insertMiddle(self, elem):
        
        if len(self) == 0:                       #Si la lista esta vacia, anadimos el elemento
            self.addFirst(elem)

        else:                                    #Si no, debemos diferenciar que la lista sea par o impar 
            
            if len(self) % 2 == 0:               #PAR
                posicion = int(len(self)/2)      #Calculamos el nodo 'posicion' y anadimos el nuevo nodo
                prev = self._head                #redirigiendo los punteros
                
                for i in range(posicion - 1):
                    prev = prev.next
                newNode = SNode(elem)
                newNode.next = prev.next
                prev.next = newNode
                self._size += 1
         

            else:                                #IMPAR
                posicion = int((len(self)+1)/2)  #Casi identico procedimiento, solo varia el calculo
                prev = self._head                #de la posicion central de la lista
                for i in range(posicion - 1):
                    prev = prev.next
                newNode = SNode(elem)
                newNode.next = prev.next
                prev.next = newNode
                self._size += 1
                
    


    
    def insertList(self,inputList,start,end):
        
        if start > 0 and start < end and end < len(self): ## CASO BASE #1: start > 0, start < end y end < len(self) ##
            node_cont_start = self._head                  #Nodos para recorrer la lista original y llegar hasta el elem "start"                 
            node_start = self._head                       
            node_cont_end  = self._head                   #Nodos para recorrer la lista original y llegar hasta el elem "end"
            node_end = self._head                                             
            node_input = inputList._head                  #Nodo final de input_list, que apuntara al resto de la lista original
            cont_start = cont_end = 0                     #Contadores para recorrer la lista original

            while node_start:  # != None                    #Bucle while para recorrer la lista original entera
                if cont_start != (start-1):                     #Mientras el "cont" sea distinto a "start-1" (para situarnos en el elem anterior al que queremos cambiar)
                    cont_start += 1                                 #Iremos sumando uno
                    node_cont_start = node_cont_start.next          #Y pasando de nodo en nodo hasta llegar al nodo "start-1"
                
                node_start = node_start.next                    #Cuando termine el if, con esto saldremos del while
                
            while node_end:                                 #Exactamente el mismo procedimiento para "end"
                if cont_end != end:
                    cont_end += 1
                    node_cont_end = node_cont_end.next
                
                node_end = node_end.next

            while node_input.next:  # != None               #Bucle while para recorrer la inputList hasta el final
                node_input = node_input.next                #Y asi tener el puntero en su ultimo nodo
            
                                                            #ACTUALIZAMOS/REDIRIGIMOS PUNTEROS
            node_cont_start.next = inputList._head          #El nodo siguiente a "start" ahora apuntara al primero de la nueva lista
            node_input.next = node_cont_end.next                #Y el nodo siguiente al final de la nueva lista apuntara al "end" de la original
            self._size = len(self) - (end - start) + len(inputList)  #Por ultimo, actualizamos el size

        
        if start == end and start != 0 and end != 0:     ## CASO BASE #2: start y end son iguales, pero distintos de cero ##
            
            node_cont_node = node_node = self._head       #Nodos para recorrer la lista original y llegar hasta el elem "start"
            node_prev = None
            node_input = inputList._head                  #Nodo final de input_list, que apuntara al resto de la lista original
            cont_node =  0                                #Contadores para recorrer la lista original

            while node_node:  # != None                    #Mismo procedimiento que los while anteriores
                if cont_node != (start-1):                 #Buscamos el nodo anterior al start para redirigir punteros   
                    cont_node += 1                             
                    node_prev = node_cont_node
                    node_cont_node = node_cont_node.next
                                                           
                node_node = node_node.next                
           

            while node_input.next:  # != None              #Identico bucle while para tener el puntero 
                node_input = node_input.next               #En el ultimo elem de la inputList
            
            node_prev.next = inputList._head                #ACTUALIZAMOS/REDIRIGIMOS PUNTEROS
            node_input.next = node_cont_node.next           #En este caso, se elimina solo un elem y se anade ahi la nueva lista
            self._size = len(self) - 1 + len(inputList)     #Actualizamos el size
        
        
        if start == 0 and end == 0:                         ## CASO BASE #3: start y end iguales, ambos son cero ##
            node_input = inputList._head                    
            while node_input.next:  # != None               #Identico bucle while para tener el puntero
                node_input = node_input.next                #En el ultimo elem de la inputList
            
            node_input.next = self._head.next               #ACTUALIZAMOS/REDIRIGIMOS PUNTEROS
            self._head = inputList._head                    #En este caso, solo se eliminara el self._head 
            self._size = len(self) - 1 + len(inputList)     #Y se anadira ahi la nueva lista
            #Actualizamos el size
        
        if start == 0 and end > 0 and end < len(self):      ## CASO BASE #4: start es cero y end no \\ end < len(self) ## 
            node_zero_end = self._head                    
            node_zero_cont_end = self._head
            cont_zero_end = 0
            node_input = inputList._head
            
            while node_input.next:  # != None               #Identico procedimiento para situar el puntero
                node_input = node_input.next                #En el ultimo nodo de la inputList
                
            while node_zero_end:                            #Identico procedimiento para encontrar el nodo end
                if cont_zero_end != end:
                    cont_zero_end += 1
                    node_zero_cont_end = node_zero_cont_end.next
                node_zero_end = node_zero_end.next

                                                            #ACTUALIZAMOS/REDIRIGIMOS PUNTEROS
            self._head = self._head.next                    #Eliminamos el primer elem de la lista haciendo next
            self._head = inputList._head                    #Y mi nueva head sera la head de inputList
            node_input.next = node_zero_cont_end.next       #El final de inputList apuntara al resto de la lista original
            self._size = len(self) - 1 + len(inputList)     #Actualizamos el size
            




    def reverseK(self,k):
        
        listaMayorK = SList()                            #Lista auxiliar para revertir los elem
        if k >= len(self):                               #Si k es mayor que la longitud de la lista
                                                         #Simplemente revertiremos todos los elem de esta
            for i in range(len(self)):
                listaMayorK.addFirst(self.removeFirst())
                i += 1
                
            self._head = listaMayorK._head               #Referenciamos el nuevo head
        
        elif 1 < k < len(self):                         #Si k es mayor que 1 y menor a la len de la lista
            listaReverso = SList()                      #Usaremos dos listas auxiliares, una para revertir
            listaFinal = SList()                        #Los elementos y la otra para devolverlos
           
            j = 1
            node = self._head
            
            while node:                                 #Mientras recorremos todos los nodos de la lista
                while j <= k:                              #Hacemos este bucle para revertir de 'k' en 'k' paquetes
                    a = self.removeFirst()
                    if a != None:
                        listaReverso.addFirst(a)
                    
                    if node != None:
                        node = node.next
                    
                    j += 1                              #Actualizamos 'j' cada iteracion para salir del bucle
                
                while len(listaReverso) != 0:           #Mientras haya elementos en nuestra listaReverso
                    listaFinal.addLast(listaReverso.removeFirst())  #Los anade y coloca en nuestra listaFinal
                 
                j = 1                                   #Hacemos que 'j' sea 1 de nuevo para volver a empezar
                
                
            self._head = listaFinal._head               #Por ultimo, referenciamos nuestra nueva head

        else:  #k <= 1                                  #Finalmente, si k es igual o menos a 1, la lista se queda igual
            pass
            
            
        

        
        
        


    def maximumPair(self):
        auxList1=SList()
        auxList2=SList()
        auxList3=SList()
        
        if (len(self) % 2) == 0:          #En caso de ser par la long de self
            rango=int(len(self)/2)
            for i in range(rango):
                var=self.getAt(i)
                auxList1.addLast(var)

                
                
            for i in range(rango , len(self)):
                var=self.getAt(i)
                auxList2.addFirst(var)

            
            
            for i in range(len(auxList1)):
                var1=auxList1.getAt(i)
                var2=auxList2.getAt(i)
                var3=var1+var2
                auxList3.addLast(var3)
            
            h=auxList3.getAt(0)
            
            for i in range(len(auxList3)):
                p=auxList3.getAt(i)
                if p>h:
                    h=p
                else:
                    continue
            return h
         
        elif len(self)==1:
            return self.getAt(0)
        
        else:
            rango=int((len(self)-1)/2)          
            varMed=self.getAt(rango)          #mitad de lista    
            for i in range(rango):          #rellena la lista 1
                var=self.getAt(i)
                auxList1.addLast(var)
                
                
            for i in range((rango+1) , len(self)):          #rellena la lista 2
                var=self.getAt(i)
                auxList2.addFirst(var)
            
            
            for i in range(len(auxList1)):              #suma y rellena lista 3
                var1=auxList1.getAt(i)
                var2=auxList2.getAt(i)
                var3=var1+var2
                auxList3.addLast(var3)
            
            h=auxList3.getAt(0)                        #variable inicial para comparar con el resto de elem de la lista aux 3                                 
            
            for i in range(len(auxList3)):              #comprobación del mayor valor de lista aux 3
                p=auxList3.getAt(i)
                if p>h:
                    h=p
                else:
                    continue
                
            if h>varMed:
                return h
            else:
                return varMed
    

