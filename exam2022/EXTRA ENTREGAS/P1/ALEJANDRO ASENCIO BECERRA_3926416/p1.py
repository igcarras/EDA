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
            
        node = start
        node2 = end
        node.next = node2.prev
        start.prev = None
        start.next = None
        end.prev = None
        end.next = None
        

    def remove_section_by_sum(self, k: int):
        """removes the consecutive nodes of the list
        whose elements sum k"""
        
        if self._size != 0:
        
            node = self._head
            node2 = node.next
            node3 = node2.next
            node4 = node3.next
            counter = 0
            start = DNode(0)
            end = DNode(0)
                
        
            while not (node.elem + node2.elem) == k or counter == len(self._size):
                if node.elem == k:
                    node = start
                    node = end
                if node2.elem == k:
                    node2 = start
                    node2 = end
                node = node.next
                node2 = node2.next
                counter+=1
            
            start = node
            end = node2
            counter = 0
            while not (node.elem + node2.elem + node3.elem) == k or counter == len(self._size):
                if node.elem == k:
                    node = start
                    node = end
                if node2.elem == k:
                    node2 = start
                    node2 = end
                if node3.elem == k:
                    node3 = start
                    node3 = end
                    
                node = node.next
                node2 = node2.next
                node3 = node3.next
                counter+=1
    
            start = node
            end = node3
            counter = 0
            while not (node.elem + node2.elem + node3.elem + node4.elem) == k or counter == len(self._size):
                if node.elem == k:
                    node = start
                    node = end
                if node2.elem == k:
                    node2 = start
                    node2 = end
                if node3.elem == k:
                    node3 = start
                    node3 = end
                if node4.elem == k:
                    node4 = start
                    node4 = end
                    
                node = node.next
                node2 = node2.next
                node3 = node3.next
                node4 = node4.next
                counter+=1
            start = node
            end = node4
            
            counter = 2
            while start != end:
                start = start.next
                counter+=1
        
            self.remove_sublist(start, end, counter)
        
        
