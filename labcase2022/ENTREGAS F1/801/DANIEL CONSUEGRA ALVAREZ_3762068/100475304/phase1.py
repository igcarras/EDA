from slist import SList,SNode
import sys
"Author: Daniel Consuegra Álvarez"
"""Nota: Todos los métodos tienen una complejidad espacial lineal, pero también he incluido en los dos últimos
    métodos en comentarios una variante de complejidad espacial cuadrática pero que en algunas ocasiones
    es menos compleja a nivel temporal, dependiendo de factores externos"""

class SList2(SList):
    slist = SList()

    def sumLastN(self,n): #METODO QUE SUMA LOS N ULTIMOS NUMEROS DE UNA LISTA SIMPLE
        sum = 0      #variable para acumular la suma y que retornará el método
        if n == 0:   #cuando n vale 0 la suma es 0
            return sum
        if n < 0:
            return None # si es numero negativo devolvemos None
        if n > 0:                               # mientras n sea mayor que 0 es posible obtener valores
            index = self.__len__() - n          # obtenemos la posicion a partir de la cual queremos sumar los valores
            nodeIt = self._head                 # recorremos la lista con un nodo auxiliar
            saltos = 0
            while nodeIt:
                if saltos >= index:             # a partir de dicha posicion acumulamos los valores en la variable sum
                    sum += nodeIt.elem
                nodeIt = nodeIt.next
                saltos += 1
            return sum                          # devolvemos el valor de la suma

    # method for inserting a new node in the middle
    def insertMiddle(self, elem): # MÉTODO QUE INSERTA UN ELEMENTO EN MEDIO DE LA LISTA
        if len(self) % 2 == 0:     # ADJUDICAMOS UNA POSICION SI ES UN CONJUNTO PAR
            index = len(self) // 2
        else:
            index = (len(self) + 1) // 2  # ADJUDICAMOS UNA POSICION SI ES UN CONJUNTO IMPAR
        if index == 0:  #cuando es 0 llamamos al método addfirst
            self.addFirst(elem)
        elif index == len(self):
            self.addLast(elem)# cuando es el ultimo elemento método addlast
        else:
            previous = self._head  # buscamos la posicion anterior
            for i in range(index - 1):
                previous = previous.next

            Node = SNode(elem)
            Node.next = previous.next  # el nuevo nodo apunta al siguiente del previous
            previous.next = Node  # el puntero del previous apunta al nuevo nodo
            self._size += 1

    def insertList(self, inputList, start, end): #METODO QUE INSERTA UNA LISTA ENTRE 2 POSICIONES DE OTRA LISTA
        if start < 0 or end >= len(self) or start > end:    #comprobamos que los valores posiciones son válidos
            pass
        else:
            nodeIt = inputList._head                #recorremos la inputlist para obtener el ultimo nodo
            while nodeIt.next:
                nodeIt = nodeIt.next
            cont = 0
            aux = self._head
            pstart = None                   #estos seran los punteros auxiliares adjudicados a las posiciones recibidas por parametro
            pend = None
            while aux:                          #recorremos la lista invocante para obtener los nodos auxiliares
                if cont == start - 1:
                    pstart = aux
                if cont == end + 1:
                    pend = aux
                aux = aux.next
                cont += 1
            if start == 0:                          # en el caso de que start sea 0 tan solo movemos el _head
                self._head = inputList._head
            else:
                pstart.next = inputList._head            # el nodo auxiliar de la posicion start de la lista invocante apunta al _head de la inputlist
            nodeIt.next = pend                      # nodo final de la inputlist apunta a el nodo auxiliar de la posicion end de la lista invocante

    def reverseK(self, k):        # metodo que invierte una lista en grupos de k elementos

        auxList1 = None  # creamos dos listas auxiliares de la clase Slist2
        auxList2 = SList2()
        NodeIt = self._head  # creamos un nodo auxiliar para recorrer la lista
        i = 0  # un contador de saltos
        grupos = 1  # un contador de grupos
        add = True  # un booleano para diferenciar cuando añadir a la lista 1 y cuando a la lista 2
        resetList = True # variable para resetear la lista auxiliar 1
        q = 0 # variable para indicar el numero de elementos restantes en caso de que al final de la lista queden elementos restantes menores que k
        if k <= 1:  # si k<=1 el metodo no hace nada nada
            pass
        else:
            if k > len(self):
                k = len(self)
            while NodeIt and len(auxList2) <= len(self): #bucle para recorrer y operar sobre la lista inicial guardando ademas el tamaño de la lista final
                if grupos > len(self) / k and len(auxList1) < k:  # en el caso de que al final de la lista sobren elementos que no completen un grupo de k elementos
                    q = len(self) + 1 - i  # lo hacemos del numero de elementos que quedan
                if add:
                    if resetList: # crear/resetear la lista auxiliar 1
                        auxList1 = SList2()
                        resetList = False
                    if (grupos - 1) * k <= i < grupos * k: # condicion para que solo se añadan los elementos del grupo en el que estamos en función del contador i
                        auxList1.addFirst(NodeIt.elem)  # añadimos los elementos en la lista auxiliar con un addfirst para invertirlos
                    if len(auxList1) == k or (grupos > len(self) / k and len(auxList1) == q):  # cuando se llena la primera lista auxiliar con k elementos o con los q restantes
                        add = False # cerramos el condicional de añadir en la lista 1 para abrir el de añadir a la segunda lista
                        i = 0 # reiniciamos el contador
                        grupos += 1  # aumentamos el numero de grupos
                        NodeIt = self._head # reiniciamos también el nodo auxiliar
                if not add and auxList1._head: # en caso de que la lista 1 no este vacía y no se le esten añadiendo elementos añadimos estos a la lista 2
                    auxList2.addLast(auxList1._head.elem)  # añadimos los elementos a la lista 2
                    if auxList1._head:
                        auxList1._head = auxList1._head.next
                    if len(auxList2) == ((grupos - 1) * k) + q: # cuando la lista vaya completando grupos volvemos a activar los booleanos para cumplir las condiciones inciales
                        add = True
                        resetList = True
                i += 1
                if NodeIt:
                    NodeIt = NodeIt.next
            self._head = auxList2._head # movemos el _head de la lista invocante al _head de la lista auxiliar 2 (ya invertida)

        #variante con complejidad espacial cuadrática
        """auxList1 = None          #creamos dos listas auxiliares de la clase Slist2
        auxList2 = SList2()
        NodeIt = self._head         #creamos un nodo auxiliar para recorrer la lista
        i = 0                    # un contador de saltos
        grupos = 1              # un contador de grupos
        resetList1 = True       # un booleano para resetear la lista cuando se agrupen k elementos
        if k <= 1:          # si k<=1 el metodo no hace nada nada
            pass
        else:
            if k > len(self):
                k = len(self)
            while NodeIt:
                if resetList1:          # creamos la lista axuliar 1
                    auxList1 = SList2()
                    resetList1 = False
                auxList1.addFirst(NodeIt.elem)                        #añadimos los elementos en la lista auxiliar con un addfirst para invertirlos
                if grupos > len(self) / k and len(auxList1) < k:   # en el caso de que al final de la lista sobren elementos que no completen un grupo de k elementos
                    k = len(self) - i               #lo hacemos del numero de elementos que quedan
                if len(auxList1) == k:          # cuando se llena la primera lista auxiliar
                    NodeIt2 = auxList1._head        # recorremos la lista aux1 para añadir sus elementos con un addlast (para no invertir el orden) en la lista aux2
                    grupos += 1                 # aumentamos el numero de grupos
                    resetList1 = True          # activamos el bool para resetear la lista 1 cuando se pasen los elementos a la aux2
                    while NodeIt2:           #recorremos la lista
                        auxList2.addLast(NodeIt2.elem)       # añadimos los elementos a la lista 1
                        NodeIt2 = NodeIt2.next
                i += 1
                NodeIt = NodeIt.next
            self._head = auxList2._head                 # movemos el _head de la lista inicial a el _head de la lista aux 2 para eliminar los elementos en el orden original"""



    def maximumPair(self):# este método suma los elementos que equdistan entre sí y devuelve el valor maximo de la suma
        n = 0  # creamos una variable contador de posicion
        m = len(self) - 1  # variable que cuenta la posicion por el final
        if self.isEmpty():  # si la lista esta vacia devolvemos None
            max = None
        else:
            max = 0  # variable que almacenara el valor maximo de las sumas y será retornado por el método
        NodeIt = self._head
        sum = 0
        cont = 0
        while NodeIt:  # recorremos la lista con un nodo auxiliar
            if cont == n and n == m:  # en caso de que la longitud de la lista sea impar el nodo central quedaría sin pareja entonces tenemos en cuenta que n y m coincidirian y el cont también
                sum = NodeIt.elem  # igualamos la variable suma a dicho elemento porque no se suma pero se tiene en cuenta para el maximo
                if sum > max:  # comprobamos si el valor de la suma es mayor que el valor maximo anterior
                    max = sum  # en caso afirmativo cambiamos el maximo
            else:
                if cont == n:  # almacenamos el valor de la posicion n en la suma
                    sum += NodeIt.elem
                if cont == m:
                    sum += NodeIt.elem  # sumamos el valor de la poscion m a la variable suma(que ya tiene el valor de la posicion n)
                    cont = 0 # cuando se encuentra la primera pareja espejo reiniciamos el contador
                    n += 1   #  sumamos una posicion a n para pasar a la siguiente pareja
                    m -= 1   # restamos una posicion a m para pasar a la siguiente pareja
                    NodeIt = self._head # reiniciamos el nodo auxiliar
                    if sum > max:  # comprobamos si el valor de la suma es mayor que el valor maximo anterior
                        max = sum  # en caso afirmativo cambiamos el maximo
                    sum = 0 # reiniciamos la variable suma para que no acumule valores anteriores
            cont += 1
            NodeIt = NodeIt.next
        return max  # devolvemos el valor maximo


    # variante con complejidad espacial cuadrática

    """n = 0               # creamos una variable contador de posicion
        m = len(self)-1                 # variable que cuenta la posicion por el final
        max=0                   # variable que almacenara el valor maximo de las sumas y será retornado por el método
        while n <= len(self)//2:    #creamos un primer bucle que recorra las posiciones (con n y m)
            if self.isEmpty():      # si la lista esta vacia devolvemos None
                max=None
            else:
                NodeIt = self._head
                sum = 0
                cont=0
                while NodeIt:# recorremos la lista con un nodo auxiliar
                    if cont==n and n==m:       # en caso de que la longitud de la lista sea impar el nodo central quedaría sin pareja entonces tenemos en cuenta que n y m coincidirian y el cont también
                        sum=NodeIt.elem        # igualamos la variable suma a dicho elemento porque se no se suma pero se tiene en cuenta para el maximo
                    else:
                        if cont==n:            # almacenamos el valor de la posicion n en la suma
                            sum+=NodeIt.elem
                        if cont==m:
                            sum+=NodeIt.elem   # sumamos el valor de la poscion m a la variable suma(que ya tiene el valor de la posicion n)
                    NodeIt=NodeIt.next
                    cont += 1
                if sum>max:         # comprobamos si el valor de la suma es mayor que el valor maximo anterior
                    max=sum         # en caso afirmativo cambiamos el maximo
            n+=1
            m-=1
        return max              # devolvemos el valor maximo"""

