#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class SNode:
  def __init__(self, e, next=None):
    self.element = e
    self.next = next

"""Now, we can implement the class for a singly linked list. Our class only uses a refererence, head, for storing the first node, respectively. Moreover, it includes an atributte, named size, which stores the number of elements in the list."""

class SList:
  """This is the implementation of a singly linked list. We use 
  a reference to the first node, named head, and also a reference 
  to the last node, named as tail. Also we keep an attribute, size, 
  to store the number of nodes"""
  def __init__(self):
    self.head=None
    self.tail=None
    self.size=0
    
    
  def isEmpty(self):
    """Checks if the list is empty"""
    return self.head == None   
    
  def __len__(self):
    return self.size

  def addFirst(self,e):
    """Add a new element, e, at the beginning of the list"""
    #create the new node
    newNode=SNode(e)
    #the new node must point to the current head
    newNode.next=self.head
    
    if self.isEmpty():
      self.tail=newNode
      
    #update the reference of head to point the new node
    self.head=newNode
    #increase the size of the list  
    self.size += 1
    
    
  def addLast(self,e):
    """Adds a new element, e, at the end of the list"""
    #create the new node
    newNode=SNode(e)
    #the last node must point to the new node
    #now, we must update the tail reference
    
    if self.isEmpty():
      self.head=newNode
    else:
      self.tail.next= newNode
      
    self.tail=newNode


    #increase the size of the list  
    self.size += 1
    
    
  def __str__(self):
    """Returns a string with the elements of the list"""
    temp=self.head
    result=''
    while temp !=None:
      result=result+','+str(temp.element)
      temp=temp.next
    if len(result)>0:
      result=result[1:]
    return result
    
  
    
  def removeFirst(self):
    """Removes the first element of the list"""
    if self.isEmpty():
      print('Error: list is empty!')
      return None
    
    #gets the first element, which we will return later
    first=self.head.element
    #updates head to point to the new head (the next node)
    self.head=self.head.next
    #if the list only has one node, tail must be None
    if self.isEmpty():
      self.tail=None
    self.size -= 1
    
    return first
    
  def removeLast(self):
    """Removes and returns the last element of the list"""
    if self.isEmpty():
      print('Error: list is empty!')
      return None

    last=self.tail.element

    #we need to reach the penultimate node
    previous=None
    current=self.head
    while current.next is not None:
        previous=current
        current=current.next
    
    if previous is None:
      #The list only has one element
      self.head=None
    else:
      previous.next=None
    
    self.tail=previous 
    
    self.size -= 1
  
    return last
  

    
    
  def getAt(self,index):
    """Returns the element at the index position in the list"""
    
    #first, check the index is a right position in the list
    if index<0 or index>=self.size:
      print(index,'error: index out of range')
      return None
      
    #we need to reach the node at the index position in the list
    i=0
    current=self.head
    while  i<index:
      current=current.next
      i+=1
    #here, current is the node at the index position in the list
    #we return its element
    return current.element
      
      
  def index(self,e):
    """It returns the first position of e into the list. If the element 
    does no exist, then it returns -1"""
    
    index=0
    
    found=False
    
    current=self.head
    #we traverse the nodes while found is not True. 
    while current is not None and found==False:
      if current.element==e:
        found=True   #the loop condition becomes False
      else:
        current=current.next
        index=index+1
    
    #Warning: if e does not exist,  
    #index is the number of nodes in the list    
    if found:
      return index
    else:
      return -1
    
    
  def insertAt(self,index,e):
    """This methods inserts a new node containing the element e at the index
    position in the list"""
    
    #first, we must check that index is a right position. Note that index=size
    #is a right position for the insertAt method. 
    if index<0 or index>self.size:
      print(index, 'Error: index out of range')
      return 
   
  
    if index==0:
      self.addFirst(e)
    elif index==self.size:
      self.addLast(e)
    else:
      #we need to reach the previous node (the node at the index-1 position)
      i=0
      previous=self.head
      while i<index-1:
        previous=previous.next
        i=i+1

      #now, previous is the node with index-1
      #create the new node
      newNode=SNode(e)
      #newnode must point to the node after previous (which is previous.next)
      newNode.next = previous.next
      #previous must point with its next reference to the new node
      previous.next = newNode
      self.size += 1

      
  def removeAt(self,index):
    """This methods removes the node at the index position in the list"""
    
    #We must check that index is a right position in the list
    #Remember that the indexes in a list can range from 0 to size-1
    if index<0 or index>=self.size:
      print(index,'Error: index out of range')
      return 
       
    if index==0:
      self.removeFirst()
    elif index==self.size-1:
      self.removeLast()
    else:
      #we must to reach the node before the node at the index position
      i=0
      previous=self.head
      while i<index-1:
        previous=previous.next
        i=i+1
      
      #previous is the node at index -1 position
      
      previous.next = previous.next.next
      self.size=self.size-1

