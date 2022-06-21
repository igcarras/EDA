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
    
    def index(self,e):
        """returns the first position of e into the list.
        If e does not exist in the list, 
        then the function will return -1"""
        nodeIt=self._head
        index=0
        while nodeIt:
            if nodeIt.elem==e:
                return index
            nodeIt=nodeIt.next
            index+=1
            
        #print(e,' does not exist!!!')
        return -1 

    def remove_sublist(self, start: DNode, end: DNode, count:int) -> None:
        """remove the sublist from node start to node end, both included
        count is the number of nodes to be removed.
        It is not necessary to check it"""
        
        elemt = self._head
        ultimo = self._tail
    
        if count == len(self):
           self = None
          
        elif start.elem == elemt.elem:
            for n in range(count):
                elemt = elemt.next 
               
            self._head = elemt 
            elemt.prev = None
            self._size -= count
        
        elif end.elem == ultimo.elem:
            
            for n in range(len(self)-count - 1):
                elemt = elemt.next 
               
            self._tail = elemt 
            elemt.next = None
            self._size -= count
            
        elif start.elem != elemt.elem and  end.elem != ultimo.elem:
            pos = self.index(start.elem)
            for n in range(pos-1)
                elemt = elemt.next
                
            incio = elemt
           

            for x in range(count):
                elemt = elemt.next 
         
            final = elemt
            inicio.next = final
            final.prev = inicio
            self._size -= count 
                        

    def remove_section_by_sum(self, k):
        """removes the consecutive nodes of the list
        whose elements sum k"""
        
        if k < 0:
            return self and print("Error")
        if len(self) == 0:
            return self

























