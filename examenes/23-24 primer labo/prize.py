class Award:
  def __init__(self, e, next=None):
    self.elem = e
    self.next = next

class Prizes:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self):
        """Checks if the list is empty"""
        return self._head == None
    def __len__(self):
        return self._size
    def add(self, e):
        newNode=Award(e)
        if self.isEmpty():
            self._head=newNode
        else:
            self._tail.next= newNode
        self._tail=newNode
        self._size += 1

    def remove(self):
        result = None
        if not self.isEmpty():
            result = self._head.elem
            self._head = self._head.next
            if self.isEmpty():
                self._tail = None
            self._size -= 1
        return result
