#Francisco Torija Jiménez, 100429111

class DNode:
    def __init__(self, e: int, next=None, prev=None) -> None:
        self.elem = e
        self.next = next
        self.prev = prev

class MyDList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def append(self, e: int) -> None:
        """adds e at the end of the list"""
        new_node = DNode(e)
        if self._head is None:
            self._head = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node

        self._tail = new_node
        self._size += 1

    def __len__(self):
        return self._size

    def __str__(self):
        """Returns a string with the elements of the list"""
        nodeIt = self._head
        result = '['
        while nodeIt:
            result += str(nodeIt.elem) + ", "
            nodeIt = nodeIt.next

        if len(result) > 1:
            result = result[:-2]

        result += ']'
        return result

    def remove_sublist(self, start: DNode, end: DNode, count:int) -> None:
        """remove the sublist from node start to node end, both included
        count is the number of nodes to be removed.
        It is not necessary to check it"""
        
        
        if start not in range(len(self)): 
            print(start,'Error')
            
        if end not in range(len(self)): 
            print(end,'Error')
            
        nodeStart = start.prev
        nodeEnd = end.next   
            
        nodeStart.next = nodeEnd
        nodeEnd.prev = nodeStart
        
        self._size -= count
        
        
    def remove_section_by_sum(self, k):
        """removes the consecutive nodes of the list
        whose elements sum k"""
        nodeIt = start = end = self._head
        suma = count = 0
        listAux = MyDList()
        while nodeIt:
            suma += nodeIt.elem 
            
            if suma == k:
                count += 1
                self.remove_sublist(start, end, count)
                break
            
            if suma > k:
                suma = count = 0
                start = end = nodeIt.next
            
            end = end.next
            nodeIt = nodeIt.next
            
        
        for i in len(self):
            listAux.append(i)
        
        return listAux
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

