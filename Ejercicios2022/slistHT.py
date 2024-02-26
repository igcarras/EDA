# -*- coding: utf-8 -*-


class SNode:
  def __init__(self, e, next=None):
    self.elem = e
    self.next = next
    

class SList:
    """This is the implementation of a singly linked list. We use 
    a reference to the first node, named _head, and also a reference
    to the last node, named as _tail. Also we keep an attribute, _size,
    to store the number of nodes"""
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
    
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        """Checks if the list is empty"""
        #return self._head == None   
        return len(self)==0   

    def __str__(self):
        """Returns a string with the elements of the list"""
        ###This functions returns the same format used 
        ###by the Python lists, i.e, [], ['i'], ['a', 'b', 'c', 'd']
        ###[1], [3, 4, 5]
        nodeIt=self._head
        result='['
        while nodeIt:
            if type(nodeIt.elem)==int:
                result+= str(nodeIt.elem)+ ", "
            else:
                result+= "'"+str(nodeIt.elem)+ "', "
            nodeIt=nodeIt.next
        
        if len(result)>1:
            result=result[:-2]

        result+=']'
        return result
    

    def addFirst(self,e):
        """Add a new element, e, at the beginning of the list"""
        #create the new node
        newNode=SNode(e)
        #the new node must point to the current _head
        
        if self.isEmpty():
            self._tail=newNode
        else:
            newNode.next=self._head

        #update the reference of _head to point the new node
        self._head=newNode
        #increase the _size of the list
        self._size+=1
    
    
    def addLast(self,e):
        """Adds a new element, e, at the end of the list"""
        #create the new node
        newNode=SNode(e)
        #the last node must point to the new node
        #now, we must update the _tail reference
        if self.isEmpty():
            self._head=newNode
        else:
            self._tail.next= newNode
        
        self._tail=newNode

        #increase the _size of the list
        self._size+=1
    
    
    
  
    
    def removeFirst(self):
        """Removes the first element of the list"""
        result=None
        if self.isEmpty():
            print('Error: list is empty!')
        else:
            #gets the first element, which we will return later
            result=self._head.elem
            #updates _head to point to the new _head (the next node)
            self._head=self._head.next
            #if the list only has one node, _tail must be None
            if self._head==None:
                self._tail=None
            self._size-=1
        
        return result
    
    

      
    def removeLast(self):
        """Removes and returns the last element of the list"""
        result=None
        if self.isEmpty():
            print('Error: list is empty!')
        elif len(self)==1:
            result=self.removeFirst()
        else:
            result=self._tail.elem

            penult=self._head
            while penult.next!=self._tail:
                penult=penult.next
            
            penult.next=None
            self._tail=penult
            
            self._size-=1
        
        return result

      
      
    def getAt(self,index):
        """return the element at the position index.
        If the index is an invalid position, the function
        will return -1"""
        result=None
        if index not in range(0,len(self)): 
            print(index,'Error getAt: index out of range')
        else:
            nodeIt=self._head
            i=0
            while nodeIt and i<index:
                nodeIt=nodeIt.next
                i+=1

            #nodeIt is at the position index
            result=nodeIt.elem

        return result

    def index(self,e):
        """returns the first position of e into the list.
        If e does not exist in the list, 
        then the function will return -1"""
        nodeIt=self._head
        index=0
        while nodeIt:
            if nodeIt.elem==e:
                return index
            nodeIt=nodeIt.next
            index+=1
            
        #print(e,' does not exist!!!')
        return -1 
      
    
    
   
    def insertAt(self,index,e):
        """This methods inserts a new node containing the element e at the index
        position in the list"""
        if index not in range(0,len(self)+1): 
            print(index, 'Error insertAt: index out of range')
        elif index==0:
            self.addFirst(e)
        elif index==len(self):
            self.addLast(e)
        else:
            nodeIt=self._head
            for i in range(index-1):
                nodeIt=nodeIt.next
            
            #nodeIt is at index-1
            newNode=SNode(e)
            newNode.next = nodeIt.next
            #previous must point with its next reference to the new node
            nodeIt.next = newNode
            self._size += 1
      
    def removeAt(self,index):
        """This methods removes the node at the index position in the list"""
        result=None
        if index not in range(len(self)): 
            print(index,'Error removeAt: index out of range')
        elif index==0:
            result= self.removeFirst()
        elif index==len(self)-1:
            result= self.removeLast()
        else:
            #we must to reach the node before the node at the index position
            nodeIt=self._head
            for i in range(index-1):
                nodeIt=nodeIt.next
                
            #nodeIt is the node at index -1 position
            #nodeIt.next is the node at index position
            auxNode=nodeIt.next #node to remove
            result=auxNode.elem
            nodeIt.next = auxNode.next
            
            self._size-=1
        
        return result

if __name__=='__main__':
    import random
    l=SList()
    for i in range(5):
        l.addLast(random.randint(-5,5))

    print('Content of l:', l)
    print('len(l):', len(l))
    print()

    while l.isEmpty()==False:
        print('after removeFirst()={}, l={}, len={}'.format(l.removeFirst(),l,len(l)))


    for i in range(3):
        x=random.randint(-5,5)
        l.addFirst(x)
        print('after addFirst({}), l={}, len={}'.format(x,l,len(l)))

    print('Content of l:', l)
    print('len(l):', len(l))
    print()

    while l.isEmpty()==False:
        print('after removeLast()={}, l={}, len={}'.format(l.removeLast(),l,len(l)))
    print('---------------------')
    for i in range(3):
        x=random.randint(-5,5)
        l.addFirst(x)
        l.addLast(x)

    print('Content of l:', l)
    print('len(l):', len(l))
    print()

    for i in range(len(l)):
        print(' getAt({})={}'.format(i, l.getAt(i)))
    print()

    for i in range(3):
        x=random.randint(-5,5)
        print(' index({})={}'.format(x, l.index(x)))
    print()

    print('Content of l:', l)
    print('len(l):', len(l))
    print()

    x=666
    l.insertAt(0,x)
    print(' insertAt(0,{}), l={}, len={}'.format(x,l,len(l)))
    l.insertAt(len(l),x)
    print(' insertAt(len(l),{}), l={}, len={}'.format(x,l,len(l)))
    l.insertAt(len(l)//2,x)
    print(' insertAt(len(l)//2,{}), l={}, len={}'.format(x,l,len(l)))
    print()
    print()


    print(' removeAt(0)={}, l={}, len={}'.format(l.removeAt(0),l,len(l)))
    print(' removeAt(len(l)-1)={}, l={}, len={}'.format(l.removeAt(len(l)-1),l,len(l)))
    print(' removeAt(len(l)//2+1)={}, l={}, len={}'.format(l.removeAt(len(l)//2+1),l,len(l)))

