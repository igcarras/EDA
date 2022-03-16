# coding=utf-8
# """MARIO SANTIUSTE SARABIA GRUPO 84 EDA ING. INF."""
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
        "Condiciones para que se ejecute el método"
        if self.isSorted() and other.isSorted():
            #Lista a devolver
            newList = MySList()

            #Elementos de las listas que se van a ir comparando
            checkNode1 = self._head
            checkNode2 = other._head

            "Mientras haya nodos por meter:"
            while checkNode1 or checkNode2:

                #Si se repiten elementos se pasa al siguiente nodo
                if checkNode1 and checkNode1.next and checkNode1.elem == checkNode1.next.elem:
                    checkNode1 = checkNode1.next
                elif checkNode2 and checkNode2.next and checkNode2.elem == checkNode2.next.elem:
                    checkNode2 = checkNode2.next

                #Se introduce el nodo de menor tamaño y se pasa al siguiente
                elif checkNode1 and checkNode2 and checkNode1.elem < checkNode2.elem:
                    newList.append(checkNode1.elem)
                    if checkNode1: checkNode1 = checkNode1.next
                elif checkNode2 and checkNode1 and checkNode2.elem < checkNode1.elem:
                    newList.append(checkNode2.elem)
                    if checkNode2: checkNode2 = checkNode2.next

                #Si los nodos son iguales se mete uno cualquiera y se pasa a los siguientes
                elif checkNode2 and checkNode1 and checkNode2.elem == checkNode1.elem:
                    newList.append(checkNode1.elem)
                    if checkNode1: checkNode1 = checkNode1.next
                    if checkNode2: checkNode2 = checkNode2.next

                #Si se acaba una lista se terminan de meter los de la otra
                elif checkNode1:
                        newList.append(checkNode1.elem)
                        checkNode1 = checkNode1.next
                elif checkNode2:
                    newList.append(checkNode2.elem)
                    checkNode2 = checkNode2.next

            return newList

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
