#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/isegura/EDA/blob/master/Josephus_problem.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# ## Implementation of Josephus Problem
# 
# We are going to implement a general solution for the josephus problem. Our function takes two parameters:
# - numSoldiers which is the initial number of soldiers standing in a circle waiting to be executed. 
# - knum which indicates that k-1 persons are skipped and kth person is killed in circle
# 
# 
# First, let met write the Queue class

# In[3]:


class Queue:
  """FIFO Queue implementation using a Python list as storage. 
  We add new elements at the tail of the list (enqueue)
  and remove elements from the head of the list (dequeue)."""
  
  def __init__(self):
    """Create an empty queue"""
    self._items=[]
    
  def __len__(self):
    """Return the number of elements in the queue"""
    return len(self._items)

  def isEmpty(self):
    """Return True if the queue is empty"""
    return len(self)==0

  def __str__(self):
    return str(self._items)  

  def enqueue(self,e):
    """Add the element e to the tail of the queue"""
    self._items.append(e)
    
  def dequeue(self):
    """Remove and return the first element in the queue"""
    result=None
    if self.isEmpty():
      print('Error: Queue is empty')
    else:
        #remove first item from the list
        result=self._items.pop(0) 
    return result

  def front(self):
    """Return the first element in the queue"""
    result=None
    if self.isEmpty():
      print('Error: Queue is empty')
    else:
        #remove first item from the list
        result=self._items[0]
    return result
  
  
q=Queue()
print('isEmpty()',q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print('Content of queue',str(q))
print('front (first) element',q.front())
print('isEmpty()',q.isEmpty())
print('dequeue():',q.dequeue())
print('Content of queue',str(q))
print('front element:',q.front())
print('size:',len(q))


# Now, we implement the function for the Josephus problem:

# In[4]:


def josephus(num, k):
  q=Queue()
  #saved soldiers into the queue.
  for i in range(1,num+1):
    q.enqueue(i)
    
  while len(q)>1:
    count=1
    #k-1 dequeue/enqueue operations
    while count<k:
      q.enqueue(q.dequeue())
      count=count+1
    #kill the kth soldier
    print(str(q.dequeue()) + ' was killed')
  print('Surviving position: ' + str(q.front()))
  
josephus(24,3)


