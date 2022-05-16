from slist import SList
import sys
from slist import SNode

class SList2(SList):

    def sumLastN(self, n):
        sumador = 0
        if self.isEmpty():  #comprobamos si la lista está vacía
            print("ERROR, debe contener al menos un elemento la lista")
            return 0
        else:
            if n < 0:    #si el número es negativo, no habrá suma
                return None
            elif n > self._size:   #cuando el numero pedidio es mayor que la lista se sumarán todos sus elementos
                for i in range (self._size):
                    ultimo_elemento = self.removeFirst()
                    sumador += ultimo_elemento
                return sumador

            elif n <= self._size: #cuando el numero pedido es menor que la lista se cogerán solo los n últimos
                for i in range (n):  #bucle para saber a partir de donde sumar
                    ultimo_elemento = self.removeLast()
                    sumador += ultimo_elemento
                return  sumador


    def insertMiddle(self, elem):
        posicion = int      #decimos que posicion  tiene que tener un valor entero
        nodeIt = self._head   #creamos un auxiliar para ir pasando de nodo

        if self.isEmpty():     #comprobamos si la lista está vacía
            self.addFirst(elem)
        else:   #dependiendo si es par o impar utilizaremos un metodo u otro
            if self._size % 2 == 0:   #miramos si la lista es par
                posicion = len(self) // 2
            elif self._size % 2 != 0:  #miramos si la lista es impar
                posicion = (len(self) + 1) // 2
            for i in range(1, posicion):    #hacemos un bucle hasta que el nodo auxiliar llegue a la posicion deseada
                nodeIt = nodeIt.next
            newNode = SNode(elem)    #pasos basicos para crear y avanzar el nodo
            newNode.next = nodeIt.next
            nodeIt.next = newNode
        self._size += 1


    def insertList(self,inputList,start,end):
        index = 1
        nodeIt = self._head   #creamos un auxiliar para ir pasando de nodo

        if start > end :    #primero realizamos todas las pruebas que dan error
            return None
        elif end >= self._size:
            return None
        elif start < 0:
            return None
        else:    #ahora realizamos las pruebas que nos dan un return correcto
            if start == 0:    #si la lista está vacia simplemente añadimos la lista input mediante un head
                self._head = inputList._head
            else:
                while index != start:      #avanzamos el nodo auxiliar hasta que coincida con el start que tenemos
                    nodeIt = nodeIt.next
                    index += 1
                first = nodeIt
                first.next = inputList._head

            while index <= end:     #avanzamos el nodo auxiliar hasta que coincida con el end
                nodeIt = nodeIt.next
                index += 1
            last = nodeIt.next

            nodeIt2 = inputList._head   #añadimos los elementos de la lista mediante un head
            while nodeIt2.next != None:
                nodeIt2 = nodeIt2.next
            nodeIt2.next = last


    def reverseK(self,k):
        nodeIt = self._head   #creamos un auxiliar para ir pasando de nodo
        posicion = 0    #establecemos una posicion incial
        i = 0
        ind = 0
        nueva_lista = SList2()   #creamos nueva lista para añadir el nuevo orden
        while nodeIt:    #mientras que existan nodos
            nueva_lista.insertAt(ind, nodeIt.elem)   #insertamos el valor del elemento el nueva lista invertido
            i += 1     #vamos sumando de 1 en 1 hasta llegar a la cifra de k
            posicion += 1

            if i == k:    #cuando i es igual k se ha acabado el bucle de k elementos
                i = 0  #reinciamos los valores para vovler a realizar el bucle hasta que nos quedemos sin elementos
                ind = posicion
            nodeIt = nodeIt.next
        self._head = nueva_lista._head  #hacemos que la nueva lista hedere el head inicial


    def maximumPair(self):
        nodeIt = self._head   # creamos un auxiliar para ir pasando de nodo
        posicion = 0   # #establecemos una posicion incial
        max_cifra = 0  #damos un valor inicial a la suma maxima

        if self.isEmpty():
            return None  #comprobamos si la lista está vacía
        else:
            while posicion < self._size//2:   #solo recorremos la mitad de la lista ya que es suficiente  mas eficaz
                valor_conjunto = self.getAt(self._size - posicion - 1)   #buscamos su valor inverso (el menos 1 es para contrarestar empezar en 0)
                adicion = nodeIt.elem + valor_conjunto   #hacemos la suma de ambas sumas
                if adicion > max_cifra:   #nos quedamos con el mayor valor de todas las sumas
                    max_cifra = adicion
                posicion+= 1
                nodeIt = nodeIt.next

        if len(self) % 2 != 0:     #si la lista es impar queda la cifra del medio, por lo que tenemos que comprobar su valor con la el resutlado obtenido anteriormente para determinar cual es el valor final
            if nodeIt.elem > max_cifra:
                max_cifra = nodeIt.elem
        return max_cifra


