from slist import SList
from slist import SNode
import sys

class SList2(SList):

    def sumLastN(self, n): #función que toma un número entero n y devuelve la suma de los n últimos nodos de la lista invocante.
        suma = 0           # i n<0, la función debe devolver None. Si el valor de n es mayor que el tamaño de la lista, devuelve la suma de todos los elementos
        if n == 0:
            suma = 0
        elif n < 0:
            suma = None
        else:
            current = self._head
            if n < len(self):                          #n como el tope de elementos a sumar
                for x in range(len(self) - n):         #movemos el puntero hasta la posicion deseada
                    current = current.next
                for h in range(n):                      # vamos cogiendo uno a uno los n nodos
                    suma += current.elem
                    current = current.next
            else:                                       #la suma de todos los elementos
                for h in range(len(self)):
                    suma += current.elem
                    current = current.next
        return suma
        #complejidad n

    def insertMiddle(self, elem):    #inserta el elemento e en el medio de la lista invocante
        #calculo de la posicion donde se introduce el elemento dependiendo de si es par o impar
        if len(self) % 2 == 0:
            posicion = int(len(self) // 2)

        elif len(self) % 2 != 0:
            posicion = (len(self) + 1) // 2

        if posicion == 0:               # la posicion es 0
            self.addFirst(elem)
        elif posicion == len(self):     # la posicion es el final de la lista
            self.addLast(elem)
        else:
            prev = self._head
            for i in range(posicion - 1):   # creamos un puntero para controlar la posicion donde queremos meter el nodo
                prev = prev.next
            newNode = SNode(elem)           #creamos el nodo
            newNode.next = prev.next    #enlazamos el nuevo nodo al siguiente elemento
            prev.next = newNode         # y el elemento del puntero se engancha al nuevo nodo
            self._size += 1
        #complejidad n

    def insertList(self,inputList,start,end): #La función toma como parámetros un objeto de la clase SList2, inputList, y dos números enteros, start y end. La función debe eliminar todos
                                                #los elementos de la lista invocante entre las posiciones start y end, e insertarlos elementos de la lista inputList en su lugar.
        if not (start < 0 or start > end or end >= len(self)): # si el start es menor que 0, el start mayor que el end, o el end se sale de rango no se toca la lista
            current = self._head
            prev = self._head
            node1 = inputList._head
            node2 = inputList._head
            for n in range(start-1):            # estara en la posicion anterior al start
                prev = prev.next
            for x in range(end+1):              # estara en la posicion siguiente al end
                current = current.next
            for y in range(len(inputList)-1):   # estara al final de la input list
                node2 = node2.next

            prev.next = node1                   # enganchamos el ultimo nodo de la primera parte de la lista a la inputlist
            node2.next = current                # enganchamos el ultimo nodo de la inputlist al primero de la segunda parte de la lista original
            if start == 0:
                self._head = self._head.next   # permite eliminar el primer nodo de la lista orignal que en este caso no queremos como el unitest 4
            self._size = self._size + len(inputList) -(end+1-start)
        #complejidad n

    def reverseK(self,k):

        current = self._head
        milista = SList2()              # lista de apoyo

        if self.isEmpty() or k <= 1:       # esta vacia o solo un elemento la lista no se cambia
            print(SList2)

        elif k >= self._size:               # si hay que darle la vuelata a la lista entera
            for n in range(self._size):        # se añaden los elementos de la lista asi misma en orden inverso utilizando addFirst y moviendo punteros
                self.addFirst(current.elem)
                current = current.next
            prev = self._head

            for n in range((self._size//2)-1):  # movemos el puntero a la mitad de la lista, nodo desde el cual el resto es la lista original por lo que lo eliminamos
                prev = prev.next
            prev.next = None

        else:
                                        #meto los k primer elementos directamente ordenados, como si diesemos la vuelta a la lista entera pero solo k elementos
            for n in range(k):
                print(current.elem)
                self.addFirst(current.elem)
                current = current.next

            n = self._size // k
            print("n",n)
            support = self._head

            for n in range(n-1):                    #queremos darle la vuelta a los grupos de numeros en una lista auxiliar y posteriormente reintroducirlos a la original
                if self._size%k == 0:               # todos los grupos son del mismo tamaño
                    for n in range(k):                    #meto los k siguientes elementos ordenados en la lista auxiliar y el current desaparece
                        milista.addFirst(current.elem)
                        if current.next != None:
                            current = current.next
                else:                   # existen elementos sobrantes
                    for n in range(k-2):
                        milista.addFirst(current.elem)
                        if current.next != None:
                            current = current.next

                for n in range(k-1):        # movemos el puntero al final del primer grupo ordenado donde lo juntaremos con el el siguiente grupo
                    support = support.next

                another2 = milista._head
                support.next = another2
                support = support.next
                prev = self._head

                for n in range((self._size // 2)+1): #eliminamos el la lista original
                    if prev.next != None:
                        prev = prev.next
                prev.next = None


    def maximumPair(self): # sumar equidistantes
        suma = 0
        current = self._head
        contador = 0

        if self.isEmpty():   # si la lista vacia no hay suma
            suma = None
            return suma

        else: # par
            if self._size == 1:     # si solo hay un elemento
                suma = current.elem

            for n in range(len(self)//2):
                parcial = current.elem + self.getAt(len(self) - 1 - contador)       # va haciendo las sumas parciales y las compara con una variable suma
                current = current.next                                              # lo que permite ir sumando dos numeros de cada vez y verificar si son o no mayores que suma
                contador += 1
                if parcial > suma:
                    suma = parcial
                if (len(self)%2) != 0:
                    if current.elem > suma:             # para el elemento extra que no tiene pareja en impares
                        suma = current.elem

            return suma
        #complejidad n2