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
        prev=None
        siguiente=None
        nodeIt=self._head
        while nodeIt:
            if nodeIt==start:
                prev=nodeIt.prev
            if nodeIt==end:
                siguiente=nodeIt.next
            nodeIt=nodeIt.next
        if prev and siguiente:
            prev.next=siguiente
            siguiente.prev=prev
        elif prev and not siguiente:
            prev.next=self._tail
            self._tail.prev=prev
        elif not prev and siguiente:  
            self._head.next=siguiente
            siguiente.prev=self._head
        
    def remove_section_by_sum(self, k):
        """removes the consecutive nodes of the list
        whose elements sum k"""
        nodeIt=self._head
        cont=0
        sublist=[]
        suma=k
        while nodeIt:
            if nodeIt.elem==suma:
                self.remove_sublist(nodeIt, nodeIt, 1)
                
            elif nodeIt.elem>suma:
                suma=k
                cont=0
                sublist.clear()
            
            elif nodeIt.elem<suma:
                suma-=nodeIt.elem
                sublist.append(nodeIt)
                cont+=1
            elif sum==0:
                break
            nodeIt=nodeIt.next
        if len(sublist)==0:
            return self
        
        self.remove_sublist(sublist[0],sublist[-1],cont)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

