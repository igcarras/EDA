# -*- coding: utf-8 -*-

class SNode:
  # Creamos la clase "SNode", que nos va a servir de apoyo a la hora de crear nuevos nodos/elementos anidados a una
  # lista en cuestión.
  def __init__(self, e, next=None):
    # "next" tiene un valor predeterminado, y es "None". A menos que digamos lo contrario, el nodo en cuestión apuntará
    # a la nada siempre.
    self.elem = e
    self.next = next

class SList:
    # Esta es la implementación de una lista simplemente enlazada, que se va a apoyar en la clase SNode anteriormente
    # mencionada.
    def __init__(self):
        # Creamos una "lista vacía". La cabeza de la misma, por defecto, apunta a la nada. El tamaño, por su parte,
        # va a tener por defecto el valor "0".
        self._head = None
        self._size = 0
    
    def __len__(self):
        # Devuelve el tamaño de la lista (simplemente decimos el valor del atributo privado "size".
        return self._size

    def isEmpty(self):
        # Si la lista está vacía devuelve "True". Básicamente, si la cabeza de la lista apunta a la nada quiere decir
        # que no hay ningún elemento en la misma.
        return self._head == None

    def __str__(self):
        # Devuelve una cadena con los elementos de la lista.
        result = ''
        nodeIt = self._head

        # Mientras que el nodo "nodeIt", que parte de la cabeza, no apunte a la nada, se va a añadir a "result".
        while nodeIt != None:
            result += ',' + str(nodeIt.elem)
            nodeIt = nodeIt.next

        # Si la cadena de texto "result" tiene un tamaño mayor que 0, se elimina la "," que se ha generado al principio.
        if len(result) > 0:
            result = result[1:] # Hipótesis: es [1:] y no [0:] para evitar la "," que se ha generado al principio.
        
        return result
  
    def addFirst(self, e):
        # Se añade un nodo al principio de la lista, pasando a ser apuntado por la cabeza/head.
        # Creamos un nuevo nodo.
        newNode = SNode(e)

        # El nuevo nodo debe apuntar a la cabeza de la lista, es decir, que el siguiente elemento es dicha cabeza (o lo
        # que es lo mismo, este nuevo nodo es el primero de todos los que hay, lo único es que todavía no pertenece a
        # la lista en sí porque, para ello, debe ser apuntada por la cabeza al ser el primer elemento.
        newNode.next = self._head

        # La cabeza/head apunta al nuevo nodo.
        self._head = newNode

        # Incrementamos en "1" el tamaño de la lista.
        self._size += 1
    
    def addLast(self, e):
        # Se añade un nodo al final de la lista.
        # Creamos un nuevo nodo.
        newNode = SNode(e)

        # Si la lista está vacía, simplemente apuntamos con el head al nuevo nodo.
        if self.isEmpty():
            self._head = newNode
        else:
            # Recorremos la lista desde la cabeza hasta llegar al final de la misma.
            current = self._head
            while current.next:
                current = current.next
            # Lo que hemos hecho es decir: "hasta que el "next" de "current" sea la nada, vamos a ir uno por uno
            # recorriendo los nodos que la componen.

            # Ahora, current debe apuntar a newNode, que va a pasar a ser el último nodo de la lista y, como
            # consecuencia, este será cuyo next apunte a "None".
            current.next = newNode
        # De nuevo, incrementamos en "1" el tamaño de la lista.
        self._size += 1

    def removeFirst(self):
        # Se elimina y devuelve el primer elemento de la lista.
        result = None
        # Si la lista está vacía, no hay ningún elemento que eliminar. Por ende, decimos que hay un error y devolvemos
        # que result = None.
        if self.isEmpty():
            print('Error removeFirst: ¡La lista está vacía!')
        else:  
            # Result toma el valor del elemento alojado en el nodo que es apuntado por la cabeza/head.
            result = self._head.elem
            # Head pasa a apuntar al siguiete nodo. Si solo había un nodo en la lista, pasará a apuntar a "None".
            self._head = self._head.next

            # Decrementamos en "1" el tamaño de la lista.
            self._size-=1
        
        return result

    def removeLast(self):
        # Se elimina y devuelve el último elemento de la lista.
        result = None
        # Si la lista está vacía, no hay ningún elemento que eliminar. Por ende, decimos que hay un error y devolvemos
        # que result = None.
        if self.isEmpty():
            print('Error removeLast: ¡La lista está vacía!')
        # Si la lista únicamente tiene un nodo, podemos aplicar un método ya implementado: removeFirst (ya que el
        # principio y el final de la lista es el mismo).
        elif len(self) == 1:
            result = self.removeFirst()
        else:
            # Lo que hacemos es lo siguinente: tenemos dos atributos auxiliares: "current" y "lastNode". Ambos
            # atributos van a recorrer la lista de forma paralela, yendo lastNode "1" por delante. Cuando "lastNode"
            # esté apuntando a None querrá decir que hemos llegado al final de la lista, quedando la siguiente
            # disposición: current = penúltimoNodo; lastNode = últimoNodo. Para eliminar el último nodo (lastNode)
            # haremos que current apunte a None en vez de a lastNode, por ende, lastNode queda fuera de la lista.
            current = None
            lastNode = self._head
            while lastNode.next:
                current = lastNode
                lastNode = lastNode.next

            # Result -lo que devuelve el método- es el elemento que había en el último nodo de la lista (lastNode).
            result = lastNode.elem
            current.next = None

            # De nuevo, decrementamos en "1" el tamaño de la lista.
            self._size -= 1
        
        return result

    def index(self, e):
        # Se nos devuelve la posición en la que aparece por primera vez en la lista el elemento "e".
        # Recorremos la lista desde la cabeza de la misma.
        nodeIt = self._head
        index = 0
        while nodeIt != None:
            if nodeIt.elem == e:
                return index
            nodeIt = nodeIt.next
            index += 1

        # Si al terminar el bucle no hemos podido hacer el "return" correspondiente, devolveremos el valor mencionado
        # anteriormente: "-1".
        return -1

    def getAt(self, index):
        # Se devuelve el elemento que hay en el índice indicado. Si el índice está fuera de rango o, de plano, no es
        # un atributo válido, el método devolverá "-1".
        result = None
        if index not in range(0, len(self)):
            print(index, 'Error getAt: El índice está fuera de rango.')
        else:
            # Como en otras ocasiones, recorremos la lista nodo por nodo desde el head.
            nodeIt = self._head
            i = 0
            # Mientras que el nodo "nodeIt", que parte de la cabeza, no apunte a la nada y el índice por el cual
            # vayamos sea menor que el que nos han adjuntado por parámetro, recorremos la lista.
            while (nodeIt != 0) and i < index:
                nodeIt = nodeIt.next
                i += 1

            # Devolvemos el elemento que se encuentra en el nodo de dicho índice.
            result = nodeIt.elem

        return result

    def insertAt(self, index, e):
        # Este método "crea" un nuevo nodo cuyo elemento que contiene sea "e" y en el índice "index" aportado por
        # parámetro.
        
        # Primero, comprobamos que "index" sea un parámetro válido.
        # Nótese que comprendemos en el bucle también el índice del último elemento, ya que -aunque no tenga mucho
        # sentido- este método debe de poder hacer las veces del "addLast".
        if index not in range(0, len(self) + 1):
            print(index, 'Error insertAt: El índice está fuera de rango.')
        # Si el índice es "0", recurrimos al método "addFirst".
        elif index == 0:
            self.addFirst(e)
        # Si el índice es uno más que el último nodo existente, recurrimos al método "addLast".
        elif index == len(self):
            self.addLast(e)
        # Si es un índice ya existente...
        else:
            # En primer lugar, debemos llegar al nodo PREVIO al que tiene el índice "index".
            current = self._head
            for i in range(index - 1):
                current = current.next
                    
            # Ahora, current es el nodo previo al nodo con el índice "index".
            # Creamos un nuevo nodo que contiene el elemento "e" pasado por parámetro.
            newNode=SNode(e)
            # "newNode" debe apuntar al nodo que hay posterior a current.
            newNode.next = current.next
            # Ahora, current va a apuntar a newNode en vez de a current.next, que es el nodo al cual está apuntando
            # newNode. De esta manera, hemos logrado incluir en medio de ambos nodos "newNode".
            current.next = newNode

            # Incrementamos en "1" el tamaño de la lista.
            self._size += 1

    def removeAt(self, index):
        # Este método elimina de la lista el nodo cuyo índice en la misma es "index".
        result = None
        # En primer lugar, comprobamos que el índice aportado es correcto. En este caso no abarcamos el índice posterior
        # al último que hay en la lista porque no queremos añadir ningún nodo más, sino eliminarlo.
        if index not in range(len(self)): 
            print(index, 'Error removeAt: El índice está fuera de rango.')
        # Si el índice es "0", recurrimos al método "removeFirst".
        elif index == 0:
            result = self.removeFirst()
        # Si el índice es el último de la lista, recurrimos al método "removeLast".
        elif index == len(self) - 1:
            result = self.removeLast()
        # Si es un índice "interno"...
        else:
            # En primer lugar, debemos llegar al nodo PREVIO al que tiene el índice "index".
            current = self._head
            for i in range(index - 1):
                current = current.next

            # Ahora bien, current.next es el nodo cuyo índice es "index".
            result = current.next.elem
            # Ahora, el .next de current no es el nodo cuyo índice es "index", sino el siguiente de este. Por tanto,
            # el nodo de dicho índice queda sin ser apuntado por ningún nodo previo y, finalmente, queda fuera de la
            # lista.
            current.next = current.next.next

            # Decrementamos en "1" el tamaño de la lista.
            self._size -= 1
        
        return result
