# -*- coding: utf-8 -*-


class SNode:
  def __init__(self, e, next=None):
    self.elem = e
    self.next = next

"""Now, we can implement the class for a singly linked list. Our class only uses a refererence, head, for storing the first node, respectively. Moreover, it includes an atributte, named size, which stores the number of elements in the list."""

class Stack:
  """This is the implementation of a stack based on a singly linked list. 
  We only use a reference to the first node, named head. This head references
  to the peak of the stack"""
  def __init__(self):
    """This constructor creates an empty stack"""
    self._head=None
    self._size=0

  def __len__(self):
    """It returns the size of the stack"""
    return self._size

  def isEmpty(self):
    """"It returns True if the stack is empty, and False eoc"""
    #return len(self)
    return self._head == None

  def push(self,e):
    """Add a new element, e, on the stack (before the peak of the stack)"""
    #create the new node
    newNode=SNode(e)
    #the new node must point to the current head
    newNode.next=self._head
    #update the reference of head to point the new node
    self._head=newNode
    #increase the size of the list  
    self._size=self._size+1


  def pop(self):
    """Removes the peak (first element) of the stack"""
    result=None
    if self.isEmpty():
      print('Error: stack is empty!')
    else:  
      #gets the first element, which we will return later
      result=self._head.elem
      #updates head to point to the new head (the next node)
      self._head=self._head.next
      self._size-=1
    
    return result
    
  def top(self):
    """returns the peak (first element) of the stack"""
    result=None
    if self.isEmpty():
      print('Error: stack is empty!')
    else:  
      #gets the first element, which we will return later
      result=self._head.elem
      
    return result

  
  def __str__(self):
    """Returns a string with the elements of the list"""
    nodeIt=self._head
    result=''
    while nodeIt: #nodeIt!=None
      result+=','+str(nodeIt.elem)
      nodeIt=nodeIt.next

    #remove the first ','
    if len(result)>0:   
      result=result[1:]

    return result

"""
Once you have implemented the two classes, you can use them in order to create your own lists:
"""

import random

if __name__=='__main__':
	s=Stack()
	print("stack:{}, len={}".format(str(s),len(s)))

	#we generate 5 random integers
	for i in range(5):
	    #creates a positive integer between 0 <=x<= 100
	    x=random.randint(0,100)
	    s.push(x)
	    print("after push({}):{}, len:{}".format(x,str(s),len(s)))


	print()
	print("top (peak) of the stack:", s.top()) #1

	print()
	while not s.isEmpty():
	    print("top (peak) of  {}:{}".format(str(s),s.pop())) 
	    print("after pop: {}, len={}".format(s,len(s)))
	    print()

	print()
	for i in range(5):
	    s.push(i)
	    print("after push({}): {}, len={}".format(i,s,len(s)))