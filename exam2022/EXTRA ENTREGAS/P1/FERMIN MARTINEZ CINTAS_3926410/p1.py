#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Fermín Martínez Cintas


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
        aux = self._head
        if start.prev != None:
            previo = start.prev
            start.prev = None
        if end.next != None:
            sig = end.next
            end.next = None
        
        previo.next = sig
        sig.prev = previo
        
        if start.prev == None and end.next == None:
            self._head = None
            self._tail = None
        
        if start.prev == None and end.next != None:
            while aux !=end.next:
                aux = aux.next
            aux.prev == None
            self._tail = aux
        
        if start.prev != None and end.next  == None:
            while aux !=start.prev:
                aux = aux.next
            aux.next == None
            self._tail = aux
        
        self._size -= count

    def remove_section_by_sum(self, k):
        """removes the consecutive nodes of the list
        whose elements sum k"""
        if len(self) == 0 or k <= 0:
            pass
        else:
            a = 0
            cuenta = 1
            nodoi = self._head
            nodof= self._head
            a += nodof.elem
            while a < k:
                if nodof.next != None:
                    nodof = nodof.next
                    a += nodof.elem
                    cuenta += 1
            
            if a == k:
                self.remove_sublist(nodoi, nodof, cuenta)
            
            while a > k:
                a -= nodoi.elem
                if nodoi.next != None:
                    nodoi = nodoi.next
                    cuenta -= 1

