from slist import SList
from slist import SNode


class SList2(SList):

    def sumLastN(self, n):
        if n < 0:
            return None

        elif n == 0 or self._size == 0:
            return 0

        else:
            sum = 0
            aux = self._head
            index = 0
            while aux is not None:
                # Creamos un puntero auxiliar que recorra toda la lista
                if index >= (self._size - n):
                    # Si el índice es mayor o igual que el tamaño de la lista menos n lo sumamos
                    sum += aux.elem
                index += 1
                aux = aux.next
            return sum

    def insertMiddle(self, elem):
        # Si la lista esta vacía creamos un nuevo nodo, con valor elem, y hacemos que sea el _head de la lista
        if self._size == 0:
            mid_node = SNode(elem)
            self._head = mid_node
            self._size+=1

        # Si el tamaño de la lista es par:
        elif self._size % 2 == 0:
            # Creamos el nodo que insertaremos en la mitad de la lista, y un puntero auxiliar
            mid_node = SNode(elem)
            aux = self._head

            # Con un for recorremos la lista hasta encontrar el nodo anterior y el nodo posterior a la mitad
            for n in range((self._size // 2) - 1):
                aux = aux.next
                post_aux = aux.next
            mid_node.next = post_aux
            aux.next = mid_node
            self._size+=1

        # Lo mismo para el caso en el que el tamaño de la lista impar, pero recorriendo una posicion mas la lista
        elif self._size % 2 != 0:
            mid_node = SNode(elem)
            aux = self._head

            for n in range((self._size // 2)):
                aux = aux.next
                post_aux = aux.next
            mid_node.next = post_aux
            aux.next = mid_node
            self._size+=1

    def insertList(self, inputList, start, end):
        if start < 0 or start > end or end >= self._size:
            print("Error en los parámetros")

        # Si la lista original esta vacía, convertimos la lista aux en la lista original
        elif self._size == 0:
            self._head = inputList._head
            self._size = inputList._size


        elif end == start == 0:
            new_tail = self._head.next
            self._head = inputList._head
            aux = self._head
            while aux.next is not None:
                aux = aux.next
            aux.next = new_tail
            self._size = self._size - 1 + inputList._size

        else:

            current = self._head
            index = 0
            while index <= end and index <= self._size - 1:
                if start - 1 < 0:
                    current = current.next
                    self._head = inputList._head

                elif index == start - 1:
                    previous = current
                    current = current.next
                    previous.next = inputList._head
                else:
                    current = current.next

                index += 1
            aux = self._head
            while aux.next is not None:
                aux = aux.next
            aux.next = current
            self._size = self._size + inputList._size - (end - start + 1)

    def reverseK(self, k):

        aux = self._head
        #reversed_list será la lista revertida
        reversed_list = SList2()

        while aux:

            # Lista auxiliar para invertir los k grupos
            aux_list = SList2()
            for n in range(k):
                if aux is not None:
                    aux_list.addFirst(aux.elem)
                    aux = aux.next


            if not reversed_list._head:
                reversed_list._head = aux_list._head

            else:
                aux_2 = reversed_list._head
                while aux_2.next is not None:
                    aux_2 = aux_2.next
                aux_2.next = aux_list._head

        if reversed_list._head:
            self._head = reversed_list._head

    def maximumPair(self):
        if self._size == 0:
            return None

        elif self._size == 1:
            return self._head.elem

        else:
            #Lista donde almacenaremos las sumas
            lista_max = SList()
            #Lista auxiliar, idéntica a la original, en la que iremos eliminando elementos
            lista_aux = SList()
            aux = self._head
            for n in range(self._size):
                lista_aux.addLast(aux.elem)
                aux = aux.next

            # Si la lista es par:
            if self._size % 2 == 0:
                for n in range(self._size // 2):
                    # aux_2 apuntará al último elemento de la lista y previous al penúltimo
                    aux_2 = lista_aux._head
                    previous = None
                    while aux_2.next is not None:
                        previous = aux_2
                        aux_2 = aux_2.next
                    # Sumamos el primer y el último elemento a la lista_max(sumas), y despues los eliminamos
                    lista_max.addLast(lista_aux._head.elem + aux_2.elem)
                    lista_aux._head = lista_aux._head.next
                    previous.next = None

            # En caso de que el tamaño sea impar, hacemos lo mismo que en el caso par, pero sumando el elemento libre a list_max
            if self._size % 2 != 0:
                for n in range(self._size // 2):
                    aux_2 = lista_aux._head
                    previous = None
                    while aux_2.next is not None:
                        previous = aux_2
                        aux_2 = aux_2.next
                    lista_max.addLast(lista_aux._head.elem + aux_2.elem)
                    lista_aux._head = lista_aux._head.next
                    previous.next = None
                lista_max.addLast(lista_aux._head.elem)

            # Comprobamos cual de los elementos de la lista_max es mayor y lo devolvemos
            max = -99999999999999
            aux = lista_max._head
            for n in range(lista_max._size):
                if aux.elem > max:
                    max = aux.elem
                aux = aux.next
            return max



