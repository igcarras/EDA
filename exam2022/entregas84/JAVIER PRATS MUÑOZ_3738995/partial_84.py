
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

        current1 = self._head.next
        previous1 = self._head
        current2 = other._head.next
        previous2 = other._head
        Aux1 = MySList()
        Aux2 = MySList()

        if not self.isSorted() or not other.isSorted():
            return None

        while current1:
            if previous1.elem == current1.elem:
                previous1.next = current1.next
            else:
                previous1 = current1
            current1 = current1.next

        while current2:
            if previous2.elem == current2.elem:
                previous2.next = current2.next
            else:
                previous2 = current2
            current2 = current2.next
        print(self.__str__())
        print(other.__str__())

        current1 = self._head
        current2 = other._head

        while current1 and current2:
            if current1.elem < current2.elem:
                Aux1.append(current1.elem)
                Aux2.append(current2.elem)
            else:
                Aux2.append(current1.elem)
                Aux1.append(current2.elem)
            current1 = current1.next
            current2 = current2.next

        if not current1 and current2:
            while current2:
                Aux2.append(current2.elem)
                current2 = current2.next
        elif not current2 and current1:
            while current1:
                Aux2.append(current1.elem)
                current1 = current1.next

        current3 = Aux1._head

        while current3.next:
            current3 = current3.next

        current3.next = Aux2._head
        self._head = Aux1._head

        current1 = self._head.next
        previous1 = self._head

        while current1:
            if previous1.elem == current1.elem:
                previous1.next = current1.next
            else:
                previous1 = current1
            current1 = current1.next

Lista1 = MySList()

Lista1.append(1)
Lista1.append(1)
Lista1.append(1)
Lista1.append(2)
Lista1.append(2)
Lista1.append(2)
Lista1.append(3)
Lista1.append(5)
Lista1.append(10)
Lista1.append(10)
Lista1.append(10)

Lista2 = MySList()

Lista2.append(1)
Lista2.append(4)
Lista2.append(6)
Lista2.append(6)
Lista2.append(8)
Lista2.append(8)
Lista2.append(9)
Lista2.append(9)
Lista2.append(9)
Lista2.append(9)

print(Lista1.__str__())

Lista1.merge(Lista2)

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

