from slist import SList
from slist import SNode

import sys


class SList2(SList):

    def delLargestSeq(self):

        # Primero, planteamos el caso de que la lista esté vacía

        if self.isEmpty():
            print("Error: la lista está vacía")


        # Comprobamos el caso de que exista un solo elemento en la lista

        elif self._size == 1:
            self.removeFirst()

        # Creamos dos nodos para ir iterando e ir comprobando si son iguales y ver si hay secuencia
        else:
            node1 = self._head
            node2 = node1.next

            # Ahora, se desarrolla el código para el caso general

            start_index = 0
            start = 0
            len_max = 0
            len_seq = 1
            while node2:
                if node1.elem == node2.elem:
                    len_seq += 1
                else:
                    if len_seq >= len_max:
                        len_max = len_seq
                        start = self.index(node2.elem)
                        start_index = start
                    len_seq = 1
                node1 = node2
                node2 = node2.next

            if len_seq > len_max:
                len_max = len_seq
                start_index = start

            for elem in range(len_max):
                self.removeAt(start_index)

        pass

    def fix_loop(self):

        node1 = self._head
        node2 = self._head

        # Intentamos detectar un bucle
        found = False
        while node1 and node1.next and not found:
            node2 = node2.next
            node1 = node1.next.next
            if node1 == node2:
                found = True

        if found:
            # Avanzamos node2 hasta el nodo de inicio del bucle
            node2 = self._head
            while node2 != node1:
                node2 = node2.next
                node1 = node1.next

            # Avanzamos ambos punteros hasta el final del bucle
            last_node = node1
            while last_node.next != node2:
                last_node = last_node.next

            # Eliminamos el bucle
            last_node.next = None
            print("Hay un bucle, que ha sido eliminado")
            return True

        print("No hay un bucle")
        return False

        pass

    def create_loop(self, position):
        # this method is used to force a loop in a singly linked list
        if position < 0 or position > len(self) - 1:
            raise ValueError(f"Position out of range [{0} - {len(self) - 1}]")

        current = self._head
        i = 0

        # We reach position to save the reference
        while current and i < position:
            current = current.next
            i += 1

        # We reach to _tail node and set the loop
        start_node = current
        print(f"Creating a loop starting from {start_node.elem}")
        while current.next:
            current = current.next
        current.next = start_node

    def leftrightShift(self, left, n):

        # Planteamos el caso de que la lista esté vacía

        if self.isEmpty():
            print("Error: la lista está vacía")

        # En el caso de que n sea menor o igual que 0, el programa lanza un error de valor, ya que según
        # el enunciado, la n debe ser un valor mayor que 0

        elif n <= 0:
            raise ValueError("Valor no válido de n")

        # En el caso de que n sea mayor que el tamaño de la lista, devolvemos un mensaje de que la lista
        # no será modificada

        elif n >= self._size:
            print("Error: como n es mayor o igual que el tamaño de la lista, no se modifica")

        # Ahora, planteamos el código para el caso general
        else:

            counter = 0

            if left == True:
                # nodeIt = self._head
                while counter < n:
                    element = self.removeFirst()
                    self.addLast(element)
                    counter += 1
            else:
                while counter < n:
                    element = self.removeLast()
                    self.addFirst(element)
                    counter += 1

        pass


L = SList2()


L.addFirst(2)
L.addFirst(1)


L.delLargestSeq()
print("list:", str(L))