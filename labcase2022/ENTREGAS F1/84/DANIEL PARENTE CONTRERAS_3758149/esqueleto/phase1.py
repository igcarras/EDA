# coding=utf-8
from slist import SList
from slist import SNode

class SList2(SList):

    def sumLastN(self, n): # Primer método, que suma los últimos n elementos
        if n > self._size: # Aseguramos que n no es mayor que el tamaño de la lista
            n = self._size
        
        if n < 0: # Si n es negativo devolvemos un None
            return None
        
        else:
            current = self._head # Creamos un puntero auxiliar y lo situamos en _head
            for i in range(self._size - n): # Colocamos el puntero en la posición anterior a los n elementos que queremos sumar
                current = current.next
            suma = 0 # Creamos una variable auxiliar para ir acumulando el valor de los elementos
            for i in range(n): # Con un bucle for recorremos los n términos y los sumamos
                suma += current.elem
                current = current.next
            return suma # Devolvemos la suma correspondiente

    def insertMiddle(self, e): # Método que inserta un nodo con un elemento e en medio de la lista
        if self._size == 0: # Si la lista está vacía se inserta con un addFirst sin hacer más operaciones
            self.addFirst(e)
        else: # Si no, se crea un nuevo nodo
            nuevo_nodo = SNode(e)
            current = self._head # Se crea un puntero que recorrerá la lista

            # Se recorre la lista hasta el elemento anterior al lugar donde va a ser insertado el nuevo nodo
            for i in range((self._size // 2) + (self._size % 2) - 1): # El módulo se añade para avanzar un
                current = current.next # lugar más en caso de que la lista tenga un tamaño impar
            nuevo_nodo.next = current.next # Después de mover el puntero se conecta con el nuevo nodo
            current.next = nuevo_nodo 
        

    def insertList(self, other : SList, start : int, end : int):
        if start < 0 or start > end or end >= self._size:
            print("Los parámetros introducidos son incorrectos")
        
        elif start == 0:
            current_other = other._head # Puntero que recorre la lista que se introduce por parámetro

            while current_other.next != None: # Movemos el puntero por la lista ajena hasta llegar al final
                current_other = current_other.next

            current_self = self._head # Puntero que recorre la lista original

            for i in range(end + 1):
                current_self = current_self.next # Movemos el puntero hasta el nodo siguiente al último que ha de ser eliminado
            
            current_other.next = current_self # Enganchamos la parte final de la lista introducida con la lista original
            
            self._head = other._head # Como debemos introducir en el 0, cambiamos la cabeza de la lista original por la nueva

        else:
            current_other = other._head # Puntero que recorre la lista introducida
            while current_other.next != None:
                current_other = current_other.next # Movemos el puntero al final de la lista que será introducida
            
            current_self_end = self._head # Puntero que irá al nodo siguiente al último que ha de ser eliminado
            
            for i in range(end + 1):
                current_self_end = current_self_end.next
            
            current_other.next = current_self_end # Enganchamos la parte final de la lista introducida con la lista original

            current_self_start = self._head # Puntero que irá al nodo anterior al primero que tiene que ser eliminado
            
            for i in range(start - 1):
                current_self_start = current_self_start.next # Movemos al puntero a su posición

            current_self_start.next = other._head # Enganchamos la lista original con el "_head" de la lista introducida


        """    def reverseK(self, k : int):
        if k <= 1: # Si k es 1 o 0 no se hace nada con la lista
            print("No se realiza ningún cambio")
        
        elif k >=  self._size:
            lista_auxiliar = SList() # Se crea la lista auxiliar
            current = self._head # Puntero que recorre la lista
            for i in range(self._size): # Recorre la lista y introduce los elementos en la lista auxiliar, cambiando el orden
                lista_auxiliar.addFirst(current.elem)
                current = current.next
            self._head = lista_auxiliar._head # La lista invertida pasa a ser la lista normal
        
        else:
            lista_auxiliar = SList() # Se crea una lista auxiliar donde se irán colocando los valores que serán invertidos
            for i in range(self._size // k): # Se divide la lista en subsecciones del tamaño de k, y se recorren con un bucle
                for n in range((k*i + k) - 1, k*i -1, -1): # Se recorren los indices de cada subsección y se añaden a la lista, empezando por el último para que queden revertidos
                    lista_auxiliar.addLast(self.getAt(n))
            for i in range(self._size - 1, self._size - (self._size % k) - 1, -1): # Se ajusta el último bucle por si quedara algún grupo de nodos sin revertir
                lista_auxiliar.addLast(self.getAt(i))

            self._head = lista_auxiliar._head  # Una vez la lista auxiliar tiene todos los valores de la original revertidos se cambia la original por la auxiliar
        """
    def reverseK(self, k):
        if k <= 1: # Si k es 0 o 1 no es necesario hacer ningun cambio
            return self
        else:
            self._head = self._reverseK(k, self._head) # Se llama a una función auxiliar dando como parametros k y donde empieza la lista
                # la función recursiva colocará los nodos a partir de la cabeza de forma correcta
    def _reverseK(self, k : int, cabeza):
        
        current = cabeza # Se inicializan tres punteros, que servirán para dar la vuelta a la lista
        ant = None
        next = None

        index = 0 # Y un contador para asegurar que se invierten solo en grupos de k elementos

        while index < k and current is not None: # Bucle que se ejecuta k veces o hasta que llegas al final de la lista
            next = current.next
            current.next = ant
            ant = current
            current = next # Este bucle invierte tantos elementos como iteraciones tenga
            
            index += 1
        
        if next is not None: # Si después de terminar el bucle la lista todavía tiene elementos se vuelve a llamar a la función
            cabeza.next = self._reverseK(k, next)

        return ant # Por último se devuleve el nodo ant, que será el de indice k-1, que será la cabeza de la lista

    
    def maximumPair(self):
        if self._size == 0: # Comprabaciones previas para saber si la lista está vacía o tiene un solo elemento
            return None     # Entonces solo haríamos una operación
        elif self._size == 1:
            return self._head.elem
       
        # Para poder sumar los elementos de la lista con los del lado contrario usando un solo bucle primero es necesario
        # darle la vuelta a una mitad de la lista
        else:
            current = self._head
            ant = None
            next = None

            for i in range(self._size // 2 + self._size % 2 - 1):
                current = current.next # Movemos un cursor hasta la mitad de la lista

            marca_division = current # guardamos el elemento anterior al primero que va a ser dado la vueltas
            current = marca_division.next

            while current is not None: # Enlazamos  cada cursor con el anterior para asi girarlos todos
                next = current.next
                current.next = ant
                ant = current
                current = next
            marca_division.next = ant # Enlazamos el elementos de la otra mitad con el primero de la segunda


            puntero1 = self._head # recorreremos cada mitad con un puntero
            puntero2 = marca_division.next
            suma_maxima = puntero1.elem + puntero2.elem
           
            while puntero1 != marca_division.next: # La marca_division indica la mitad de la lista, ya que no hay que recorrerla entera
                
                if puntero2 == None: # Tal y como está hecho el método, si hay un elemento impar siempre queda en la primera mitad
                    if puntero1.elem > suma_maxima: # por lo que si el puntero2 es None, sabes que el puntero1 apunta al elemento impar
                        suma_maxima = puntero1.elem
                    puntero1 = puntero1.next
                
                else: # Se comprueba si la suma de ambos elementos es mayor que la suma máxima
                    if puntero1.elem + puntero2.elem > suma_maxima:
                        suma_maxima = puntero1.elem + puntero2.elem

                    puntero1 = puntero1.next
                    puntero2 = puntero2.next

            return suma_maxima
