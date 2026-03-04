# -*- coding: utf-8 -*-
from dlist import DList
from dlist import DNode

class DList2(DList):

    def reverseHalves(self):
       
        if len(self) <=2:
            return
      
        node=self._head
        last1 = None
        init2 = None
        mid = len(self) //2
    
        for i in range (mid):
            node.next,node.prev=node.prev,node.next          
            last1 = node   
            node=node.prev
        
        init2 = node
       
        for i in range (mid,len(self)):
            node.next,node.prev=node.prev,node.next    
            node=node.prev
            
        self._head.next = self._tail
        self._tail.prev = self._head
        self._head = last1
        self._tail = init2
        self._tail.next = None
        self._head.prev = None
                
                    
if __name__=='__main__':
    
    print("empty list")
    l=DList2()
    print(l)
    l.reverseHalves()
    print(l)
    
    print("one elem")
    l=DList2()
    l.addLast(0)
    print(l)
    l.reverseHalves()
    print(l)
        
    l=DList2()
    for i in [0,1,2,3,4,5]:
        l.addLast(i)
    print(l)
    l.reverseHalves()
    print(l)

    l=DList2()
    for i in [0, 1,2,3,4]:
        l.addLast(i)
    print(l)
    l.reverseHalves()
    print(l)

    
    