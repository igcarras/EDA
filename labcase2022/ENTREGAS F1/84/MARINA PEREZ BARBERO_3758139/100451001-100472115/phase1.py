from slist import SList
from slist import SNode
import sys
# Marina Pérez Barbero 100472115
# Jorge Ramos Santana 100451001

class SList2(SList):
    _head = None

    def sumLastN(self, n):
        "Este metodo se encarga de sumar los n últimos elementos"\
        "Complejidad: O(n)"

        current = self._head
        currentnum = 0
        total = 0

        if n < 0:
            return None
        elif n == 0:
            return 0
        " En caso de que n sea menor que 0 devuelve None y si n es igual a 0 devuelve 0 "


        while current and currentnum <= self.__len__() - n - 1:
            current = current.next
            currentnum += 1
        "Este while te recorre la lista hasta la posición anterior que vas a sumar"


        while current and currentnum <= self.__len__():
            total += current.elem
            currentnum += 1
            current = current.next
        "Este while termina de recorer la lista y va sumando todos los elementos por los que va pasando"

        return total





    def insertMiddle(self, elem):
        "Este metodo se encarga de insetar un elemento en mitad de la lista"
        "Complejidad: O(n)"

        if self.isEmpty():
            self.addFirst(elem)
            "Si la lista esta vacia añade el elemento"

        else:
            if self.__len__() % 2 == 0:
                pos = len(self) // 2
                "Si la lista es par se añade en la posicion del medio "
            else:
                pos = (len(self) + 1) / 2
                "Si la lista es inpar se añade en la posicion del medio mas 1"

            current = self._head
            pos_current = 0
            previus = None

            while pos_current != pos:  
                previus = current  
                current = current.next
                pos_current += 1
            "Mientras que las posicion del puntero current no llegue a mitad de la lista, se va recorriendo"

            newNode = SNode(elem)
            previus.next = newNode  
            newNode.next = current  
            self._size += 1  
            "Se conecta el nuevo nodo a la lista y se aumenta el tamañno"



    def insertList(self, inputList, start, end):
        "Metodo que inserta una lista"
        "Complejidad: O(n)"
        if start < 0 or start > end or end >= self.__len__():
            return

        currentl = self._head
        currentlnum = 0
        currentr = self._head
        currentrnum = 0
        othernode = inputList._head
        other = 0

        while currentl and currentlnum <= start - 2:
            currentl = currentl.next
            currentlnum += 1
        """
        La función tiene dos punteros (currentl y currentr), y dos contadores(currentlnum y currentrnum). Los punteros son el nodo; el contador es
        simplemente un numero que indica el indice del nodo actual. 
        El primer bucle avanza hasta el nodo anterior al que queremos eliminar. Uso "start-2" porque el contador empieza en 0 (por lo que se le r
        esta uno) y porque me interesa quedarme en el nodo anterior (por lo que se le resta otro uno) ya que al hacer node.next
        ya elimino el nodo correcto.
        """

        while currentr and currentrnum <= end - 1:
            print("RIGHT", currentr.elem)
            currentr = currentr.next
            currentrnum += 1
        """
        Misma idea que el bucle anterior, solo que en este caso nos quedamos en el mismo nodo que vamos a eliminar, no en el anterior. (por que?) 
        Al hacer node.next ya vamos al siguiente nodo
        """

        if start == 0:
            self._head = inputList._head
        else:
            currentl.next = inputList._head
        """
        En caso de que start sea 0, el primer elemento de nuestra lista self será reemplazado por inputList. De no ser así, operamos
         normalmente con el puntero obtenido en primer bucle.
        """

        while othernode and other < inputList.__len__() - 1:
            print("OTHERELEM", othernode.elem)
            othernode = othernode.next
            other += 1
        """
        Avanzamos por la inputList hasta llegar a su último nodo, para luego volver a enlazarlo a la lista self
        """


        if end < self.__len__() - 1:
            othernode.next = currentr.next
        """
        Volveremos a unir inputList a self SALVO QUE end sea igual a la longitud de la lista self, en cuyo caso inputList será la nueva "colilla" 
        (no confundir "colilla" con el último nodo de una lista "tail")
        """




    def reverseK(self, k):
        "Se encarga de da intercambiar la posicion de K elementos seguidos de la lista"
        "Complejidad: O(n^2)"
        aux1 = SList2()
        aux2 = SList2()
        cur = aux2._head

        while self._head:
            "El bucle se repite hasta que no haya elementos en la lista"

            pos_p = 0
            while pos_p < k and self._head:
                aux1.addFirst(self.removeFirst())
                pos_p += 1
            "Recorre cada intervalo de k y lo añade invertido a la lista aux 1"

            if cur == None:
                aux2._head = aux1._head
                cur = aux2._head
            else:
                cur.next = aux1._head
            "Se añade la lista aux1 al final de la lista 2"

            aux1._head = None
            "Se borra la lista 1 "

            while cur.next != None:
                cur = cur.next
            "Se mueve el puntero cur al final de la lista"

        self._head = aux2._head
        "La lista 2 se convierete en la principal"




    def maximumPair(self):
        "Este metodo se encarga de decir que pareja de max es mayor"
        "Complejidad: O(n^2)"

        if self.isEmpty():
            print("Error la lista esta vacia")
            return None

        pos_in = 0
        s = SList2()
        pos_me = self.__len__() // 2 - 1

        while pos_in <= pos_me:
            suma = 0
            pos_fi = self.__len__() - 1 - pos_in
            suma = self.getAt(pos_in) + self.getAt(pos_fi)
            s.addFirst(suma)
            pos_in += 1
        """
        Se recorre la lista hasta la mitad mientras se van sumando los elementos equidistantes.
        El resultado se añade a una lista auxiliar
        """

        if self.__len__() % 2 != 0:
            pos_m = self.__len__() // 2
            s.addFirst(self.getAt(pos_m))
            "Si la lista es impar, se añade el nodo del medio"

        max = -100
        current = s._head
        while current:
            if current.elem > max:
                max = current.elem
            current = current.next
        return max
        "Se develve el mayor elemento de la lista auxiliar"
