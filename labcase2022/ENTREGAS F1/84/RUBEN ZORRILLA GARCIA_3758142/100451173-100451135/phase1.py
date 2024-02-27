class SNode:
    def __init__(self, e, next=None):
        self.elem = e  # 1
        self.next = next  # 1


class SList:
    """This is the implementation of a singly linked list. We only use 
    a reference to the first node, named _head"""

    def __init__(self):
        """This constructor creates an empty list"""
        self._head = None
        self._size = 0

    def __len__(self):
        """It returns the _size of the list"""
        return self._size

    def isEmpty(self):
        """"It returns True if the list is empty, and False eoc"""
        # return self._head == None
        return len(self) == 0

    def __str__(self):
        """Returns a string with the elements of the list"""
        result = ''

        nodeIt = self._head

        while nodeIt != None:  # nodeIt!=None           
            result += str(nodeIt.elem) + ", "
            nodeIt = nodeIt.next

        if len(result) > 0:
            result = result.strip()
            result = result[:-1]

        return "[" + result + "]"

    def addFirst(self, e):
        """Add a new element, e, at the beginning of the list"""
        newNode = SNode(e)
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    def addLast(self, e):
        """This functions adds e to the end of the list"""
        newNode = SNode(e)

        if self.isEmpty():
            self._head = newNode
        else:
            # we move throught the list until to reach the last node
            lastNode = self._head
            while lastNode.next:  # lastNode.next!=None
                lastNode = lastNode.next
            # now, lastNode is the last node
            # the last node must point to the new node (which will be the new last node)
            lastNode.next = newNode
        self._size += 1

    def removeFirst(self):
        """Removes the first element of the list"""
        result = None
        if self.isEmpty():
            print('Error: list is empty!')
        else:
            # gets the first element, which we will return later
            result = self._head.elem
            # updates _head to point to the new _head (the next node)
            self._head = self._head.next
            self._size -= 1

        return result

    def removeLast(self):
        """removes and returns the last node of the list. 
        If the list is empty, it prints an error and returns None"""
        result = None
        if self.isEmpty():
            print('Error: list is empty!')
        elif len(self) == 1:
            result = self.removeFirst()  # O(1)
        else:
            penult = None
            lastNode = self._head
            while lastNode.next:
                penult = lastNode
                lastNode = lastNode.next

            result = lastNode.elem
            penult.next = None

            self._size -= 1

        return result

    def getAt(self, index):
        """return the element at the position index.
        If the index is an invalid position, the function
        will return -1"""
        result = None
        if index not in range(0, len(self)):
            print(index, 'Error getAt: index out of range')
        else:
            nodeIt = self._head
            i = 0
            while nodeIt and i < index:
                nodeIt = nodeIt.next
                i += 1

            # nodeIt is at the position index
            result = nodeIt.elem

        return result

    def index(self, e):
        """returns the first position of e into the list.
        If e does not exist in the list, 
        then the function will return -1"""
        nodeIt = self._head
        index = 0
        while nodeIt:
            if nodeIt.elem == e:
                return index
            nodeIt = nodeIt.next
            index += 1

        # print(e,' does not exist!!!')
        return -1

    def insertAt(self, index, e):
        """This methods inserts a new node containing the element e at the index
        position in the list"""

        # first, we must check that index is a right position. 
        # Please, Note that index=len()+1 would be a right position
        # to insert a new element
        if index not in range(0, len(self) + 1):
            print(index, 'Error insertAt: index out of range')
        elif index == 0:
            self.addFirst(e)
        elif index == len(self):
            self.addLast(e)
        else:
            # we need to reach the previous node (the node at the index-1 position)
            previous = self._head
            for i in range(index - 1):
                previous = previous.next

            # now, previous is the node with index-1
            # create the new node
            newNode = SNode(e)
            # newnode must point to the node after previous (which is previous.next)
            newNode.next = previous.next
            # previous must point with its next reference to the new node
            previous.next = newNode
            self._size += 1

    def removeAt(self, index):
        """This methods removes the node at the index position in the list"""
        result = None
        # We must check that index is a right position in the list
        # Remember that the indexes in a list can range from 0 to _size-1
        if index not in range(len(self)):
            print(index, 'Error removeAt: index out of range')
        elif index == 0:
            result = self.removeFirst()
        elif index == len(self) - 1:
            result = self.removeLast()
        else:
            # we must to reach the node before the node at the index position
            previous = self._head
            for i in range(index - 1):
                previous = previous.next

            # previous is the node at index -1 position
            # previous.next is the node at index position
            result = previous.next.elem
            previous.next = previous.next.next
            self._size -= 1

        return result

