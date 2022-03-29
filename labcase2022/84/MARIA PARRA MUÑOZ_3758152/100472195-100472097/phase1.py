from slist import SList
import sys


class SList2(SList):

    # method that returns the sum of the last n nodes in the list
    # method complexity: O(n)
    # method complexity: 19
    def sumLastN(self, n):
        suma = 0
        posicion = (len(self) - n)

        # Si n es menor que 0 el método nos devuelve None
        if n < 0:
            return None

        # Si n es 0 el método nos devuelve 0, ya que no hay ningún elemento para sumar
        elif n == 0:
            return 0

        else:
            # Primero comprobamos si la lista está vacía ya que si está vacía no habrá ningún elemento para sumar y por
            # tanto el método nos devuelve 0
            if self.isEmpty():
                return 0

            # Si la lista no está vacía y n es mayor que 0 el método nos devuelve la suma de sus n últimos elementos
            # - Si n es menor que la longitud de la lista el método nos devuelve la suma de sus n últimos elementos
            # - Si n es mayor o igual que la longitud de la lista el método nos devuelve la suma de todos los elementos
            #   de la lista
            # Lo haremos creando un puntero auxiliar con un índice que irá recorriendo la lista hasta la posición
            # que a partir de la cual tiene que empezar a sumar y luego seguirá recorriendola pero ya sumando
            # los elementos
            else:
                current = self._head
                i = 0
                while i < posicion:
                    current = current.next
                    i += 1
                while current:
                    suma += current.elem
                    current = current.next

                return suma

    # ------------------------------------------------------------------------------------------------------------------

    # method for inserting a new node in the middle of the list
    # method complexity: O(n)
    # method complexity: 22
    def insertMiddle(self, elem):
        # Si la lista está vacía simplemente añadimos el elemento
        if self.isEmpty():
            self.addFirst(elem)

        # Si la lista no está vacía insertaremos el elemento (creando una nueva lista con ese elemento como único nodo)
        # en el medio de la lista (dependiendo de su tamañano, par o impar, utilizaremos una fórmula u otra)
        # Lo haremos creando dos punteros auxiliares en la lista original con índices que irán recorriendo la lista
        # hasta la posición que nos interesa (en la que tenemos que insertar el nuevo elemento y su anterior) y
        # posteriormente los conectaremos a la nueva lista con el elemento a insertar
        else:
            if len(self) % 2 == 0:
                posicion = len(self) // 2
            else:
                posicion = (len(self) + 1) // 2

            current1 = self._head
            i1 = 0
            while i1 < (posicion - 1):
                current1 = current1.next
                i1 += 1

            current2 = self._head
            i2 = 0
            while i2 < posicion:
                current2 = current2.next
                i2 += 1

            newList = SList()
            newList.addFirst(elem)
            current1.next = newList._head
            newList._head.next = current2
            self._size += 1

    # ------------------------------------------------------------------------------------------------------------------

    # method for inserting a new list in the position start, but previously removing the original list elements between
    # the positions start and end
    # mehod complexity: O(n)
    # method complexity: 38
    def insertList(self, inputList, start, end):
        # Si los parámetros son incorrectos el método nos devuelve un error
        if start < 0 or start > end or end >= len(self):
            print("Error, parámetros start y/o end incorrectos.")

        # Si los parámetros son correctos debemos borrar los elementos de la lista original entre start y end, y
        # posteriormente insertar la otra lista en la posición start
        # Lo haremos creando punteros auxiliares (uno en la posicion anterior a start, otro en la posición end, y otro
        # en el final de la lista a insertar) para después conectarlos según nos interese dependiendo de cada caso
        else:
            current1 = self._head
            i1 = 0
            while i1 < (start - 1):
                current1 = current1.next
                i1 += 1

            current2 = self._head
            i2 = 0
            while i2 < end:
                current2 = current2.next
                i2 += 1

            current3 = inputList._head
            while current3.next:
                current3 = current3.next

            # Hay casos específicos en los que si start es 0 y la lista a insertar no está vacía, la cabeza de la lista
            # a insertar se convertirá en la nueva cabeza. También dependiendo de la posición end deberemos conectar los
            # punteros de una forma u otra, existe un caso específico (end = (len(self) - 1)) en el que nuestra lista
            # original se borra por completo
            if start == 0:
                if end == (len(self) - 1):
                    if inputList.isEmpty():
                        self._head = None
                        self._size = 0
                    else:
                        self._head = inputList._head
                        self._size = inputList._size
                else:
                    if inputList.isEmpty():
                        self._head = current2.next
                        self._size -= (end + 1)
                    else:
                        self._size -= (end + 1)
                        self._size += inputList._size
                        current3.next = current2.next
                        self._head = inputList._head


            else:
                self._size -= ((end - start) + 1)
                self._size += inputList._size
                current1.next = inputList._head
                current3.next = current2.next

    # ------------------------------------------------------------------------------------------------------------------

    # method for reversing the items of the list in groups of k elements
    # method complexity: O(n)
    # method complexity: 46
    def reverseK(self, k):
        # Si la lista está vacía, no cambia nada. Si no está vacía, ejecutamos el método
        # Lo haremos creando una nueva lista y un puntero auxiliar, mientras exista el puntero (no hayamos terminado de
        # invertir) cogemos cada elemento de la lista con el puntero, empezando por la primera posición, y lo añadiremos
        # al principio de nuestra nueva lista (esta acción ya de por si invierte la lista, puesto que estamos cogiendo
        # de menor a mayor posición en la lista original y lo estamos colocando de mayor a menor posición en la
        # nueva lista)
        if not self.isEmpty():
            invList = SList()
            current = self._head
            while current:
                elemento = current.elem
                invList.addFirst(elemento)
                current = current.next

            # Si el grupo de elementos es mayor o igual que la longitud de la lista original nuestra lista definitiva
            # será la lista completamente invertida (convertimos la nueva lista en la original igualando cabezas)
            if k >= len(self):
                self._head = invList._head

            # Si k <= 1, no se realiza ninguna transformación. Si es mayor que 1 crearemos dos listas auxiliares, una
            # para coger los grupos de k elementos de la lista invertida (separar los grupos para reordenar la lista) y
            # una "definitiva" donde iremos conectando punteros entre dicha lista y la otra auxiliar según el orden
            # correcto
            # Creamos algunas variables númericas para establecer una relación "matemática" en la lista y poder basar
            # el método en contadores y posiciones en un bucle
            elif k > 1:
                defList = SList()

                grupos = (len(self) // k)
                resto = (len(self) % k)
                resto_hecho = False

                kgrupoList = SList()
                contador = 0
                contador_grupos = 0


                while contador_grupos < grupos:
                    current = invList._head
                    elemento = current.elem
                    kgrupoList.addLast(elemento)
                    invList._head = current.next
                    invList._size -= 1
                    contador += 1

                    if resto > 0 and contador == resto and not resto_hecho:
                        defList._head = kgrupoList._head
                        defList._size = kgrupoList._size
                        kgrupoList._head = None
                        kgrupoList._size = 0
                        contador = 0
                        resto_hecho = True

                    if (contador % k) == 0 and contador != 0:
                        if defList.isEmpty():
                            defList._head = kgrupoList._head
                            defList._size = kgrupoList._size
                        else:
                            current1 = kgrupoList._head
                            while current1.next:
                                current1 = current1.next
                            current1.next = defList._head
                            defList._head = kgrupoList._head
                            defList._size += kgrupoList._size

                        kgrupoList._head = None
                        kgrupoList._size = 0
                        contador_grupos += 1

                self._head = defList._head

    # ------------------------------------------------------------------------------------------------------------------

    # method for returning the maximum value of the sum of two equidistant elements of a list
    # method complexity: O(n)
    # method complexity: 36
    def maximumPair(self):
        # Si la lista está vacía el método devuelve None ya que no hay nada que sumar
        if self.isEmpty():
            return None

        # Si la lista está vacía el método nos devuelve directamente el único elemento como máximo
        elif len(self) == 1:
            elemento = self._head.elem
            maximo = elemento
            return maximo

        # Si la lista no está vacía creamos una nueva lista que será la lista original invertida, y mediante punteros
        # auxiliares (uno en la posición n de la lista original, y otro en la misma posición n pero de la lista
        # invertida, por lo que estaremos cogiendo los valores equidistantes) sumaremos los valores equidistantes
        # Para obtener el valor máximo de las sumas creamos una variable llamada máximo cuyo valor inicial es 0, y
        # vamos comparando dicha variable con las respectivas sumas para almacenar el máximo valor
        else:
            maximo = 0

            invList = SList()
            current = self._head
            while current:
                elemento = current.elem
                invList.addFirst(elemento)
                current = current.next

            current1 = invList._head
            current2 = self._head
            suma = current1.elem + current2.elem
            if suma >= maximo:
                maximo = suma

            # Comprobamos si la lista es par o impar, ya que en caso de que sea impar hay un elemento "sobrante" con el
            # que también debemos comparar el máximo
            if (len(self) % 2) != 0:
                # Sumamos en un rango de mitad de la lista menos 1 ya que al ser pares de elementos solo sumamos una
                # vez dichos pares, y menos uno ya que hemos realizado la primera suma fuera del bucle
                for e in range((len(self) // 2) - 1):
                    current1 = current1.next
                    current2 = current2.next
                    suma = current1.elem + current2.elem
                    if suma >= maximo:
                        maximo = suma

                current1 = current1.next
                elemento_sobra = current1.elem
                if elemento_sobra > maximo:
                    maximo = elemento_sobra

            else:
                for e in range((len(self) // 2) - 1):
                    current1 = current1.next
                    current2 = current2.next
                    suma = current1.elem + current2.elem
                    if suma >= maximo:
                        maximo = suma

            return maximo
