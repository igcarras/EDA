class SNode:
  def __init__(self, e, next=None):
    self.element = e
    self.next = next

"""Now, we can implement the class for a singly linked list. Our class only uses a refererence, head, for storing the first node, respectively. Moreover, it includes an atributte, named size, which stores the number of elements in the list."""

class SList:
  """This is the implementation of a singly linked list. We use 
  a reference to the first node, named head, and also a reference 
  to the last node, named as tail. Also we keep an attribute, size, 
  to store the number of nodes"""
  def __init__(self):
    self.head=None
    self.tail=None
    self.size=0
    
    
  def isEmpty(self):
    """Checks if the list is empty"""
    return self.head == None   
    
  def __len__(self):
    return self.size

  def addFirst(self,e):
    """Add a new element, e, at the beginning of the list"""
    #create the new node
    newNode=SNode(e)
    #the new node must point to the current head
    newNode.next=self.head
    
    if self.isEmpty():
      self.tail=newNode
      
    #update the reference of head to point the new node
    self.head=newNode
    #increase the size of the list  
    self.size += 1
    
    
  def addLast(self,e):
    """Adds a new element, e, at the end of the list"""
    #create the new node
    newNode=SNode(e)
    #the last node must point to the new node
    #now, we must update the tail reference
    
    if self.isEmpty():
      self.head=newNode
    else:
      self.tail.next= newNode
      
    self.tail=newNode


    #increase the size of the list  
    self.size += 1
    
    
  def __str__(self):
    """Returns a string with the elements of the list"""
    temp=self.head
    result=''
    while temp !=None:
      result=result+','+str(temp.element)
      temp=temp.next
    if len(result)>0:
      result=result[1:]
    return result
    
  
    
  def removeFirst(self):
    """Removes the first element of the list"""
    if self.isEmpty():
      print('Error: list is empty!')
      return None
    
    #gets the first element, which we will return later
    first=self.head.element
    #updates head to point to the new head (the next node)
    self.head=self.head.next
    #if the list only has one node, tail must be None
    if self.isEmpty():
      self.tail=None
    self.size -= 1
    
    return first
    
  def removeLast(self):
    """Removes and returns the last element of the list"""
    if self.isEmpty():
      print('Error: list is empty!')
      return None

    last=self.tail.element

    #we need to reach the penultimate node
    previous=None
    current=self.head
    while current.next is not None:
        previous=current
        current=current.next
    
    if previous is None:
      #The list only has one element
      self.head=None
    else:
      previous.next=None
    
    self.tail=previous 
    
    self.size -= 1
  
    return last
  

    
    
  def getAt(self,index):
    """Returns the element at the index position in the list"""
    
    #first, check the index is a right position in the list
    if index<0 or index>=self.size:
      print(index,'error: index out of range')
      return None
      
    #we need to reach the node at the index position in the list
    i=0
    current=self.head
    while  i<index:
      current=current.next
      i+=1
    #here, current is the node at the index position in the list
    #we return its element
    return current.element
      
      
  def index(self,e):
    """It returns the first position of e into the list. If the element 
    does no exist, then it returns -1"""
    
    index=0
    
    found=False
    
    current=self.head
    #we traverse the nodes while found is not True. 
    while current is not None and found==False:
      if current.element==e:
        found=True   #the loop condition becomes False
      else:
        current=current.next
        index=index+1
    
    #Warning: if e does not exist,  
    #index is the number of nodes in the list    
    if found:
      return index
    else:
      return -1
    
    
  def insertAt(self,index,e):
    """This methods inserts a new node containing the element e at the index
    position in the list"""
    
    #first, we must check that index is a right position. Note that index=size
    #is a right position for the insertAt method. 
    if index<0 or index>self.size:
      print(index, 'Error: index out of range')
      return 
   
  
    if index==0:
      self.addFirst(e)
    elif index==self.size:
      self.addLast(e)
    else:
      #we need to reach the previous node (the node at the index-1 position)
      i=0
      previous=self.head
      while i<index-1:
        previous=previous.next
        i=i+1

      #now, previous is the node with index-1
      #create the new node
      newNode=SNode(e)
      #newnode must point to the node after previous (which is previous.next)
      newNode.next = previous.next
      #previous must point with its next reference to the new node
      previous.next = newNode
      self.size += 1

      
  def removeAt(self,index):
    """This methods removes the node at the index position in the list"""
    
    #We must check that index is a right position in the list
    #Remember that the indexes in a list can range from 0 to size-1
    if index<0 or index>=self.size:
      print(index,'Error: index out of range')
      return 
       
    if index==0:
      self.removeFirst()
    elif index==self.size-1:
      self.removeLast()
    else:
      #we must to reach the node before the node at the index position
      i=0
      previous=self.head
      while i<index-1:
        previous=previous.next
        i=i+1
      
      #previous is the node at index -1 position
      
      previous.next = previous.next.next
      self.size=self.size-1
