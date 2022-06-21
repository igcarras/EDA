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

    def remove_sublist(self, start: DNode, end: DNode, count:int) -> None:
        """remove the sublist from node start to node end, both included
        count is the number of nodes to be removed.
        It is not necessary to check it"""
        aux1 = self._head
        aux2 = None
        
        if count == -1:
            self._head = None
            self._tail = None
            self._size = 0
        
        if count == -2:
            return MyDList, print("Error")
        
        while aux1 is not start:
            aux2 = aux1
            aux1 = aux1.next
            aux1.prev = aux2
        for i in range(count - 1):
            if aux1.next:
                aux1 = aux1.next
            
            
        if aux1.next:
            aux1 = aux1.next
            aux1.prev = aux2
            if aux2 == None:
                aux1 = self._head 
            
        else:
            if aux2:
                aux2.next = None
                aux2 = self._tail
        
        if self._size != 0:
            self._size -= count
                    
            
    def remove_section_by_sum(self, k):
        """removes the consecutive nodes of the list
        whose elements sum k"""
        aux = self._head
        start = aux
        end = aux
        p = None
        sum = 0
        count = 1
        found = False
        if k < 0:
            return self.remove_sublist(start, end, -2)
        if k > self._size:
            return self.remove_sublist(start, end, -1)
        while not found:
            sum += aux.elem
            if sum > k:
                sum = 0
                count = 1
                start = aux.next
            elif sum == k:
                found = True
            
            if aux.next is None:
                sum = -1
                found = True
            else:
                p, end = aux
                aux = aux.next
                aux.prev = p
                count += 1
                
        return self.remove_sublist(start, end, count)
                
        
                
                
        
                
        
        
        
        
        
        
        

