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
        if start.prev:
            start.prev.next = end.next
        if end.next:
            end.next.prev = start.prev

        # Update head / tail references if needed
        if start == self._head:
            self._head = end.next
        if end == self._tail:
            self._tail = start.prev

        # Update size of the list
        self._size -= count

    def remove_section_by_sum(self, k):
        """removes the consecutive nodes of the list
        whose elements sum k"""
        if len(self) == 0:
            return
        if k < 0:
            return

        current = self._head

        # A couple of extra references to handle the count and starting position
        start = current
        count = 0
        nodes_count = 1

        # Iterate through the list from the beginning
        while current:
            # Add the current value first
            count += current.elem

            # Check count
            if count == k: 
                # If matches, remove sublist [start, current] and finish
                self.remove_sublist(start, current, nodes_count)
                return
            elif count > k:
                # Reduce the window moving 'start' reference and remove its value from the counter. 
                # This could be done N times but considering this into the tests (in case anyone does it without a loop)
                while count > k and start != current:                    
                    count -= start.elem
                    start = start.next
                    nodes_count -= 1

                if count == k:
                    self.remove_sublist(start, current, nodes_count)
                    return

            # In any case we must move current reference to keep iterating
            current = current.next
            nodes_count += 1

