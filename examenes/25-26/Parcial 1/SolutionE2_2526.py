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

  def isEmpty(self):
    """Checks if the list is empty"""
    #return self.head == None
    return len(self)==0

  def addLast(self, e):
      """Add a new elem, e, at the end of the list"""
      # create the new node
      newNode = DNode(e)

      if self.isEmpty():
          self._head = newNode
      else:
          newNode.prev = self._tail
          self._tail.next = newNode

      # update the reference of _head to point the new node
      self._tail = newNode
      # increase the _size of the list
      self._size = self._size + 1

  def removeFirst(self):
      """Returns and remove the first elem of the list"""
      if self.isEmpty():
          print("Error: list is empty")
          return None

      result = self._head.elem
      self._head = self._head.next
      if self._head is None:
          self._tail = None
      else:
          self._head.prev = None

      self._size = self._size - 1
      return result

  def ringList (self, s):
    other = DList()
    current=self.head
    if s>0 and s<self.size :
        for i in range (0,s):
            """order of complexity O(n)"""
            other.addLast(self.removeFirst())
        """ring List pointers"""
        other.tail.next = other.head
        other.head.prev = other.tail
        return other
    else:
        print("error: wrong size")

