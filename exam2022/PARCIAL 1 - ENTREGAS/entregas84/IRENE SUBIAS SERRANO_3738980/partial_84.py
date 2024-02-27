# coding=utf-8
# Irene Subías Serrano

class SNode:
  def __init__(self, e, next=None):
    self.elem = e
    self.next = next
    
    
class MySList():
    
    def __init__(self):
        self._head = None
        self._tail = None
        
    def __str__(self):
        """Returns a string with the elements of the list"""
        ###This functions returns the same format used
        ###by the Python lists, i.e, [], ['i'], ['a', 'b', 'c', 'd']
        ###[1], [3, 4, 5]
        nodeIt=self._head
        result='['
        while nodeIt:
            result+= str(nodeIt.elem)+ ", "
            nodeIt=nodeIt.next

        if len(result)>1:
            result=result[:-2]

        result+=']'
        return result
    
    def append(self,e):
        """Adds a new element, e, at the end of the list"""
        #create the new node
        newNode=SNode(e)
        #the last node must point to the new node
        #now, we must update the _tail reference
        if self._head==None:
            self._head=newNode
        else:
            self._tail.next= newNode
        
        self._tail=newNode

    def isSorted(self):
        "returns True if self is sorted"
        if self._head==None:
            return True
        else:
            node1=self._head
            node2=node1.next
            while node2:
                if node1.elem>node2.elem:
                    return False
                node1=node2
                node2=node2.next
                
        return True

    def merge(self, other):
        "Merge of two ordered lists. No duplicates allowed."
        if other.isSorted() and self.isSorted():
            l = MySList()
            index1 = self._head
            index2 = other._head
            last = None
            while index1 or index2:
                if index1 and index2:
                    if index1.elem < index2.elem and index1.elem != last:
                        l.append(index1.elem)
                        last = index1.elem
                        index1 = index1.next
                    elif index1.elem == index2.elem and index1.elem != last:
                        l.append(index1.elem)
                        last = index1.elem
                        index1 = index1.next
                        index2 = index2.next
                    elif index1.elem > index2.elem != last:
                        l.append(index2.elem)
                        last = index2.elem
                        index2 = index2.next
                    elif index1.elem == last:
                        index1 = index1.next
                    elif index2.elem == last:
                        index2 = index2.next
                elif index1:
                    if index1.elem != last:
                        l.append(index1.elem)
                        last = index1.elem
                        index1 = index1.next
                    else:
                        index1 = index1.next
                else:
                    if index2.elem != last:
                        l.append(index2.elem)
                        last = index2.elem
                        index2 = index2.next
                    else:
                        index2 = index2.next
            return l
        else:
            return None


import random
if __name__=='__main__':
       #Please, uncomment the code for test each function
        l2=MySList()

        for i in range(10):
            l2.append(random.randint(0,20))
        print(l2)

        l3 = MySList()
        for i in range(10):
            l3.append(i)

        print('l2:', str(l2))
        print('l3:', str(l3))

        print("List merged:", str(l2.merge(l3)))
        print("List merged:", str(l3.merge(l2)))
        
        data=[]
        for i in range(5):
            x=random.randint(0,10)
            if x not in data:
                data.append(x)

        data.sort()
        l2=MySList()
        for x in data:
            l2.append(x)
            
        data=[]
        for i in range(7):
            x=random.randint(0,10)
            if x not in data:
                data.append(x)
            
        data.sort()
        l3=MySList()
        for x in data:
            l3.append(x)

        print('l2:', str(l2))
        print('l3:', str(l3))
        print("List merged:" , str(l2.merge(l3)))
        print("List merged:" , str(l3.merge(l2)))
