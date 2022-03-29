from slist import SList, SNode
import sys

class SList2(SList):

    """Metodo para sumar los n ultimos numeros"""
    def sumLastN(self, n):
        "Excepciones"
        if n < 0: return None
        elif n == 0 or self.isEmpty(): return 0
        elif n > (len(self)): n = len(self)

        "Metodo general"
        resultado = 0  #Almacena la suma
        checkNode = self._head  #Almacena el elemento a sumar a sumar

        "Desplazar checkNode"
        for i in range(len(self) - n):
            checkNode = checkNode.next

        "Suma"
        for i in range(n):
            resultado += checkNode.elem
            checkNode = checkNode.next

        return resultado

    """Metodo para insertar un nuevo nodo en el medio"""
    def insertMiddle(self, elem):

        "Asigna el valor de index en funcion de si es par o no"
        if self._size % 2 == 0:
            index = len(self)//2
        else:
            index = (len(self)+1)//2

        "Introduce el elemento"
        #Comprueba si la posicion es la primera
        if index == 0:
            self.addFirst(elem)

        #Entre medias
        else:
            previous = self._head #Nodo anterior a la poosicion que queremos insertar
            for i in range(index - 1):
                previous = previous.next
            newNode = SNode(elem) #Creamos el nodo con el elem a insertar
            newNode.next = previous.next #El nuevo nodo apunta al siguiente de su posicion
            previous.next = newNode #El anterior nodo pasa a apuntar al nuevo

            self._size += 1

    """Metodo para insertar otra lista entre dos parametros"""
    def insertList(self,inputList,start,end):

        if 0 <= start <=end and 0 <= end < len(self):
            "1 nodo auxiliar"
            node1 = self._head
            #Se le asigna el nodo anterior al start
            for i in range(start-1):
                node1 = node1.next

            "2 nodo auxuliar"
            node2 = self._head
            #Se le asigna el nodo del end
            for i in range(end):
                node2 = node2.next

            "Ultimo nodo lista auxiliar"
            inputList._tail = inputList._head
            for i in range(len(inputList)-1):
                inputList._tail = inputList._tail.next

            "Enlazar listas"
            #Excepcion
            if start == 0:
                self._head = inputList._head
            #Enlazar el principio
            else:
                node1.next = inputList._head
            #Enlazar el final
            inputList._tail.next, node2.next = node2.next, None

            self._size = self._size + inputList._size - (end - start + 1)


    """Metodo para invertir elementos en grupos"""
    def reverseK(self,k):
        if not k <= 1:
            "Variables auxiliares"
            stack = SList()  #Lista para meter los grupos
            reverse = SList() #Lista original al reves
            contador = 0 #Int para comprobar cuando se ha llenado un grupo

            "Llena reverse"
            for i in range(len(self)):
                #Llena la pila
                stack.addLast(self.removeFirst())
                contador += 1

                #Vacia la pila y lo mete al reverse
                if contador % k == 0:
                    for i in range(len(stack)):
                        reverse.addLast(stack.removeLast())

            #Meter los elementos que sobran
            if k > len(self):
                for i in range(len(stack)):
                    reverse.addLast(stack.removeLast())

            "La original pasa a ser la reverse"
            self._head = reverse._head


    """Metodo que devuelve la mayor suma de los elementos equidistantes"""
    def maximumPair(self):
        if not self.isEmpty():
            "Variables"
            max = 0 #Valor maximo a devolver
            copyList = SList() #Copia de la lista original
            for i in range(len(self)):
                copyList.addLast(self.getAt(i))

            "Determinar suma maxima"
            while not copyList.isEmpty():
                #Asignacion de la variable suma
                if len(copyList) > 1:
                    suma = copyList.removeFirst() + copyList.removeLast()
                else:
                    suma = copyList.removeFirst()

                #Actualizacion de la variable max
                if max < suma:
                    max = suma

            return max