class SList2(SList):

    def sumLastN(self, n):
        index = 0
        nueva_lista = 0
        nodeIt = self._head
        media = (len(self)) - n
        # aqui hacemos la comprobaciones que nos obliga el enunciado y tmb hallamos las variables que usaremos
        # como apoyo para realizar correctamente el metodo
        if n < 0 or self._size < 0:
            return None
        elif n == 0:
            return n
        if n > len(self): # aqui cuando n es mayor que len(self)
            #y a parte se sumarian los elementos y pasariamos al siguiente nodo
            while nodeIt:
                nueva_lista += nodeIt.elem
                nodeIt = nodeIt.next
        else:
            # Si n no es mayor que len(self), sumamos los n ultimos elementos
            while nodeIt:
                if index < media:
                    nodeIt = nodeIt.next
                    index +=1
                #cuando index < media seguimos sumando al contador
                else:
                    nueva_lista += nodeIt.elem
                    nodeIt = nodeIt.next
        return nueva_lista

    # La complejidad de este método es O(n) ya que no hay bucles anidados, solo bucles sueltos
    # el mejor/peor caso es : cuando o n <=0, y el peor caso es que tenga que recorrer toda la lista

    def insertMiddle(self, elem):
        media = len(self) // 2 # aqui partimos y encontramos el valor del medio

        if len(self)%2 != 0:
            media +=1
        elif media == 0: # esto quiere decir que que media esta al principio # aqui tmb podemos poner self is empty
            self.addFirst(elem)
        #en la parte de arriba realizamos los requisitos iniciales y luego seguir con el resto de tipos
        else:
            a = SNode(elem)
            nodeIt = self._head
            for x in range(media-1):
                nodeIt = nodeIt.next
            a.next = nodeIt.next
            nodeIt.next = a
            self._size +=1
        return
    # el mejor caso es que este vacia la lista ya que se añade al principio// el pero caso es cuando se usa insertmiddle
    # en una lista larga
    # La complejidad de este método es O(1) ya que no hay bucles
    def insertList(self,inputList,start,end):
        # Este método iserta una lista en otra entre las posiciones start y end de la principal,
        # borrando esos elementos
        if start > self._size or end > self._size or end < start:
            return
        else:
            s1 = 0
            s2 = start
            nodeit = inputList._head
            # Aquí vamos añadiendo y quitando elementos a la lista principal en función de la inputlist
            while s1 < (1 + end - start) and nodeit !=None:
                self.removeAt(s2)
                self.insertAt(s2,nodeit.elem)
                nodeit = nodeit.next
                s2 += 1
                s1 += 1
            # La complejidad de este método es O(n^2) ya que hay bucles anidados
            # el mejor caso es el requisito inicial que nos obliga el enunciado
            # el peor caso es cuando tienes que recorrer toda la lista y los valores start end estar juntos

    def reverseK(self,k):
        # Este método hace reverse en grupos de k elementos a la lista
        '''nodeIt = self._head
        index = 0
        index_final = len(self)
        if k <= 1:
            return
        elif k == len(self):
            return self[::-1] # es decir aqui devuelve la lista al reves
        else:
            while nodeIt:
                if index != k or index:
                    index +=1'''
        if len(self) <= 0:
            # Si la len de la lista es <= 0, la función acaba sin hacer nada
            print('Error, la lista está vacía')
            return

        elif k <= 1:
            # Si k <= 1, la lista se devuelve sin modificar
            return self

        elif k > len(self):
            # Si k > len(self), es decir, mayor que la longitud de la lista, esta se hace reverse
            # en su totalidad
            index = self._size
            aux = SList()
            c = 0
            while c < self._size:
                # Con este bucle añadimos a una lista auxiliar (aux) los elementos revertidos de la principal
                NewNode = SNode(self.getAt(index))
                aux.addLast(NewNode)
                c += 1
                index -= 1
            while self._size > 0:
                # Aquí borramos todos los elementos de la lista principal
                self.removeFirst()
            nodeIt = aux._head
            while nodeIt:
                # Por último, añadimos los elementos de la lista auxiliar a la principal y devolvemos la lista
                self.addLast(nodeIt.elem)
                nodeIt = nodeIt.next
            return self

        else:
            # Si k es menor que la len de la lista, revertimos por grupos los elementos
            aux = SList()
            grupos = len(self)//k
            index = (k - 1) * grupos
            while grupos > 0:
                c = k
                while c != 0:
                    NewNode = SNode(self.getAt(index))
                    aux.addLast(NewNode)
                    self.removeAt(index)
                    index -= 1
                    c -= 1
                grupos -= 1
            nodeit = aux._head
            while nodeit:
                self.addLast(nodeit)
                nodeit = nodeit.next
            return self
    # La complejidad de este método es O(n^2) ya que hay llamada a otro método dentro de un bucle
    # teniendo ese método bucles internos
    # el mejor caso es cuadno la lista esta vacia
    # el peor caso es cuando hay una lista muy larga y tenemos que hacer reverse con valores k muy pequeños

    def maximumPair(self):
        # aqui añadimos el tres variables index que reccore
        # todo e index2 que es la longitud -1

        index1 = 0
        index2 = len(self) - 1
        nodeit = self._head
        valor = 0

        if len(self) < 1:
            return None  # return N
        elif len(self) == 1:
            return nodeit.elem

        else:
            while index1 <= index2:
                # aqui recorrera toda la lista dada hasta que llegue al final de la misma
                nodeIt = self._head
                x = 0
                while index1 > x: # recorre index 1 cuando sea mayor que uno
                    nodeIt = nodeIt.next
                    x += 1
                a = nodeIt.elem
                while index2 > x:  # se recorre pq queremos llegar hasta el segundo valor,
                    nodeIt = nodeIt.next
                    x += 1
                b = nodeIt.elem
                if index1 == index2: #si son iguales, como nos dicen el enunciado hay que dividirlo entre
                    # dos la suma
                    suma = (a + b) / 2
                else:
                    suma = a + b
                if valor < suma:
                    valor = suma
                index1 += 1
                index2 -= 1

        return valor
        # La complejidad de este metodo es O(n^2) ya que hay bucles anidados
        # el mejor caso  es cuando len(self) <=1
        # el peor caso es cuando la lista es muy larga y y longitud impar

















