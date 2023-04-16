#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Carmen Marrasan Monar, 100475114
class DNode:
    def __init__(self, e: int, next = None, prev=None) -> None:
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
        node1 = start
        node2 = end
        if node1 == self._head:
            self._head = node2.next
            if self._head == None:
                self._tail = None
            else:
                self._head.prev = None   
        else:        
            node1.prev.next = node2.next            
            if node2.next == None:
                self._tail = node1.prev
            else:
                node2.next.prev = node1.prev
        self._size -= count
        

    def remove_section_by_sum(self, k):
        """removes the consecutive nodes of the list
        whose elements sum k"""
        if k <0:
            print("Error")
            return
        if len(self) == 0:
            return None
        prev = self._head
        nodeIt = prev
        #nodeIt = nodeIt.next
        count = 0  
        while nodeIt:
            num = prev.elem
            aux=nodeIt.elem
            print(nodeIt.elem,prev.elem)
            while (num + aux) <=k:
                num += aux
                if num == k:
                    self.remove_sublist(prev, nodeIt, count)
                else:
                    nodeIt = nodeIt.next
                    count +=1
            prev = nodeIt
            nodeIt = nodeIt.next

                
            
    

