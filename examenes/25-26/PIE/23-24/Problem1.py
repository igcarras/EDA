# -*- coding: utf-8 -*-


class SNode:
  def __init__(self, e, next=None):
    self.elem = e
    self.next = next


class SList:
    """This is the implementation of a singly linked list. We only use 
    a reference to the first node, named head"""
    def __init__(self):
        """This constructor creates an empty list"""
        self._head=None
        self._size=0
    
    def __len__(self):
        """It returns the size of the list"""
        return self._size


    def isEmpty(self):
        """"It returns True if the list is empty, and False eoc"""
        #return self._head == None
        return len(self)==0
    
    def uniqueList(self):
        other = SList()
        
        if self.isEmpty():
            return other
        
        x = self._head.elem
        node= self._head.next
        
        other._head = SNode(x)
        other._size +=1
        otherNode = other._head
        
        while node:
            if node.elem != x:
                x = node.elem
                otherNode.next = SNode (x)
                otherNode = otherNode.next
                other._size +=1
                
            node = node.next
        
        return other
            
            

    def __str__(self):
        """Returns a string with the elements of the list"""
        result=''

        nodeIt=self._head
        while nodeIt: #nodeIt!=None
            result+=','+str(nodeIt.elem)
            nodeIt=nodeIt.next
        
        if len(result)>0:
            result=result[1:]
        
        return result
  
   
    
    def addLast(self,e):
        """This functions adds e to the end of the list"""
        newNode=SNode(e)

        if self.isEmpty():
            self._head=newNode
        else:
            #we move throught the list until to reach the last node
            lastNode=self._head
            while lastNode.next: #lastNode!=None
                lastNode=lastNode.next
            #now, lastNode is the last node
            #the last node must point to the new node (which will be the new last node)
            lastNode.next=newNode
        self._size+=1

    
      
  


l= SList()
for i in [1,1,2,3,4,4,5,6,6,7,8,8]:
    l.addLast(i)
print (l.uniqueList())