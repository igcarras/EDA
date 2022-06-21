#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Simon Benzaquen, grupo 801
class BinaryNode:

    def __init__(self, elem: object, node_left: 'BinaryNode' = None, node_right: 'BinaryNode' = None) -> None:
        self.elem = elem
        self.left = node_left
        self.right = node_right
        self.next = None

    def __str__(self):
        return str(self.elem)

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
    newNode=BinaryNode(e)
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
    newNode=BinaryNode(e)
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
      result=result+','+str(temp.elem)
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
    first=self.head.elem
    #updates head to point to the new head (the next node)
    self.head=self.head.next
    #if the list only has one node, tail must be None
    if self.isEmpty():
      self.tail=None
    self.size -= 1
    
    return first
        
        
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

    def right_sum(self) -> int:
        # Define a variable to track current level
        if self._root is None:
            return 0
        # we can use SList with tail and head
        suma = 0
        list_nodes = SList()
        list_nodes.addLast(self._root)
        
        while len(list_nodes) > 0:  # loop will be executed the size of tree: n
            current = list_nodes.removeFirst()
            print(current)
            if current.left is not None and current.right is None:
                list_nodes.addLast(current.left)# O(1)
                suma += current.elem
                
            if current.right is not None and current.left is None:
                list_nodes.addLast(current.right)# O(1)
                suma += current.elem
                
            if current.left is not None and current.right is not None:
                suma += current.elem
                
            if current.left is None and current.right is None:
                suma += current.elem
            print(suma)

        return suma 
  