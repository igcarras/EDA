import random
from dlist import DList
    
def merge(left, right):

  if left._tail and right._head:
      if left._tail.elem >= right._head.elem:
           left._tail.next = right._head
           right._head.prev = left._tail
           left._tail = right._tail
           left._size += right._size
           return left
      
  newList=DList()
  node1 = left._head
  node2 = right._head
  
  while node1 and node2:
      
      if node1.elem  > node2.elem:
          newList.addLast(node1.elem)
          node1 = node1.next
      else:
          newList.addLast(node2.elem)
          node2 = node2.next
          
 
  while node1:
    newList.addLast(node1.elem)
    node1 = node1.next
 
  while node2:
    newList.addLast(node2.elem)
    node2 = node2.next
  
  return newList

def split(l):
    
    left = DList()
    right = DList()
     
    i=0
    node = l._head
    
    while(i<len(l)):
        
        if i < len(l)//2:
            left.addLast(node.elem)
        else:
            right.addLast(node.elem)
        i+=1
        node=node.next
            
   
    return left, right

def mergesort_optimized(A):
 
    if A==None or len(A)==0:
        return None
    if len(A)==1:
       return A
   
    left, right = split (A)
  
    sorted1=mergesort_optimized(left)
    sorted2=mergesort_optimized(right)
    
    return merge(sorted1,sorted2)





#Test mergesort

data=DList()
for i in range(10):
  data.addLast(random.randint(0,10))

print("\ndata={}".format(data))
print(mergesort_optimized(data))






