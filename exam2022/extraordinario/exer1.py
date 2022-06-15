#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class DNode:
    def __init__(self,e, next=None, prev=None):
        self.elem=e
        self.next=next
        self.prev=prev

class MyDList:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
  
    def append(self,e):
        '''adds e at the end of the list'''
        newNode=DNode(e)
        if self._head==None:
            self._head=newNode
        else:
            newNode.prev=self._tail
            self._tail.next=newNode
           
        self._tail=newNode
        self._size+=1
        
    def __len__(self):
        return self._size
    
    def __str__(self):
        """Returns a string with the elements of the list"""
        ###This functions returns the same format used 
        ###by the Python lists, i.e, [], ['i'], ['a', 'b', 'c', 'd']
        ###[1], [3, 4, 5]
        nodeIt=self._head
        result='['
        while nodeIt:
            result+= str(nodeIt.elem)+ ", "
            nodeIt=nodeIt.next
        
        if len(result)>1:
            result=result[:-2]

        result+=']'
        return result

    #Exam starts here
    def remove_sublist(self, start, end, count):
     ...

    def remove_section_by_sum(self, k):        
     ...

