# -*- coding: utf-8 -*-
from slistHT import SList

class SList2(SList):
    def removev1(self,e):
        """This solution is based on the functions index and remove"""
        index=self.index(e)
        if index!=-1:
            self.removeAt(index)
        else:
            print(e, ' does not exist!!!')
    
    def remove(self,e):
        """This solution does not not use any function of the SList class"""
        prev=None
        nodeIt=self._head
        found=False
        while not found and nodeIt : #nodeIt!=None
            if nodeIt.elem==e:
                #remove node
                if prev==None:
                    #it is the first node
                    self._head=self._head.next
                    if self._head==None:
                        self._tail=None
                else:
                    #it's not the first node
                    prev.next=nodeIt.next
                    if nodeIt.next==None:
                        #nodeIt was the last node
                        self._tail=prev

                self._size -=1
                found=True
            else:
                prev=nodeIt
                nodeIt=nodeIt.next
                
        if not found:
            print(e, ' does not exist!!!')
            
        
    def removeAllv1(self,e):
        """This solution is based on the functions index and removeAt"""
        index=self.index(e)
        while index!=-1:
            self.removeAt(index)
            index=self.index(e)
            
    def removeAll(self,e):
        """This solution does not not use any function of the SList class"""
        prev=None
        nodeIt=self._head
        while nodeIt : #nodeIt!=None
            if nodeIt.elem==e:
                #remove node
                if prev==None:
                    #it is the first node
                    self._head=self._head.next
                    if self._head==None:
                        self._tail=None
                else:
                    #it's not the first node
                    prev.next=nodeIt.next
                    if nodeIt.next==None:
                        #nodeIt was the last node
                        self._tail=prev
                self._size -=1
                
            prev=nodeIt
            nodeIt=nodeIt.next
            
    
    def getAtRevv1(self,index):
        """This solution is based on the function getAt"""
        result=None
        n=len(self)
        if index>=0 and index<n:
            result=self.getAt(n-1-index)
        else:
            print(index,' wrong!!!')
        return result          

    def getAtRev(self,index):
        """This solution is based on the function getAt"""
        result=None
        n=len(self)
        if index>=0 and index<n:
            i=0
            nodeIt=self._head
            while index<n-1-i:
                nodeIt=nodeIt.next
                i+=1
                
            result=nodeIt.elem
            
        else:
            print(index,' wrong!!!')
        return result          

    def getMiddle(self):
        result=None
        if self.isEmpty():
            print('An empty list does not have middle!!!')
        else:
            m=len(self)//2
            
            result=self.getAt(m)
        return result
    
    def count(self,e):
        cont=0
        nodeIt=self._head
        while nodeIt:
            if nodeIt.elem==e:
                cont+=1
            nodeIt=nodeIt.next
            
        return cont
    
    def isPalindrome(self):
        m=len(self)//2
        if m>0:
            for i in range(m+1):
                if self.getAt(i)!=self.getAtRev(i):
                    return False
            
        return True
        
    def isSorted(self):
        if len(self)<=1:
            return True
        else:
            node1=self._head
            node2=node1.next
            for i in range(1,len(self)):
                if node1.elem>node2.elem:
                    return False
                node1=node2
                node2=node2.next
                
            return True
        
    def removeDuplicatesSortedv1(self):
        if self.isSorted():
            if len(self)>1:
                i=1
                while i<len(self):
                    if self.getAt(i-1)==self.getAt(i):
                        self.removeAt(i)
                    else:
                        i+=1    
            
        else:
            print('list is not sorted!!!')
    
    def removeDuplicatesSorted(self):
        if self.isSorted():
            if len(self)>1:
                prev=self._head
                nodeIt=prev.next
                while nodeIt:
                    if prev.elem==nodeIt.elem:
                        prev.next=nodeIt.next
                        if nodeIt.next==None:
                            self._tail=prev
                        self._size-=1
                        nodeIt=nodeIt.next
                    else:
                        prev=nodeIt
                        nodeIt=nodeIt.next
            
        else:
            print('list is not sorted!!!')
            
    def removeDuplicates(self):
        nodeIt=self._head
        while nodeIt:
            prev=nodeIt
            nodeIt2=nodeIt.next

            e=nodeIt.elem
            while nodeIt2:
                if e==nodeIt2.elem:
                    prev.next=nodeIt2.next
                    if nodeIt2.next==None:
                        self._tail=prev
                    self._size-=1
                else:    
                    prev=nodeIt2

                nodeIt2=nodeIt2.next
                
            nodeIt=nodeIt.next
       
    def swapPairwise(self):
        if len(self)>1:
            node1=self._head
            node2=node1.next
            while node1 and node2:
                #swap elements
                node1.elem,node2.elem=node2.elem,node1.elem
                node1=node2.next
                if node1:
                    node2=node1.next
                

    def moveLastv1(self):
        """This function is based on the functions removeLast and addFirst"""
        if len(self)>1:
            x=self.removeLast()
            self.addFirst(x)
            
    def moveLast(self):
        if self.isEmpty():
            print('list is empty!!')
        else:
            penult=None
            last=self._head
            while last!=self._tail:
                penult=last
                last=last.next
            
            last.next=self._head
            self._head=last
            
            penult.next=None
            self._tail=penult
            
            
    def intersection(self,l2):
        output=SList2()
        if self.isSorted() and l2.isSorted():
            node1=self._head
            node2=l2._head
            
            while node1:
                while node2 and node2.elem<node1.elem:
                    node2=node2.next
                if node2!=None and node2.elem==node1.elem:
                    output.addLast(node1.elem)
                node1=node1.next
        
        return output

    def segregateOddEven(self):
        
        if len(self)>1:
            
            evens=SList2()
            odds=SList2()
            node=self._head
            while node:
                e=node.elem
                if e%2==0:
                    evens.addLast(e)
                else:
                    odds.addLast(e)
                    
                node=node.next
                
            if evens.isEmpty():
                self._head=odds._head
                self._tail=odds._tail
            elif odds.isEmpty():
                self._head=evens._head
                self._tail=evens._tail
            else:
                self._head=evens._head
                evens._tail.next=odds._head
                self._tail=odds._tail
                
              
