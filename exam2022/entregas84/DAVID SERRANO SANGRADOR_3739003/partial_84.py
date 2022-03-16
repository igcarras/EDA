# coding=utf-8
# David Serrano Sangrador
class SNode:
  def __init__(self, e, next=None):
    self.elem = e
    self.next = next
    
    
class MySList():
    
    def __init__(self):
        self._head=None
        self._tail=None
        
    def __str__(self):
        """Returns a string with the elements of the list"""
        ###This functions returns the same format used 
        ###by the Python lists, i.e, [], ['i'], ['a', 'b', 'c', 'd']
        ###[1], [3, 4, 5]
        nodeIt=self._head
        result='['
        while nodeIt:
            result+= str(nodeIt.elem)+ ", "
            nodeIt=nodeIt.next

        if len(result)>1:
            result=result[:-2]

        result+=']'
        return result
    
    def append(self,e):
        """Adds a new element, e, at the end of the list"""
        #create the new node
        newNode=SNode(e)
        #the last node must point to the new node
        #now, we must update the tail reference
        if self._head==None:
            self._head=newNode
        else:
            self._tail.next= newNode
        
        self._tail=newNode

    def isSorted(self):
        "returns True if self is sorted"
        if self._head==None:
            return True
        else:
            node1=self._head
            node2=node1.next
            while node2:
                if node1.elem>node2.elem:
                    return False
                node1=node2
                node2=node2.next
                
        return True

    def merge(self, other):
        laux = MySList()
        "Merge of two ordered lists. No duplicates allowed."
    # primero comprobamos si la lista está ordenada
        if self._head == None and other._head == None:
            return laux
        elif self.isSorted() == False or other.isSorted() == False:
            return None
        elif self._head == None and other.isSorted() == True:
            laux = other
            return laux

        elif self.isSorted() == True and other._head != None:
            puntero1 = self._head
            while puntero1.next != None:
                a = puntero1.elem
                laux.append(a)
                puntero1 = puntero1.next
            return laux
        else:
            # Caso más sencillo
            puntero1 = self._head
            punteroother = other._head
            while puntero1.next != None:
                a = puntero1.elem
                laux.append(a)
                puntero1 = puntero1.next
            while punteroother.next != None:
                a = punteroother.elem
                laux.append(a)
                punteroother = punteroother.next
        #Acabamos de juntar las 2 listas, ahora toca eliminar duplicados
            # faltaría ordenarlos de mayor a menos
            current = laux._head
            previous = laux._head
            while current.elem != current.next.elem:
                while previous.next != current:
                    previous = previous.next
                while current.elem == current.next.elem:
                    current = current.next
                previous.next = current
                current = current.next
        # hemos estado moviendo los puntero para que eliminen los elementos duplicados juntos y solo se quede 1 de los duplicados
            return laux


other = MySList()


import random
if __name__=='__main__':
       #Please, uncomment the code for test each function
        l2=MySList()

        for i in range(10):
            l2.append(random.randint(0,20))
        print(l2)

        l3 = MySList()
        for i in range(10):
            l3.append(i)

        print('l2:', str(l2))
        print('l3:', str(l3))

        print("List merged:", str(l2.merge(l3)))
        print("List merged:", str(l3.merge(l2)))
        
        data=[]
        for i in range(5):
            x=random.randint(0,10)
            if x not in data:
                data.append(x)

        data.sort()
        l2=MySList()
        for x in data:
            l2.append(x)
            
        data=[]
        for i in range(7):
            x=random.randint(0,10)
            if x not in data:
                data.append(x)
            
        data.sort()
        l3=MySList()
        for x in data:
            l3.append(x)

        print('l2:', str(l2))
        print('l3:', str(l3))
        print("List merged:" , str(l2.merge(l3)))
        print("List merged:" , str(l3.merge(l2)))

"""
# si una lista esta vacia y la otra esta ordenada, da igual si se repiten elementos o no copiamos la lista
            # que esta ordenada,
            punteroother = other._head
            while punteroother.next != None:
                a = punteroother.elem
                laux.append(a)
                punteroother = punteroother.next
            current = laux._head
            previous = laux._head
            while current != current.next:
                while previous.next != current:
                    previous = previous.next
                while current.elem == current.next.elem:
                    current = current.next
                previous.next = current
                current = current.next
            return laux
"""
