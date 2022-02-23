# -*- coding: utf-8 -*-

class SNode:
  def __init__(self, e, next=None):
    self.element = e
    self.next = next


class SList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def isEmpty(self):
    return self.head == None

  def __len__(self):
    return self.size

  def addFirst(self, e):
    newNode = SNode(e)
    newNode.next = self.head
    if self.isEmpty():
      self.tail = newNode
    self.head = newNode
    self.size += 1


  def addLast(self, e):
    newNode = SNode(e)
    if self.isEmpty():
      self.head = newNode
    else:
      self.tail.next = newNode
    self.tail = newNode
    self.size += 1

  def __str__(self):
    result = ""
    current = self.head

    while current != None:
      result += "," + str(current.element)
      current = current.next

    if len(result) > 0:
      result = result[1:]

    return result

  def removeFirst(self):
    if self.isEmpty():
      print("Error: ¡La lista está vacía!")
      return None
    first = self.head.element
    self.head = self.head.next
    if self.isEmpty():
      self.tail = None
    self.size -= 1

    return first

  def removeLast(self):
    if self.isEmpty():
      print("Error: ¡La lista está vacía!")
      return None
    last = self.tail.element
    previous = None
    current = self.head
    while current.next != None:
        previous = current
        current = current.next
    # El siguiente if lo que hace es comprobar que si previous es igual a vacío entonces es porque no se ha movido el
    # puntero previous (no ha entrado en el while). Por tanto, si no ha entrado en el while y la lista sabemos que tiene
    # elementos (porque antes comprobamos si es empty) entonces solo puede tener un elemento.
    if previous == None:
      self.head = None
    else:
      previous.next = None

    self.tail = previous
    self.size -= 1

    return last

  def getAt(self, index):
    # Se devuelve el elemento que hay en el índice indicado. Si el índice está fuera de rango o, de plano, no es
    # un atributo válido, el método devolverá "-1".
    result = None
    if index not in range(0, len(self)):
      print(index, "Error getAt: El índice está fuera de rango.")
    else:
      # Como en otras ocasiones, recorremos la lista nodo por nodo desde el head.
      current = self.head
      i = 0
      # Mientras que el nodo "current", que parte de la cabeza, no apunte a la nada y el índice por el cual
      # vayamos sea menor que el que nos han adjuntado por parámetro, recorremos la lista.
      while (current != None) and i < index:
        current = current.next
        i += 1

      # Devolvemos el elemento que se encuentra en el nodo de dicho índice.
      result = current.element

    return result

  def index(self, e):
    # Se nos devuelve la posición en la que aparece por primera vez en la lista el elemento "e".
    # Recorremos la lista desde la cabeza de la misma.
    current = self.head
    index = 0
    while current != None:
      if current.element == e:
        return index
      current = current.next
      index += 1

    # Si al terminar el bucle no hemos podido hacer el "return" correspondiente, devolveremos el valor mencionado
    # anteriormente: "-1".
    return -1

  def insertAt(self, index, e):
    # Este método "crea" un nuevo nodo cuyo elemento que contiene sea "e" y en el índice "index" aportado por
    # parámetro.

    # Primero, comprobamos que "index" sea un parámetro válido.
    # Nótese que comprendemos en el bucle también el índice del último elemento, ya que -aunque no tenga mucho
    # sentido- este método debe de poder hacer las veces del "addLast".
    if index not in range(0, len(self) + 1):
      print(index, "Error insertAt: El índice está fuera de rango.")
    # Si el índice es "0", recurrimos al método "addFirst".
    elif index == 0:
      self.addFirst(e)
    # Si el índice es uno más que el último nodo existente, recurrimos al método "addLast".
    elif index == len(self):
      self.addLast(e)
    # Si es un índice ya existente...
    else:
      # En primer lugar, debemos llegar al nodo PREVIO al que tiene el índice "index".
      current = self.head
      for i in range(index - 1):
        current = current.next

      # Ahora, current es el nodo previo al nodo con el índice "index".
      # Creamos un nuevo nodo que contiene el elemento "e" pasado por parámetro.
      newNode = SNode(e)
      # "newNode" debe apuntar al nodo que hay posterior a current.
      newNode.next = current.next
      # Ahora, current va a apuntar a newNode en vez de a current.next, que es el nodo al cual está apuntando
      # newNode. De esta manera, hemos logrado incluir en medio de ambos nodos "newNode".
      current.next = newNode

      # Incrementamos en "1" el tamaño de la lista.
      self.size += 1

  def removeAt(self, index):
    # Este método elimina de la lista el nodo cuyo índice en la misma es "index".
    result = None
    # En primer lugar, comprobamos que el índice aportado es correcto. En este caso no abarcamos el índice posterior
    # al último que hay en la lista porque no queremos añadir ningún nodo más, sino eliminarlo.
    if index not in range(len(self)):
      print(index, "Error removeAt: El índice está fuera de rango.")
    # Si el índice es "0", recurrimos al método "removeFirst".
    elif index == 0:
      result = self.removeFirst()
    # Si el índice es el último de la lista, recurrimos al método "removeLast".
    elif index == len(self) - 1:
      result = self.removeLast()
    # Si es un índice "interno"...
    else:
      # En primer lugar, debemos llegar al nodo PREVIO al que tiene el índice "index".
      current = self.head
      for i in range(index - 1):
        current = current.next

      # Ahora bien, current.next es el nodo cuyo índice es "index".
      result = current.next.element
      # Ahora, el .next de current no es el nodo cuyo índice es "index", sino el siguiente de este. Por tanto,
      # el nodo de dicho índice queda sin ser apuntado por ningún nodo previo y, finalmente, queda fuera de la
      # lista.
      current.next = current.next.next

      # Decrementamos en "1" el tamaño de la lista.
      self.size -= 1

    return result

  def remove(self, e):
    # Eliminamos de la lista la primera aparición de "e".
    # Recorremos la lista desde la cabeza de la misma.
    current = self.head
    index = 0
    while current != None:
      if current.element == e:
        self.removeAt(index)
        return None
      current = current.next
      index += 1

    # Si al terminar el bucle no hemos podido hacer el "return" correspondiente, devolveremos que el elemento pedido
    # no está en la lista.
    return "Error remove: El elemento no existe en la lista."

  def removeAll(self, e):
    current = self.head
    number = self.count(e)
    apariciones = 0
    while current.next != None:
      if current.next.element == e:
        current.next = current.next.next
        apariciones += 1
      else:
        current = current.next
    if apariciones == number:
      return None
    else:
      return "Error remove: El elemento no existe en la lista."

  def getAtRev(self, index):
    result = None
    if index not in range(0, len(self)):
      print(index, "Error getAt: El índice está fuera de rango.")
    else:
      current = self.head
      i = 0
      while (current != 0) and i < ((self.size - 1) - index):
        current = current.next
        i += 1
      result = current.element

    return result

  def getMiddle(self):
    if self.__len__() % 2 == 0:
      return self.getAt((self.__len__() // 2) + 1)
    else:
      return self.getAt(self.__len__() // 2)

  def count(self, e):
    current = self.head
    number = 0
    while current.next != None:
      if current.element == e:
        number += 1
      current = current.next
    if number == 0:
      return "El elemento no existe en la lista."
    else:
      return number

  def isPalindrome(self):
    i = self.__len__() - 1
    notpalindrome = False
    if i <= 1:
      print("Los elementos contenidos en la lista no pueden formar una palabra palíndroma debido a su escasa longitud.")
      return False
    else:
      while i != 0 and not notpalindrome:
        if self.getAt(i) != self.getAt((self.__len__() - 1) - i):
          notpalindrome = True
        else:
          if i == 1:
            i -= 1
          else:
            i -= 2
    if i == 0:
      return True
    else:
      return False

  def isSorted(self):
    # Vamos a considerar el caso en el que los elementos de la lista son números.
    current = self.head
    orden = True
    end = False
    while current != None and orden and not end:
      if current.next != None:
        if current.element > current.next.element:
          orden = False
        else:
          current = current.next
      else:
        end = True
    return orden

  def removeDuplicatesSorted(self):
    # Vamos a considerar el caso en el que los elementos de la lista son números.
    current = self.head
    end = False
    if not self.isSorted():
      return None
    else:
      while current != None and not end:
        if current.next != None:
          if current.element == current.next.element:
            current.next = current.next.next
          else:
            current = current.next
        else:
          end = True

  def removeDuplicates(self):
    current = self.head
    previous = self.head
    next = self.head.next
    while current:
      e = current.element
      while next:
        if e == next.element:
          previous = next
          next = next.next
        else:
          previous.next = next.next
          next = next.next
      current = current.next

  def removeDuplicates2(self):
    nodeIt = self._head
    while nodeIt:
      e = nodeIt.elem
      prev = nodeIt
      nodeIt2 = nodeIt.next
      while nodeIt2:
        if e == nodeIt2.elem:
          prev.next = nodeIt2.next
          if nodeIt2.next == None:
            self._tail = prev
          self._size -= 1

        prev = nodeIt2
        nodeIt2 = nodeIt2.next

      nodeIt = nodeIt.next

  def swapPairwise(self):
    current = self.head
    end = False
    while current != None and not end:
      if current.next != None:
        result1 = current.element
        result2 = current.next.element
        current.element = result2
        current.next.element = result1
        current = current.next.next
      else:
        end = True

  def moveLast(self):
    if self.head == None or self.__len__() == 1:
      print("Error moveLast: La lista no tiene los elementos suficientes para aplicar el método correctamente.")
    else:
      element = self.tail.element
      current = self.head
      while current.next != self.tail:
        current = current.next
      current.next = None
      self.tail = current
      newNode = SNode(element)
      newNode.next = self.head
      self.head = newNode

  def intersection(self, l2):
    if not self.isSorted() or not l2.isSorted():
      print("Error intersection: Ambas listas han de estar ordenadas.")
    else:
      result = ""
      for element in self.__str__():
        if element != ",":
          if element in l2.__str__():
            result += "," + element
      if len(result) > 0:
        # Le quitamos la coma "extra" que hay al principio.
        result = result[1:]
      return result

  def segregateOddEven(self):
    Lista_Par = SList()
    Lista_Impar = SList()
    for i in range(self.__len__()):
      if self.getAt(i) % 2 == 0:
        Lista_Par.addLast(self.getAt(i))
      else:
        Lista_Impar.addLast(self.getAt(i))
    Lista_Par.tail.next = Lista_Impar.head
    self.head = Lista_Par.head
    self.tail = Lista_Impar.tail

L = SList()

L.addLast(1)
L.addLast(2)
L.addLast(4)
L.addLast(1)
L.addLast(1)
L.addLast(3)
L.addLast(7)
L.addLast(3)

print(L.__str__())

L.removeDuplicates()

print(L.__str__())

'''
  def removeDuplicates(self):
    current = self.head
    previous = None
    while current:
      if current == self.head:
        current = self.head.next
        previous = self.head
      else:
        previous = previous.next
        current = current.next
      e = previous.element
      while current:
        if current.element != e:
          current = current.next
        else:
          i = self.index(current.element)
          current = current.next
          self.removeAt(i)
      current = previous.next
'''






