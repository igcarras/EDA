from slist import SList
import sys

class SList2(SList):

    def sumLastN(self, n):
        """returns the sum of the last n elements of the list"""
        #variable for acumulate the sum of the last N elements of the list
        
        if n < 0 :
           print('Error:', n, ' cannot be a negative number')
           return None
        
        if n > len(self) :
           n=len(self)
        
        # calculate number of steps to traverse the list
        n = len(self) - n
            
        #move throught the list until to reach the nth node
        itNode = self._head
        while n > 0:
            itNode = itNode.next
            n = n - 1
    
        result = 0
        
        # now, itNode is the first node to sum
        while itNode:  
            #accumulate values in result variable
            result = result + itNode.elem
            #move to next Node
            itNode = itNode.next
    
        
        return result
    
    #method for inserting a new node in the middle
    def insertMiddle(self, elem):
        
        if self.isEmpty():
            self.addFirst(elem)
        else:
            position = len(self)
            if position % 2 == 0:
                # if even then insert at the middle
                self.insertAt(position//2,elem)
    
                #print("Insertado elemento:", elem, " en ", len/2)
            else:
                # if odd then insert at the middle+1
                self.insertAt((position+1)//2,elem)
    
                #print("Insertado elemento2:", elem, " en ", (len+1)/2)

    
    def insertList(self,inputList,start,end):
        if start<0 or start>end or end>=len(self):
            print(start,end, " are wrong positions!")
            return 
        
        i=0
        nodePrev=None
        nodeIt=self._head
        while i<start:
            i+=1
            nodePrev=nodeIt
            nodeIt=nodeIt.next
            
        #nodePrev is the previous node to the node at position start
        while i<=end:
            i+=1
            nodeIt=nodeIt.next
            
        #nodeIt is the node at the position end 
         
        
        #we gets the last node of the inputList
        if inputList.isEmpty():
            #we must remove the nodes from start to end positions
            if nodePrev==None:
                if nodeIt!=None:
                    self._head=nodeIt
            else:
                nodePrev.next=nodeIt
                
        else:
            lastNode=inputList._head
            while lastNode.next!=None:
                lastNode=lastNode.next
            
            
            lastNode.next=nodeIt
            
            
            if nodePrev==None:
                self._head=inputList._head
                
            else:
                nodePrev.next=inputList._head
            
        self._size=self._size - (end - start-1)


    def reverseK(self,k):
        #reverse the list in groups of given size
        
        #check
        if self.isEmpty is True:
            print('List is empty')
            return
        
        current=self._head  #traversal variable
        aux1=SList2()       #aux list to keep the inverted groups
        aux2=SList2()       #aux list to keep the inverted groups joined in a SList
       
        while current!=None:
            c=0
            
            #loop to invert the k first elements and remove them from original list
            while c<k and current!=None:
                current=current.next
                aux1.addFirst(self.removeFirst())
                c+=1
                
            current2=aux1._head
            
            #loop to remove the elements from aux list 1 and add them  to aux list 2
            while current2:
                current2=current2.next
                aux2.addLast(aux1.removeFirst())
        
        #convert aux list 2 into original list                      
        self._head=aux2._head


    def maximumPair(self):
        """return the maximum sum of equidistant nodes"""
        result=None
        if self.isEmpty():
            return result
        
        if len(self)==1:
            return self.getAt(0)
        
        
        _half=len(self)//2
        left=SList2()
        node=self._head
        for i in range(_half):
            left.addLast(node.elem)
            node=node.next
            
        if len(self)%2!=0:
            #print('ES IMPAR', _half, self.getAt(_half))
            node=node.next
        
        right=SList2()
        for i in range(_half):
            right.addFirst(node.elem)
            node=node.next
            
        
        result=-sys.maxsize
        
        nodeL=left._head
        nodeR=right._head
        i=0
        while i<len(left):
            sumPair=nodeR.elem + nodeL.elem
            nodeL=nodeL.next
            nodeR=nodeR.next
            i+=1
            if sumPair>result:
                result=sumPair
            
            
        if len(self)%2!=0:
            #print('ES IMPAR', _half, self.getAt(_half))
            result=max(result,self.getAt(_half))
            
        return result
            
            
l=SList2()
l2=SList2()

for x in [0,1,2,3,4,5,6,7,8,9]:
    l.addLast(x)
    
for x in ['a','b','c']:
    l2.addLast(x)
print(l)
l.insertList(l2,1,len(l)-1)
print(l)
