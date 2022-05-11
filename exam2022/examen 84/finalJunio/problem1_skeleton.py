
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
        """removes those nodes whose element divides some of the other elements in the list"""
        ...
        


        
import random
if __name__=='__main__':
    l=MyDList()
    data=[]
    
    for i in range(15):
        data.append(random.randint(0,15))
        
    data.sort()
    for x in data:
        l.append(x)
    
    print(l)
    l.removeDividers()
    print(l)
    print()        
        
        
        
        