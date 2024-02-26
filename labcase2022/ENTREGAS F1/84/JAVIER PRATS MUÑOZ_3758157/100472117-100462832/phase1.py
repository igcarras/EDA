from slist import SList
from slist import SNode
import sys

class SList2(SList):

    # MÉTODO "sumLastN".
    # COMPLEJIDAD: O(n). Hay, a lo sumo, un bucle (es decir, no tiene más bucles anidados).
    # MEJOR CASO: el parámetro "n" es negativo. Devolvemos "None". O(1).
    # PEOR CASO: el parámetro "n" es positivo y menor que el tamaño de la lista. Como consecuencia de ello, tenemos
    # que hacer tanto el bucle "for" como el bucle "while". O(n).
    def sumLastN(self, n):
        # Inicializamos el puntero "current" -que va a estar apuntando a la cabeza de la lista en un inicio- y la
        # variable "m", a la cual le asignamos el valor 0 por defecto.
        current = self._head
        m = 0
        # Si el parámetro "n" es negativo, no hacemos nada.
        if n < 0:
            return None
        # En cambio, si "n" -aparte de ser positivo- es menor que el tamaño de la lista, moveremos el puntero "current"
        # hasta que nos encontremos en el nodo en el cual va a empezar la suma de los elementos de la lista (el
        # nodo "n" si empezamos a contar desde atrás).
        elif n < self.__len__():
            for i in range(self.__len__() - n):
                current = current.next
        # Ahora bien, comenzaremos a sumar los valores de los nodos con ayuda de la variable "m". Cabe destacar que
        # no hemos añadido un "else" en el cual n >= self.__len__(), ya que básicamente lo que tendríamos que hacer es
        # el bucle while escrito abajo. Por otro lado, como el caso en el que n < self.__len__() también requiere dicho
        # bucle, directamente lo escribimos fuera de cualquier condición.
        while current:
            m += current.elem
            current = current.next
        # Devolvemos el valor de la variable "m", que representa la suma de los n últimos nodos de la lista invocante.
        return m

    # MÉTODO "insertMiddle".
    # COMPLEJIDAD: O(n). Hay, a lo sumo, un bucle (es decir, no tiene más bucles anidados).
    # MEJOR CASO: la lista está vacía, con lo cual únicamente tenemos que añadir el elemento (ya sea al principio o
    # al final, es lo mismo). O(1).
    # PEOR CASO: la lista no está vacía y la tenemos que recorrer para encontrar el medio y añadir el nodo en esa
    # posición. O(n).
    def insertMiddle(self, elem):
        # En primer lugar, inicializamos el puntero "current", que en un inicio va a estar apuntando a la cabeza de la
        # lista.
        current = self._head
        # Tenemos que distinguir varios pasos:
        # Si la lista no tiene elementos tampoco tiene medio, con lo cual añadimos "elem" apoyándonos en el método ya
        # creado: "addLast".
        if self.__len__() == 0:
            self.addFirst(elem)
        # Por otro lado, si la longitud de la lista es par, vamos a mover el puntero "current" hasta el nodo anterior al
        # alojado en la posición "self.__len__() // 2", ya que el nuevo nodo irá justo después.
        else:
            if self.__len__() % 2 == 0:
                for i in range((self.__len__() // 2) - 1):
                    current = current.next
            # No obstante, si la longitud de la lista es impar, moveremos el puntero "current" hasta el nodo anterior al
            # alojado en la posición "(self.__len__() + 1) // 2".
            else:
                for i in range(((self.__len__() + 1) // 2) - 1):
                    current = current.next
            # En cualquiera de los dos casos anteriormente mencionados, procederemos de la siguiente manera: creamos un
            # nuevo nodo llamado "nodo", el cual tendrá como elemento el pasado por parámetro. Como el puntero "current"
            # está justo en la posición previa, "nodo" apuntará al siguiente de "current" (que era originalmente el nodo
            # que estaba en la posición que se va a ocupar ahora). Ahora, para que el nuevo nodo quede completamente
            # integrado en la lista, el puntero "current" tendrá como nodo siguiente a "nodo".
            nodo = SNode(elem)
            nodo.next = current.next
            current.next = nodo
            # Tenemos que incrementar en uno, claro está, el tamaño de la lista.
            self._size += 1

    # MÉTODO "insertList".
    # COMPLEJIDAD: O(n). Hay, a lo sumo, un bucle (es decir, no tiene más bucles anidados).
    # MEJOR CASO: si el parámetro "start" es negativo, el parámetro "start" es mayor que el parámetro "end" o "end"
    # es mayor o igual al tamaño de la lista, no hacemos ninguna modificación y devolvemos "None". O(1).
    # PEOR CASO: tenemos que recorrer la lista para averiguar el comienzo y el final de la lista "inputList". O(n).
    def insertList(self, inputList, start, end):
        # Vamos a considerar varios escenarios posibles.
        # El primero, si el parámetro "start" es negativo, el parámetro "start" es mayor que el parámetro "end" o "end"
        # es mayor o igual al tamaño de la lista, no hacemos ninguna modificación en la misma.
        if start < 0 or start > end or end >= self.__len__():
            return None
        # Por otro lado, si start = 0.
        elif start == 0:
            # Si end = (self.__len__() - 1) -el último nodo-, directamente cambiamos la lista invocante por "inputList".
            if end == (self.__len__() - 1):
                self._head = inputList._head
            else:
                current1 = self._head
                current2 = inputList._head
                # En este caso, recorremos la lista invocante con "current1", llegando este al nodo siguiente cuyo
                # índice es "end + 1".
                for i in range(end + 1):
                    current1 = current1.next
                # En cuanto a "current2", lo posicionamos en el último nodo de "inputList" y, para
                # añadirla a la "lista general", hacemos que su último nodo apunte a "current1".
                while current2.next:
                    current2 = current2.next
                current2.next = current1
                # Posteriormente, decimos que la cabeza de la lista invocante pasa a ser la de "inputList", ya que
                # start = 0.
                self._head = inputList._head
        # Si start != 0.
        else:
            # Si end = (self.__len__() - 1) -el último nodo-.
            if end == self.__len__() - 1:
                current1 = self._head
                # Movemos "current1" hasta el nodo cuyo índice es "start - 1".
                for i in range(start - 1):
                    current1 = current1.next
                # Ahora, "current1" va a apuntar a la cabeza de "inputList", cuyo último elemento será el último de
                # la lista (porque end = (self.__len__() - 1)).
                current1.next = inputList._head
            else:
                # Si start != 0 y end != (self.__len__() - 1) -caso general-.
                current1 = self._head
                current2 = self._head
                current3 = inputList._head
                # Posicionamos el puntero "current1" hasta el nodo cuyo índice es "start - 1".
                for i in range(start - 1):
                    current1 = current1.next
                # Posicionamos el puntero "current1¡2" hasta el nodo cuyo índice es "end + 1".
                for i in range(end + 1):
                    current2 = current2.next
                # Ahora bien, el puntero "current3" va a recorrer "inputList" hasta llegar al último nodo. Dicho nodo
                # pasará de apuntar a "None" a "current2", y "current1" apuntará a la cabeza de la lista. De esta
                # manera, hemos incluido la lista "inputList" en una posición genérica de la lista invocante.
                while current3.next:
                    current3 = current3.next
                current3.next = current2
                current1.next = inputList._head

    # MÉTODO "reverseK".
    # COMPLEJIDAD: O(n^3). Como en un momento llamamos al método "addLast" y este tiene un bucle en su interior;
    # como dicha llamada se hace dentro de un bucle que además está anidado a otro bucle, causa que la complejidad sea
    # cúbica.
    # MEJOR CASO: si el parámetro "k" es menor o igual a 1. En este caso devolvemos "None". O(1).
    # PEOR CASO: tenemos que recorrer la lista, añadir los valores invertidos a "AuxList1" y, posteriormente,
    # hacer un "addLast" en "AuxList2". De esta forma tendremos la lista invocante con los valores invertidos en
    # grupos de "k" elementos. O(n^3).
    def reverseK(self, k):
        # Vamos a considerar una serie de casos:
        # Si el parámetro "k" es menor o igual a uno, no hacemos ninguna modificación en la lista invocante.
        if k <= 1:
            return None
        # Si el parámetro "k" es mayor o igual que la longitud de la lista, la invertimos entera.
        elif k >= self.__len__():
            current = self._head
            AuxList = SList()
            # En una lista auxiliar "AuxList" vamos añadiendo los valores de la lista invocante de manera que estén
            # invertidos (el elemento del último nodo es el primero y viceversa).
            for i in range(self.__len__()):
                AuxList.addFirst(current.elem)
                current = current.next
            # Ahora, para trasladar este cambio a la lista general, únicamente movemos el puntero de la cabeza a la
            # cabeza de dicha lista auxiliar.
            self._head = AuxList._head
        else:
            # En el caso "general" -y más importante- tenemos los siguientes parámetros a destacar: puntero "current1",
            # que está en un primer momento en la cabeza de la lista invocante. Por otro lado, definimos dos listas
            # auxiliares: "AuxList1" y "AuxList2".
            current1 = self._head
            AuxList1 = SList()
            AuxList2 = SList()
            # Mientras current1 != None, vamos a ir recorriendo la lista e invirtiendo sus valores consecutivamente.
            while current1:
                # Si el parámetro "k" es menor o igual que la longitud de la lista, procedemos de la siguiente manera.
                if k <= self.__len__():
                    # Añadimos "k" elementos invertidos a la lista auxiliar "AuxList1". Conforme vamos añadiendo
                    # los valores, eliminamos su nodo correspondiente en la lista general.
                    for i in range(k):
                        AuxList1.addFirst(current1.elem)
                        current1 = current1.next
                        self._head = current1
                        self._size -= 1
                # Si el parámetro "k" es mayor que la longitud de la lista, procedemos de esta otra manera.
                else:
                    # Como hemos estado borrado periódicamente los nodos de la lista, podemos llegar a un punto en el
                    # que, por ejemplo, el parámetro "k" nos pida invertir 4 valores y a nosotros únicamente nos queden
                    # 2. Llegados a dicho punto, vamos a usar un bucle while en vez de un for. De esta manera podemos
                    # estar seguros de que, aunque no sea la cantidad requerida por "k", los valores restantes se
                    # invertirán de todas formas.
                    while current1:
                        AuxList1.addFirst(current1.elem)
                        current1 = current1.next
                        self._head = current1
                        self._size -= 1
                # Ahora bien, llega el momento de ir añadiendo los valores invertidos en la otra lista auxiliar:
                # "AuxList2".
                current2 = AuxList1._head
                # Operamos de la misma manera que en la lista invocante: conforme vayamos añadiendo valores a
                # "AuxList2", los eliminamos de "AuxList1". Así, "AuxList1" puede volver a ser usada en el bucle para
                # alojar más elementos invertidos.
                while current2:
                    AuxList2.addLast(current2.elem)
                    current2 = current2.next
                    AuxList1._head = current2
            # Cuando ya hemos terminado, simplemente movilizamos el puntero "_head" de la lista general al de la lista
            # auxiliar "AuxList2".
            self._head = AuxList2._head
            # Además, como hemos estado decrementando el tamaño de la lista invocante, ahora tenemos que self._size = 0.
            # Para solucionar esto, decimos que el valor actual de self._size es el de la "AuxList2", osea, el de la
            # lista original.
            self._size = AuxList2._size

    # MÉTODO "maximumPair".
    # COMPLEJIDAD: O(n^2). Tenemos, a lo sumo, dos bucles anidados, causando así que la complejidad sea cuadrática.
    # MEJOR CASO: si el parámetro "k" es negativo o es igual a 0. En el primer caso devolvemos "None"; en el segundo,
    # el elemento del único nodo que alberga la lista. O(1).
    # PEOR CASO: k >= 1. Nos introducimos en el bucle "while". O(n^2).
    def maximumPair(self):
        # Definimos una lista auxiliar, dos punteros que apuntan a la cabeza de la lista invocante y una variable que
        # tiene como valor el tamaño de la lista - 1.
        AuxList = SList()
        current1 = self._head
        current2 = self._head
        k = self._size - 1
        # Si la lista está vacía, no hacemos nada.
        if k < 0:
            return None
        # Si solo tenemos un elemento, lo devolvemos.
        elif k == 0:
            return self._head.elem
        # En cualquier otro caso, vamos a realizar el siguiente bucle, que se ejecutará siempre y cuando el tamaño de
        # la lista auxiliar no haya alcanzado el mismo valor que el de la lista invocante.
        # La idea es la siguiente: vamos a ir añadiendo los elementos equidistantes de la lista a la auxiliar y,
        # posteriormente, vamos a sumarlos de dos en dos para averiguar cual es el número máximo resultante de sumar
        # los pares.
        while self._size != AuxList._size:
            # Movemos el puntero "current2" al equivalente de "current1" pero empezando por detrás.
            for i in range(k):
                current2 = current2.next
            # Si el tamaño de la lista es impar, vamos a llegar a un punto en el que ambos punteros coincidan en un
            # mismo nodo -el nodo situado en la mitad-. Por ende, solo añadimos un único elemento, ya sea el de
            # "current1" o el de "current2", da igual.
            if current1 == current2:
                AuxList.addLast(current1.elem)
            # En cuaquier otro caso, añadimos tanto el elemento de "current1" como su equivalente en "current2".
            else:
                AuxList.addLast(current1.elem)
                AuxList.addLast(current2.elem)
            # Actualizamos los punteros y la variable "k".
            current1 = current1.next
            current2 = self._head
            k -= 1
        # Ahora, vamos a ir recorriendo la lista auxiliar, que tiene dispuestos los elementos equidistantes uno detrás
        # del otro. Ambos elementos van a estar apuntados por "current3" y "current4" respectivamente, y dependiendo
        # del valor de la variable "max" -que inicialmente es "None"- se actualizará esta última o no como un nuevo
        # valor máximo.
        current3 = AuxList._head
        current4 = AuxList._head.next
        max = None
        while current3:
            if current4:
                if not max:
                    max = current3.elem + current4.elem
                else:
                    if max < (current3.elem + current4.elem):
                        max = current3.elem + current4.elem
                current3 = current4.next
                # "If" específico para cuando tengamos solo dos elementos. En tal caso no podemos hacer
                # "current4 = current3.next", porque current4 es el elemento final, así que "current3 = current4.next"
                # es como si dijeramos "current3 = None", por ende, no podemos hacer el ".next" de None.
                if current3:
                    current4 = current3.next
                else:
                    current4 = None
            # Si no existe "current4" -es decir, estamos en el elemento que se encontraba en el nodo de la mitad de la
            # lista invocante (suponiendo que esta tuviese un tamaño impar)-, vamos a ver si el valor de este elemento
            # se vale por sí solo como el número máximo.
            else:
                if max < current3.elem:
                    max = current3.elem
                current3 = None
        # Devolvemos el valor máximo.
        return max





