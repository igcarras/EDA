# coding=utf-8
#Nora Tajuelo del Pozo 
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
        #now, we must update the _tail reference
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
        #comprobamos que las listas no estén vacías 
        prev = None 
        node = self._head
        #comprobamos que las listas no estén vacías
        if self._head == None :
            print("la lista está vacía")
            return None 
        elif other._head ==None: 
            print("la lista está vacía")
            return None 
            
        else: 
            #creamos una lista para ir añadiendo los elementos 
            resultado = MySList()
            #colocamos el nodo en la cabecera para ir recorriendo la lista
            while node!=None:
                #primero añadimos los elementos de la lista invocante
                resultado.append(node.elem)
                node = node.next 
            #Ahora colocamos el nodo en la cabecera de la lista other
            node = other._head 
            while node!=None:
                resultado.append(node.elem)
                node = node.next
            #cuando hayamos añadido todos, los ordenamos 
            resultado.isSorted()
            #ahora debemos recorrer la lista para eliminar aquellos elementos 
            #que estén repetidos y eliminar uno de ellos 
            node = resultado._head
            while node!=None: 
                if node.elem == node.next.elem:
                    if node == self._head: 
                        self._head = self._head.next 
                        if self._head == None: 
                            self._tail=None 
                    else: 
                        anterior = node.prev 
                        siguiente = node.next 
                        anterior.next = siguiente  
                        siguiente.prev= anterior  
                        if node.next==None: #es porque el nodo se encuentra en la cola
                            self._tail = self._tail.prev 
                            if self._tail==None:
                                self._head = None 
                else:
                    node = node.next 
                    
            prev = node
            node = node.next 
        return resultado 
            
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
