
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
        left=self._head
        otherleft=other._head
        right=self._tail
        countl=0
        countr=0
        length=0
        otherlength=0
        othercounter=0
        aux=MySList()


        #CHECK ORDER
        """
        while otherleft is not None:
            otherleft=otherleft.next
            otherlength+=1
        otherleft=other._head
        while otherleft and othercounter<otherlength-1:
            if otherleft.next.elem<otherleft.elem: return None
            otherleft=otherleft.next
        """
        if self._head==None:
            self._head==other._head
        if other._head==None:
            return self

        #Calculate original length
        while left is not None:
            left=left.next
            length+=1
    
        #Go to last node
        left=self._head
        while left and countr<length-1:
            if left.next.elem<left.elem: return None #exit if list is not ordered
            print("ELEM",left.elem)
            countr+=1
            left=left.next
        left.next=other._head #join two lists
        
        
        #Calculate New Lenth
        length=0
        left=self._head
        while left is not None:
            left=left.next
            length+=1
        print("NEWLONG",length)

        #remove duplicates
        countr=0
        left=self._head
        leftnext=self._head
        while left and countr<length-1:
            print("left next",left.next.elem,"left", left.elem) #me he trabado con los punteros
            if left.elem==leftnext.elem:
                leftnext=leftnext.next
            left.next=leftnext
            """
            if left.next.elem==left.elem and left: #me di cuenta de que esta implementacion no funiona si hay mas de dos elementos iguales seguidos
                left.next=left.next.next
                length-=1
            left=left.next    
            countr+=1
            """
            
        return(self)
        

            
            
        


print("Test")

"""

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

l=[1,1,1,1,1,1,1,2,3,4]
l2=[5,6,7,8,8]
lista=MySList()
lista2=MySList()
for i in l:
    lista.append(i)
for e in l2:
    lista2.append(e)
print(lista,lista2)
lista.merge(lista2)
print("Despues",lista)