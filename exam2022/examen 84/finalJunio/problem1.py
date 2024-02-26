
class DNode:
    def __init__(self,e, next=None, prev=None):
        self.elem=e
        self.next=next
        self.prev=prev
        
class MyDList:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
  
    def append(self,e):
        newNode=DNode(e)
        if self._head==None:
            self._head=newNode
        else:
            newNode.prev=self._tail
            self._tail.next=newNode
           
        self._tail=newNode
        self._size+=1
        
    def __len__(self):
        return self._size
    
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
       
        
    def isSorted(self):
        """checks if the list is sorted in ascending order"""
        if len(self)<=1:
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
    
        
    def removeDividers(self):
        
        if self.isSorted()==False:
            print('Error: list should be sorted!!!')    

        elif len(self)>1: #is sorted and with two or more elements
 
            node1=self._head
            while node1 != None:
                div=node1.elem
                if div!=0:
                    found=False #this indicates if we have found some element that is divisible by div
                    node2=node1.next
                    
                    while not found and node2!=None:
                        
                        if node2.elem%div==0:
                            found=True
                            #we have to remove node1
                            if node1==self._head:
                                self._head=self._head.next 
                                self._head.prev=None
                            else:
                                #In this case, node1 always has next and prev
                                #we have to remove node1
                                #we never remove the _tail, for this reason, we cannot modify _tail
                                node1.prev.next=node1.next
                                node1.next.prev=node1.prev
                                
                            self._size -=1
                            
                        else:
                            node2=node2.next      
                    
                
                node1 = node1.next
            
    
            
import random
if __name__=='__main__':
    l=MyDList()
    data=[]
    
    for i in range(20):
        data.append(random.randint(0,15))
        
    data.sort()
    for x in data:
        l.append(x)
        
    print(l)
    print(l.isSorted())
    
    l.removeDividers()
    print(l)
    print(len(l))
        
    print(l)
    l.removeDividers()
    print(l)
    print()
    
    l=MyDList()
    for i in [0,0,0,1,1,3,3,3,5,6,7,8,11,13,15,16,18]:
        l.append(i)
    print(l)
    l.removeDividers()
    print(l)
    print()

    l=MyDList()
    for i in [1,1,1,1,1,1]:
        l.append(i)
    print(l)
    l.removeDividers()
    print(l)
    print()
