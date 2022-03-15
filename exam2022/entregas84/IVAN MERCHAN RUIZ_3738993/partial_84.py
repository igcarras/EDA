# coding=utf-8
import random


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
        "Merge of two ordered lists. No duplicates allowed."
        if self.isSorted() and other.isSorted():
            'Vemos si están ordenadas o no ambas listas'
            aux = MySList()
            node1 = self._head
            node2 = other._head
            'Creamos un bucle que añade a aux los elementos de ambas listas sin repetirlos'
            while node1 and node2:
                if node1.elem < node2.elem:
                    aux.append(node1.elem)
                    node1 = node1.next
                elif node2.elem < node1.elem:
                    aux.append(node2.elem)
                    node2 = node2.next
                elif node1.elem == node2.elem:
                    aux.append(node1.elem)
                    node1 = node1.next
                    node2 = node2.next
            'Añadimos a aux los elementos que queden en una lista si la otra ya está recorrida al completo'
            if node1:
                while node1:
                    aux.append(node1.elem)
                    node1 = node1.next
            if node2:
                while node2:
                    aux.append(node2.elem)
                    node2 = node2.next
            'Devolvemos aux y acaba la función'
            return aux
        else:
            'Si no están ambas ordenadas, devolvemos None y acaba la función'
            return None

'Si sirve de algo, la complejidad es O(n) ya que solo hay bucles sueltos, el mejor caso se dará si hay alguna lista ' \
'desordenada o alguna vacía, y el peor si ambas son largas y con repetición de valores'

'''#Prueba propia
l1 = MySList()
for i in range(10):
    l1.append(i)
print('l1: ',str(l1))
l2 = MySList()
for i in range(8):
    l2.append(2)
print('l2: ',str(l2))
print('list merged: ',str(l1.merge(l2)))
Esta prueba da error si muchos números consecutivos de una lista son iguales, este se situa en la parte del código siguiente:
    elif node1.elem == node2.elem:
        aux.append(node1.elem)
        node1 = node1.next
        node2 = node2.next
He estado mirándolo y probando otro código como:
    elif node1.elem == node2.elem:
        aux.append(node1.elem)
        while node1.elem == node1.next.elem and node1.next == True:
            node1 = node1.next
        while node2.elem == node2.next.elem and node2.next == True:
            node2 = node2.next
pero no da resultados. '''

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
