class DoublyNode:
  def __init__(self, e, n=None, p=None ):
    self.element = e
    self.next = n
    self.prev = p



class DoublyLinkedList:
  def __init__(self):
    """creates an empty list"""
    self.head=None
    self.tail=None
    self.size=0
        
  def isEmpty(self):
    """Checks if the list is empty"""
    return self.head is None   
    
  def addLast(self,e):
    """Add a new element, e, at the end of the list"""
    #create the new node
    newNode=DoublyNode(e)
    
    if self.isEmpty():
      self.head=newNode
    else:
      newNode.prev=self.tail
      self.tail.next=newNode
      
    #update the reference of head to point the new node
    self.tail=newNode
    #increase the size of the list  
    self.size=self.size+1
   
  
  def __str__(self):
    """Returns a string with the elements of the list"""
    temp=self.head
    strList=''
    while temp is not None:
      strList=strList+','+str(temp.element)
      temp=temp.next
    return strList[1:]
  
  
  def removeAlternate(self):

   if self.isEmpty():
     return "Empty list!!"

   if self.size == 1:
     return self

   count = 0
   current = self.head
   while current.next:
     #print(current.element)
     #print(self)
     if count%2 != 0:
       if current.next.next:
           newNext = current.next.next
           current.next = newNext
           newNext.prev = current
       else:
           current.next = None
           self.tail = current
           
     else:
       current = current.next
       
     count +=1


l= DoublyLinkedList()
for i in range (20):
    l.addLast(i)
l.removeAlternate()
print(l)
   

