import random

class SNode:
  def __init__(self, e, next=None):
    self.elem = e
    self.next = next


class SList:
    def __init__(self):
        self._head=None
        self._size=0
    
    def __len__(self):
        return self._size
 
    def addLast(self,e):
        """This functions adds e to the end of the list"""
        newNode=SNode(e)

        if len(self)==0:
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
        
    def __str__(self):
        """Returns a string with the elements of the list"""
        result=''

        nodeIt=self._head
        while nodeIt: #nodeIt!=None
            result+=','+str(nodeIt.elem)
            nodeIt=nodeIt.next
        
        #we remove the first ','
        if len(result)>0: 
            result=result[1:]
        
        return result
        
    
    
    def orderByParity(self):
        
        if len(self) <= 1:
            return
        
        tail_node = None
        prev = None
        node = self._head
        
        while node and node.next:
            node = node.next
        tail_node = node
      
        node = self._head
        for i in range (len(self)):
           
            nodenext = node.next
           
            if node.elem %2 != 0:
             
               if prev:
                   prev.next = node.next
               else:
                   self._head = node.next
             
                
               node.next = None
               tail_node.next = node
               tail_node = node
               
               
            else: 
                prev = node
                
            node = nodenext
    def print_reverse_slist(self):
        self._print_reverse_slist(self._head)
        return
    def _print_reverse_slist(self, node: SNode):
        """Imprime los elementos desde el final al inicio usando recursión"""
        if node is None:
            return
        self._print_reverse_slist(node.next)
        print(node.elem, end=' ')


if __name__ == "__main__":
    l1=SList()
    for i in range(10):
        l1.addLast(random.randint(0,10))

    print("Lista original:")
    print(l1)
    print("Lista ordenada:")
    l1.orderByParity()
    print(l1)

    print("Lista invertida:")
    l1.print_reverse_slist()
