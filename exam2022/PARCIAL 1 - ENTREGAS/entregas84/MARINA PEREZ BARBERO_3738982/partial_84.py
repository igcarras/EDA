# coding=utf-8
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
        if self.isSorted() == True and other.isSorted() == True:
            if self._head == None:
                if other._head == None:
                    print("Lista vacia")
                self._head = other._head
                self._tail = other._tail
            elif other._head == None:
                return
            else:
                current_1 = self._head
                current_2 = other._head
                aux = MySList()
                while current_1 or current_2:
                    if current_1.elem >= current_2.elem:
                        aux.append(current_1)
                        aux.append(current_2)
                    else:
                        aux.append(current_2)
                        aux.append(current_1)
                    current_1 = current_1.next
                    current_2 = current_2.next

                while current_1:
                    aux.append(current_1)
                    current_1 = current_1.next
                while current_2:
                    aux.append(current_2)
                    current_2 = current_2.next
                current_aux = aux._head
                previus_aux = None
                while current_aux:
                    if previus_aux.elem == current_aux.elem:
                        if current_aux == self._head:
                            self._head = self._head.next
                        elif current_aux == self._tail:
                            self._tail = previus_aux
                            self._tail.next = None
                        else:
                            previus_aux.next = current_aux.next
                    previus_aux = current_aux
                    current_aux = current_aux.next


                current_3 = aux._head
                while current_3:
                    current_3 = current_3.next
                self._head = aux._head
                self._tail = current_3

        else:
            return  None



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