class BinaryNode:

    def __init__(self, elem: object, node_left: 'BinaryNode' = None, node_right: 'BinaryNode' = None) -> None:
        self.elem = elem
        self.left = node_left
        self.right = node_right

    def __str__(self):
        return str(self.elem)

class BinaryTree:
    def __init__(self) -> None:
        """creates an empty binary tree"""
        self._root = None

    def draw(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n\n')

    def _draw(self, prefix: str, node: BinaryNode, is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)

    def insert(self, elem: object) -> None:
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        if node is None:
            return BinaryNode(elem)

        if node.elem == elem:
            print('Error: elem already exist ', elem)
            return node

        if elem < node.elem:
            node.left = self._insert(node.left, elem)
        else:
            # elem>node.elem
            node.right = self._insert(node.right, elem)
        return node
    
    def level_order(self) -> None:
        """prints the level order of the tree. O(n)"""
        if self._root is None:
            print('tree is empty')
        else:
            print("Level order: ", end= ' ')  # avoid the new line

            # we can use SList with tail and head
            list_nodes = SList()
            list_nodes.add_last(self._root)
            while len(list_nodes) > 0:  # loop will be executed the size of tree: n
                current = list_nodes.remove_first()
                print(current.elem, end=' ')
                if current.left is not None:
                    list_nodes.add_last(current.left)  # O(1)
                if current.right is not None:
                    list_nodes.add_last(current.right)  # O(1)

            print()

    def level_order_list(self) -> list:
        """prints the level order of the tree. O(n)"""
        result = []
        if self._root is not None:
            # we can use SList with tail and head
            list_nodes = SList()
            list_nodes.add_last(self._root)

            while len(list_nodes) > 0:  # loop will be executed the size of tree: n
                current = list_nodes.remove_first() # O(1)
                result.append(current.elem)
                if current.left is not None:
                    list_nodes.add_last(current.left)  # O(1)
                if current.right is not None:
                    list_nodes.add_last(current.right)  # O(1)

        return result

    def depth(self, node):
        """ returns the depth of the node; this is the length from
        the root to the node"""
        depth_level = None

        if self._root is None:
            print('Error: the tree is empty')
        else:
            # we can use SList with tail and head
            depth_level = 0

            list_nodes = SList()
            list_nodes.add_last(self._root)

            while len(list_nodes) > 0:  # loop will be executed the size of tree: n
                current = list_nodes.remove_first() # O(1)
                if current == node:
                    return depth_level
                if current.left is not None and node.elem < current.elem:
                    list_nodes.add_last(current.left)  # O(1)
                if current.right is not None and node.elem > current.elem:
                    list_nodes.add_last(current.right)  # O(1)
                depth_level += 1

        print('Not found ', node.elem)
        return None
    
    def size(self) -> int:
        """Returns the number of nodes"""
        return self._size(self._root)

    def _size(self, node: BinaryNode) -> int:
        """return the size of the subtree from node"""
        if node is None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)

    def height(self) -> int:
        """Returns the height of the tree"""
        return self._height(self._root)

    def _height(self, node: BinaryNode) -> int:
        """return the height of node"""
        if node is None:
            return -1
        else:
            return 1 + max(self._height(node.left), self._height(node.right))
    
    def sumaArray(a: list) -> int:
        """devuelve la suma de los elementos del array a"""
        if a is None or len(a)==0:
            return 0
        #base case
        if len(a)==1:
            return a[0]
        #recursive case
        #dividir
        m=len(a)//2
        part1=a[0:m]
        part2=a[m:]
        #vencer
        sum1= sumaArray(part1)
        sum2= sumaArray(part2)
        #  combinar
        return sum1+sum2
    
    
    
    def right_sum(self) -> int:
        # Define a variable to track current level
        nodos = []
        if self._size != 0:
            node = self._root
            nodos.append(node)
            nodeaux1 = self._root
            nodeaux2 = self._root
        if self._size != 1 and self._size != 0:
            node1 = self._root
            node2 = self._root
            if node1.right:
                node1 = node1.right
                nodos.append(node1.elem)
            else:
                node1 = nodeaux1
            if node2.left:
                node2 = node2.left
            #empieza el bucle
            while node1 != nodeaux1 and node2 != nodeaux2:
                if node1.right:
                    node1 = node1.right
                    nodos.append(node1.elem)
                else:
                    if node1.left:
                        node1 = node1.left
                        nodos.append(node1.elem)
                    else:
                        node1 = nodeaux1
                
                if node2.right:
                    node2 = node2.right
                    if self.depth(node1) < self.depth(node2) or node1 == nodeaux1:
                        nodos.append(node2.elem)
                if node2.left:
                    if node1 == nodeaux1:
                        node2 = node2.left
                        nodos.append(node2.elem)
                else:
                    node2 = nodeaux2
            
        return self.sumaArray(nodos)
