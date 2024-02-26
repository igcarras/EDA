from slist import SList
from slist import SNode
import sys

class SList2(SList):

    def sumLastN(self, n):
        # Método que suma los n últimos elementos de una lista. Complejidad lineal.
        index = 0
        suma = 0
        current = self._head
        if n < 0:
            # En el caso en el que n sea menos que 0, devuelve None.
            return None
        else:
            while current:
                # Con el while se recorre toda la lista hasta llegar al último elemento.
                if index >= len(self)-n:
                    # Si se ha llegado al término len(self)-n, se empiezan a sumar elementos.
                    suma += current.elem
                index += 1
                # Index controla en que posición de la lista se está.
                current = current.next
        return suma
    

    def insertMiddle(self, elem):
        # Método que añade un elemento en la mitad de la lista. Complejidad lineal.
        if self.isEmpty():
            # Si la lista está vacía añade un elemento al principio.
            self.addFirst(elem)
        else:
            newNode = SNode(elem)
            current = self._head
            for i in range(((len(self)+1)//2)-1):
                # Función que calcula la posición del medio para una lista de longitud par o impar.
                current = current.next
            newNode.next = current.next
            current.next = newNode
            # Al llegar al medio se conecta el nuevo nodo con la lista.

    def insertList(self, inputList, start, end):
        # Método que inserta una lista dentro de otra entre dos posiciones dadas eliminando los elementos entremedias.
        # Complejidad lineal
        if start < 0 or end >= len(self) or start > end:
            # Si start o end no están entre los valores válidos, se devuelve None.
            return None
        else:
            principio = self._head
            final = self._head
            new = inputList._head
            for i in range(start - 1):
                # Se coloca el puntero principio en la posición anterior al elemento en la posición start.
                principio = principio.next
            for i in range(end):
                # Se coloca el puntero final en la posición del elemento en la posición end.
                final = final.next
            while new.next:
                # Se recorre la nueva lista hasta el final para poner un puntero en el último elemento.
                new = new.next
            new.next = final.next
            # Se conecta el final de la nueva lista.
            if start == 0:
                # Si start es 0, el _head de la antigua lista se reemplaza por el de la nueva.
                self._head = inputList._head
            else:
                # Si no, se conecta con el elemento principio.
                principio.next = inputList._head

    def reverseK(self, k):
        # Método que invierte los elementos en grupos de k elementos
        if k >= 1 and not self.isEmpty():
            # Solo se ejecuta si k es mayor a 1 y la lista no está vacía
            before = self._head
            # Puntero que apunta al último nodo del grupo anterior
            after = self._head
            # Puntero que apunta al primer nodo del siguiente grupo
            current = self._head
            # Puntero que apunta al nodo en el que se están realizando los cambios
            follow = current.next
            # Puntero que apunta al nodo al que se va a mover current tras haberse realizado los cambios oportunos
            previous = after
            # Puntero que apunta al nodo en el que estaba current previamente ya que va a ser el nuevo current.next
            contador = 0
            i = 0
            termina = False
            while before:
                # Se repetirá hasta que before sea None, indicando que se ha llegado al final de la lista
                if contador < k:
                    # Coloca after en su posición en el  grupo siguiente al actual, moviendolo de k en k posiciones.
                    if after:
                        # Cuando after sea None, se ha llegado al final de la lista y se deja de mover.
                        after = after.next
                    contador += 1
                    previous = after
                    # Previous empieza en after, el primer nodo del grupo a modificar apunta al primer nodo del siguente
                else:
                    if current != after:
                        # Esto se ejecuta hasta que se han recolocado todos los nodos del grupo y current es after
                        current.next = previous
                        # Current.next es el nodo previo a current, cambia el sentido
                        previous = current
                        # Previous pasa a ser current
                        current = follow
                        # Current pasa a ser follow, dejando solo a previous en su lugar
                        if follow:
                            # Follow avanza al siguiente nodo, dejando current en su lugar y solo si no es None
                            follow = follow.next
                    elif self._head.next == after or not termina:
                        # Cuando current es after, si self._head.next es también after, _head está descolocado
                        # Esto solo se cumple una vez, con el primer grupo
                        if i == 0:
                            # Esto solo se ejecuta en la primera pasada por el elif, hasta que el else reinicie i
                            self._head = previous
                            # Previous se ha quedado en el último elemento del primer grupo que se ha modificado
                            # El último miembro del grupo es ahora el primero al cambiar el sentido, previous es _head
                            before = self._head
                            # Colocamos before en el nuevo _head
                        if i < k - 1:
                            # Se va a ejecutar k - 1 veces, hasta que before se encuentra en el final del primer grupo
                            # Es k - 1 porque before está en el primer miembro de ese grupo no en el último del anterior
                            if before:
                                before = before.next
                            i += 1
                        else:
                            # Una vez colocado el before, se reinician las variables,saliendo de el elif
                            contador = 0
                            i = 0
                            termina = True
                            # Termina se aseguraba que aunque _head ya se había colocado, el elif siguera ejecutandose
                    else:
                        if i == 0:
                            # Esto solo se ejecuta en la primera pasada por el else, hasta que se reinicie i
                            before.next = previous
                            # Une el grupo previo con el primer elemento del grupo que se acaba de modificar
                            # Previous se ha quedado en el último elemento del grupo que se ha modificado
                            # El último miembro del grupo es ahora el primero al cambiar el sentido
                        if i < k:
                            # Se ejecuta k veces, moviendo before al último miembre del grupo modificado
                            if before:
                                before = before.next
                            i += 1
                        else:
                            # Reinicia contadores
                            contador = 0
                            i = 0

    def maximumPair(self):
        # Metodo que devuleve la suma máxima entre 2 elemntos equidistantes de la ista. Complejidad lineal
        first = self._head
        last = self._head
        finales = len(self) - 1
        primeros = 0
        maximo = 0
        suma = 0
        i = 0
        j = 0
        if self.isEmpty():
            # Si la lista está vacía, devuelve none.
            return None
        while finales >= primeros:
            # Se repite hasta que los dos indicadores llegan al medio y se intercambian.
            if last.next and i < finales:
                # Coloca el puntero last en la posición de finales. Usa un contadore para controlar la posición.
                last = last.next
                i += 1
            if first and j < primeros:
                # Coloca el puntero first en la posición de primeros. Usa un contadore para controlar la posición.
                first = first.next
                j += 1
            if i == finales and j == primeros:
                # Cuando ambos punteros han llegado a su posición, los contadores(i, j) son iguales a los indicadores.
                if first == last:
                    # Cuando los indicadores son iguales, está en el medio de una lista impar. Se toma el elemento solo.
                    suma = first.elem
                else:
                    suma = first.elem + last.elem
                finales -= 1
                primeros += 1
                i = 0
                j = 0
                last = self._head
                first = self._head
            if suma > maximo:
                # Si el nuevo número es mayor a maximo, se asigna como nuevo valor de max.
                maximo = suma
        return maximo

