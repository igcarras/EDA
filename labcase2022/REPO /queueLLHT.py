# -*- coding: utf-8 -*-


class SNode:
  def __init__(self, e, next=None):
    self.elem = e
    self.next = next

class Queue:
    """This is the implementation of a queue based on a singly linked list. We use 
    a reference to the first node, named _head, and also a reference 
    to the last node, named as _tail. Also we keep an attribute, _size, 
    to store the number of nodes"""
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
    
    
    def isEmpty(self):
        """Checks if the list is empty"""
        return self._head == None   
        
    def __len__(self):
        return self._size
 
    def dequeue(self):
        """Removes the first element of the list"""
        result=None
        if self.isEmpty():
            print('Error: queue is empty!')
        else:
            #gets the first element, which we will return later
            result=self._head.elem
            #updates _head to point to the new _head (the next node)
            self._head=self._head.next
            #if the queue only has one node, _tail must be None
            if self.isEmpty():
                self._tail=None
            #decreases the _size of the queue
            self._size -= 1
            
        return result 

    def front(self):
        """returns the first element of the queue"""
        result=None
        if self.isEmpty():
            print('Error: queue is empty!')
        else:
            #gets the first element, which we will return later
            result=self._head.elem
        return result 

    def tail(self):
        """returns the last element of the queue"""
        result=None
        if self.isEmpty():
            print('Error: queue is empty!')
        else:
            #gets the _tail element, which we will return later
            result=self._tail.elem
           
            
        return result 

    def enqueue(self,e):
        """Adds a new element, e, at the end of the queue"""
        #create the new node
        newNode=SNode(e)
        #the last node must point to the new node
        #now, we must update the _tail reference
        if self.isEmpty():
            self._head=newNode
        else:
            self._tail.next= newNode
        #update _tail to point the new last node
        self._tail=newNode
        #increases the _size of the list
        self._size += 1
    
    
    def __str__(self):
        """Returns a string with the elements of the queue"""
        result=''
        nodeIt=self._head
        
        while nodeIt: #nodeIt!=None
            result=result+','+str(nodeIt.elem)
            nodeIt=nodeIt.next
        #we must remove the first comma ','
        if len(result)>0:
            result=result[1:]

        return result



import random
if __name__=='__main__':

    s=Queue()
    print("Queue:{}, len={}".format(str(s),len(s)))

    #we generate 5 random integers
    for i in range(5):
        #creates a positive integer between 0 <=x<= 100
        x=random.randint(0,100)
        s.enqueue(x)
        print("after enqueue({}):{}, len:{}".format(x,str(s),len(s)))


    print()
    print("front of the queue:", s.front()) 
    print("_tail of the queue:", s.tail())
    print()


    print()
    while not s.isEmpty():
        print("front of {}: {}".format(str(s),s.dequeue())) 
        print("after pop: {}, len={}".format(s,len(s)))
        print()