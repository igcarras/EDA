#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
    
    def isEmpty(self):
        """Checks if the list is empty"""
        #return self.head == None   
        return len(self)==0
    
    def removeFirst(self):
        """Returns and remove the first element of the list"""
        result=None
        if self.isEmpty():
            print("Error: list is empty")
        else:
            result=self._head.elem 
            
            self._head= self._head.next 
            if self._head==None:
                self._tail=None
            else:
                self._head.prev = None

            self._size-=1

        return result
    
    def removeLast(self):
        """Returns and remove the last element of the list"""
        result=None

        if self.isEmpty():
            print("Error: list is empty")
        else:
            result=self._tail.elem                       
            self._tail= self._tail.prev                 
            if self._tail==None:
                self._head=None
            else:
                self._tail.next = None

            self._size-=1

        return result
    
    def remove_sublist(self, start: DNode, end: DNode, count:int) -> None:
        """remove the sublist from node start to node end, both included
        count is the number of nodes to be removed.
        It is not necessary to check it"""
        if count <= 0 or count > len(self):
            return self
        
        if start == self._head:
            for i in range(count):
                self.removeFirst()
            return self
        
        if end == self._tail:
            for i in range(count):
                self.removeLast()
            return self
        
        else:
            start.next = end.next
            end.prev = start.prev
            self._size -= count
            return self
     
    def remove_section_by_sum(self, k):
        """removes the consecutive nodes of the list
        whose elements sum k"""
        if len(self) == 0 or k < 0:
            return self
        
        previous = self._head
        while previous != None:
            current = previous
            result = 0
            while current != None:
                result += current.elem
                current = current.next
                if result == k:
                    self.remove_sublist(self._head, current, len(self))
                    return self
            previous = previous.next
        
        return self

            
        
            

