from slist import SList
from slist import SNode
import sys

class SList2(SList):

    def sumLastN(self, n):
        """Toma un número entero n y devuelve la suma de los n últimos nodos de la lista invocante. O(n)"""
        result = 0
        punt = self._head
        if len(self) == 0 or n == 0: #Comprobamos que los valores son correctos
            return 0
        if n < 0:
            return None
        if n >= len(self): # Si n es mayor que la longuitud, hacemos que sea igual
            n = len(self)  # para ejercutar los bucles
        for i in range(len(self) - n): # Nos movemos los nodos necesarios hasta
            punt = punt.next           # llegar a los n últimos
        for i in range(n): # Sumamos el valor del elemento y pasamos al siguiente
            result += punt.elem
            punt = punt.next
        return result
    
    #method for inserting a new node in the middle
    def insertMiddle(self, elem):
        """Se inserta el elemento e en el medio de la lista invocante. O(n)"""
        if len(self) == 0: # Si la lista está vacía, añadimos el elmento
            self.addFirst(elem)
            return None
        punt = self._head
        medio = len(self) // 2
        if len(self)%2 != 0: # Si es impar, sumamos 1 a medio
            medio += 1
        if medio == 0: # Si es 0, añadimos el elemento
             self.addFirst(elem)
        else:
            punt = SNode(elem)
            node = self._head
            for i in range(medio - 1): # Nos movemos los nodos necesarios
                node = node.next
            punt.next = node.next # Añadimos el nodo y aumentamos el tamaño
            node.next = punt
            self._size += 1
        return None


    
    def insertList(self,inputList,start,end):
        """Se eliminan todos los elementos de la lista invocante entre las posiciones 
        start y end, e insertamos los elementos de la lista inputList en su lugar. O(n2)"""
        punt = self._head
        if start < 0 or start > end or end >= len(self): #Comprobamos que los valores son correctos
            return None
        if start == 0: # Si start es 0 no queremos que se mueva
            for i in range(end + 1): # Borramos los elementos que sean necesarios
                punt = punt.next
                self._size -= 1
            self._head = punt
        else:    
            for i in range(start - 1): # Nos movemos los nodos que sean necesarios
                punt = punt.next
            for i in range(end - start + 1): # Borra los elementos que sean necesarios
                punt.next = punt.next.next
                self._size -= 1
        for i in range(len(inputList)): # Para cada nodo de la lista
            self.insertAt(start + i, inputList.removeFirst()) # Insertamos en su respectiva posición los
                                                              # nodos de la lista y los vamos eliminando
                                                              # para pasar al siguiente que se inserta
                                                              # en la siguiente posición  
        return None
            


    def reverseK(self,k):
        """Se invierten los elementos de la lista invocante en grupos de k elementos."""
        if k <= 1: # Comprobamos si el valor de k es válido para hacer la transformación
            return None
        elif k >= len(self): # Si esto se cumple, si invierte la lista completa
            newList = SList()
            while len(self) > 0:
                newList.addFirst(self.removeLast()) # Añadimos al principio de la nueva lista el 
                                                    # último elemento de la lista invocante el cual
                                                    # eliminamos
            self._head = newList._head      # Copiamos los elementos de la nueva lista en la
            self._size = newList._size      # actual
            
        else:
            aux = SNode(None)  #Creamos un nuevo nodo
            aux.next = self._head #Declaramos las variables del nodo
            current = self._head
            lastaux = aux
            lastcurrent = current
            i = k
            while current:   #Creamos un bucle que recorra toda la lista
                prev = None
                while i > 0 and current:  #Con un contador vamos sacando los elementos de la lista
                    next = current.next
                    current.next = prev
                    prev = current
                    current = next
                    i -= 1
                lastaux.next = prev  #Con los valores anteriores invertimos la posición de los nodos
                lastcurrent.next = current
                lastaux = lastcurrent
                lastcurrent = current
                i = k
            self._head = aux.next
        return None 

    def maximumPair(self):
        """Se debe devolver el valor máximo de la suma de elementos equidistantes en una lista. O(n2)"""
        result = 0
        newList = SList()
        if len(self) == 0: # Si la lista está vacía, devuelve None
            return None
        else: # En caso contrario, copiamos la lista para hacer los cambios
            for i in range(len(self)): # Recorremos cada nodo
                newList.insertAt(i, self.getAt(i)) # Añadimos en cada posición, el elemento que le corresponde
            while newList._head:
                if len(newList) > 1: # Mientras haya más de un elemento
                    suma = newList.removeFirst() + newList.removeLast() # Sumamos el primer y el último nodo de
                                                                        # la lista y los eliminamos para comprobar
                                                                        # los siguientes
                else: # Si sólo queda un elemento
                    suma = newList.removeFirst() # Lo guardamos en suma y lo eliminamos
                if suma > result: # Comprobamos para cada valor de suma si es mayor que el anterior y
                    result = suma # si cumple que es mayor, lo guarda en result para luego devolverlo
        return result
                    
        