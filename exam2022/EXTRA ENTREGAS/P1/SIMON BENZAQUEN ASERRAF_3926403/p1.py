#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Simon Benzaquen, grupo 801
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
        if start == None or end == None:
            return None
        if start.prev != None and end.next == None:
            self._tail = start.prev
        if start.prev == None and end.next != None:
            self._head = end.next 
        if start.prev == None and end.next == None:
            return None
        if start.prev != None and end.next != None:
            start.prev.next = end.next
        
            
        
    def remove_section_by_sum(self, k):
        """removes the consecutive nodes of the list
        whose elements sum k"""
        if len(self) == 0 or self._head == None:
            return None
        
        aux = self._head
        aux_f = self._tail
        
        suma = 0
        
        if self._head.elem == k:
            return self.remove_sublist(self._head, self._head, 1)
            
        if self._tail.elem == k:
            return self.remove_sublist(self._tail, self._tail, 1)
            
        while aux:
            if aux.elem + aux_f.elem == k:
                 self.remove_sublist(aux, aux, 1)
                 self.remove_sublist(aux_f, aux_f, 1)
                 return self
            
            aux = aux.next

        return self.remove_sublist(None, None, 0)
            
            
            
            
            
            
            
            
            