import random

if __name__=='__main__':
   #Please, uncomment the code for test each function

    print()
    '''
    l1=SList2()
    for i in range(10):
        l1.addLast(random.randint(0,10))
    print("before remove(0)", l1)
    l1.remove(0)
    print("after remove(0)", l1)
    print()
    print("before remove(33)", l1)
    l1.remove(33)
    print("after remove(33)", l1)
    '''

    l2=SList2()
    for i in [7, 0, 8, 7, 6, 1, 7, 10, 2, 0, 9]:
        l2.addLast(i)



    print("before removing 7", l2)
    l2.removeAll(7)
    print("after removing 7:", l2)
    print()

    print("before removing -1", l2)
    l2.removeAll(-1)
    print("after removing -1:", l2)
    print()



    print(l2)
    for i in range(len(l2)):
        print("l2.getAt({})={}, l2.getAtRev({})={}".format(i,l2.getAt(i),i,l2.getAtRev(i)))
    print()



    print()
    print(l2)
    print("l2.getMiddle()={}".format(l2.getMiddle()))
    print()
    l2.remove(0)
    print(l2)
    print("l2.getMiddle()={}".format(l2.getMiddle()))
    print()


    '''
    l2.addFirst(10)
    l2.addLast(10)
    print(l2)
    print("l2.count(10)={}".format(l2.count(10)))
    print()
    print(l2)
    print("l2.count(2)={}".format(l2.count(2)))
    print()
    print(l2)
    print("l2.count(5)={}".format(l2.count(5)))
    print()
    '''

    '''
    print(l2)
    print("l2.isPalindrome()={}".format(l2.isPalindrome()))
    print()
    '''

    l3=SList2()
    for i in ['a','b','b','a']:
        l3.addLast(i)
    '''
    print(l3)
    print("Even case, l3.isPalindrome()={}".format(l3.isPalindrome()))
    print()
    l3.insertAt(2,'c')
    print(l3)
    print("Odd case, l3.isPalindrome()={}".format(l3.isPalindrome()))
    print()
    '''

    '''
    print(l3)
    print("l3.isSorted()={}".format(l3.isSorted()))
    print()
    '''

    '''
    l4=SList2()
    for i in range(8):
        l4.addLast(i)

    print(l4)
    print("l4.isSorted()={}".format(l4.isSorted()))
    print()

    l4.insertAt(1,1)
    l4.insertAt(1,1)
    l4.insertAt(6,3)
    l4.insertAt(8,5)
    l4.insertAt(9,5)
    l4.addLast(7)
    l4.addLast(7)
    l4.addFirst(0)
    l4.addFirst(0)

    print("before remove duplicates (sorted):",l4)
    l4.removeDuplicatesSortedv1()
    print("after remove duplicates (sorted):", l4)
    print()
    '''
    
    
    print(l2)
    l2.insertAt(4,6)
    l2.insertAt(4,6)
    l2.insertAt(4,6)
    print(l2)

    l2.addLast(9)
    l2.addLast(9)
    l2.addLast(9)
    
    l2.addFirst(7)
    l2.addFirst(7)
    
    print("before remove duplicates:", l2)
    l2.removeDuplicates()
    print("after remove duplicates:", l2)
    print()
    

    
    '''
    print("before swapPairwise:",l2)
    l2.swapPairwise()
    print("after swapPairwise:",l2)
    '''

    '''
    l2.moveLastv1()
    print("after moveLastv1:",l2)
    print()
    l2.moveLast()
    print("after moveLast:",l2)
    '''
    '''
    print(l4)
    l5=SList2()
    for i in [2,2,4,6,8,9]:
        l5.addLast(i)

    print("{}.intersection({})={}".format(l4,l5,l4.intersection(l5)))
    '''

    '''
    print("before segregateOddEven:",l2)
    l2.segregateOddEven()
    print("after segregateOddEven:",l2)
    print()
    print("before segregateOddEven:",l4)
    l4.segregateOddEven()
    print("after segregateOddEven:",l4)
    '''
