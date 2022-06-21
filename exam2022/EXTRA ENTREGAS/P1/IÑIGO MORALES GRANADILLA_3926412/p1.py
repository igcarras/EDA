#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Iñigo Morales"""
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
        if start == self._head and end == self._tail:
            self._size -= count
            return []
        if start == self._head:
            end.next.prev = None
            self._size -= count
            return self
        if end == self._tail:
            start.prev.next == None
            self._size -= count
            return self
        
        start.prev.next = end.next
        end.next.prev = start.prev
        self._size -= count
        return self
    
    def remove_section_by_sum(self, k):
        """removes the consecutive nodes of the list
        whose elements sum k"""
        nodeIt = self._head
        node2 = self._head.next
        cuenta = 0
        pasos = 2
        

        while nodeIt and node2:
            cuenta += nodeIt.elem
            if cuenta == k:
                self.remove_sublist(nodeIt, nodeIt, 1)
            else:
                cuenta += node2.elem
                if cuenta == k:
                    self.remove_sublist(nodeIt, node2, pasos)
                else:
                    while cuenta < k and node2.next:
                        node2 = node2.next
                        pasos += 1
                        cuenta += node2.elem
            cuenta = 0
            nodeIt = nodeIt.next
            node2 = nodeIt.next
            
            
        
            
    
        

