from dlist import DList
from dlist import DNode

class DList2(DList):
    def removeNeighbours(self, x):
        if len(self) == 0:
            print('List is empty')
            return
    
        node = self._head
    
        while node:
            if node.elem == x:
                # Eliminar el nodo previo si existe
                if node.prev:
                    node.prev = node.prev.prev
                    if node.prev: 
                        node.prev.next = node
                else:
                    self._head = node
                    self._head.prev = None
                    
    
                # Eliminar el nodo siguiente si existe
                if node.next:
                    node.next = node.next.next
                    if node.next:
                        node.next.prev = node
                    else:
                        self._tail = node
                        self._tail.next = None
                
                    
                self._size -= 1 #vale con uno
                return
    
            node = node.next


mylist = DList2()
expected = DList2()
for x in [1, 2, 2, 6,7,2,4]:
    mylist.addLast(x)
    
print(mylist)
mylist.removeNeighbours(2)
print(mylist)