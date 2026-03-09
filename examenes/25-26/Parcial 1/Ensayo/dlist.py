
class DNode:
  def __init__(self, e, n=None, p=None ):
    self.elem = e
    self.next = n
    self.prev = p

class DList:
  def __init__(self):
    """creates an empty list"""
    self._head=None
    self._tail=None
    self._size=0
    
    
  def __len__(self):
      return self._size
  
  def isEmpty(self):
    """Checks if the list is empty"""
    return self._head is None
  
  def addFirst(self,e):
    """Add a new elem, e, at the beginning of the list"""
    #create the new node
    newNode=DNode(e)
    #the new node must point to the current _head
    
    if self.isEmpty():
      self._tail=newNode
    else:
      newNode.next=self._head
      self._head.prev=newNode
      
    #update the reference of _head to point the new node
    self._head=newNode
    #increase the _size of the list
    self._size= self._size + 1
    
    
  def addLast(self,e):
    """Add a new elem, e, at the end of the list"""
    #create the new node
    newNode=DNode(e)
    
    if self.isEmpty():
      self._head=newNode
    else:
      newNode.prev=self._tail
      self._tail.next=newNode
      
    #update the reference of _head to point the new node
    self._tail=newNode
    #increase the _size of the list
    self._size= self._size + 1

  def __str__(self):
    """Returns a string with the elements of the list"""
    ###This functions returns the same format used
    ###by the Python lists, i.e, [], ['i'], ['a', 'b', 'c', 'd']
    ###[1], [3, 4, 5]
    nodeIt = self._head
    result = '['
    while nodeIt:
      if type(nodeIt.elem) == int:
        result += str(nodeIt.elem) + ", "
      else:
        result += "'" + str(nodeIt.elem) + "', "
      nodeIt = nodeIt.next

    if len(result) > 1:
      result = result[:-2]

    result += ']'
    return result

  
  def removeFirst(self):
    """Returns and remove the first elem of the list"""
    if self.isEmpty():
      print("Error: list is empty")
      return None
    
    result=self._head.elem
    self._head= self._head.next
    if self._head is None:
      self._tail=None
    else:
      self._head.prev = None

    self._size= self._size - 1
    return result
  
  def removeLast(self):
    """Returns and remove the last elem of the list"""
    if self.isEmpty():
      print("Error: list is empty")
      return None
    
    result=self._tail.elem
    self._tail= self._tail.prev
    if self._tail is None:
      self._head=None
    else:
      self._tail.next = None

    self._size= self._size - 1
    return result
  
  
  def insertAt(self,index,e):
    """It inserts the elem e at the index position of the list"""
    if index<0 or index>self._size:
      print('Error: index out of range')
      return
    
    if index==0:
      self.addFirst(e)
    elif index==self._size:
	    self.addLast(e)
    else:
      i=0
      aux=self._head
      while i<index:
        aux=aux.next
        i=i+1
      #aux is the node at the index position
      previous=aux.prev
      newNode=DNode(e)
      newNode.next=aux
      newNode.prev=previous
      aux.prev=newNode
      previous.next=newNode
      self._size= self._size + 1
      
      
  def getAt(self,index):
    """Returns the elem at the index position in the list"""
    
    #first, check the index is a right position in the list
    if index<0 or index>=self._size:
      print(index,'error: index out of range')
      return None
      
    #we need to reach the node at the index position in the list
    i=0
    current=self._head
    while  i<index:
      current=current.next
      i+=1
    #here, current is the node at the index position in the list
    #we return its elem
    return current.elem
      
      
  def index(self,e):
    """It returns the first position of e into the list. If the elem 
    does no exist, then it returns -1"""
    
    index=-1
    
    found=False
    
    current=self._head
    #we traverse the nodes while found is not True. 
    while current is not None and found==False:
      if current.elem==e:
        found=True   #the loop condition becomes False
      current=current.next
      index=index+1
    
    #Warning: if e does not exist,  
    #index is the number of nodes in the list    
    if found:
      return index
    else:
      return -1
    
  def removeAt(self,index):
    """This methods removes the node at the index position in the list"""
    
    #We must check that index is a right position in the list
    #Remember that the indexes in a list can range from 0 to _size-1
    if index<0 or index>=self._size:
      print(index,'Error: index out of range')
      return 
       
    if index==0:
      self.removeFirst()
    elif index==self._size-1:
      self.removeLast()
    else:
      #we must to reach the node at the index position
      i=0
      node=self._head
      while i<index:
        node=node.next
        i=i+1
      
      prevNode=node.prev
      nextNode=node.next
      
      prevNode.next=nextNode
      nextNode.prev=prevNode
      self._size= self._size - 1



#main
