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
        outputList = MySList()
        if self.isSorted() and other.isSorted():
            node1 = self._head
            node2 = other._head

            while node1:
                next1 = node1.next
                if node1.elem == next1.elem:
                    node1.next = next1.next
                    if next1.next == None:
                        node1 = self._tail
                else:
                    node1 = next1
            while node2:
                next2 = node2.next
                if node2.elem == next2.elem:
                    node2.next = next2.next
                    if next2.next == None:
                        node2 = other._tail
                else:
                    node2 = next2

            node1 = self._head
            node2 = other._head
            firstListOver = False
            secondListOver = False
            while firstListOver == False and secondListOver == False:
                if node1 == None:
                    firstListOver = True
                elif node2 == None:
                    secondListOver = True
                elif node1.elem > node2.elem:
                    if node2 == None:
                        secondListOver = True
                    else:
                        outputList.append(node2.elem)
                        node2 = node2.next
                else:
                    if node1 == None:
                        firstListOver = True
                    else:
                        outputList.append(node1.elem)
                        node1 = node1.next

            if firstListOver:
                while node2:
                    outputList.append(node2.elem)
                    node2 = node2.next
            else:
                while node1:
                    outputList.append(node1.elem)
                    node1 = node1.next

            return outputList

        else:
            return None











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
