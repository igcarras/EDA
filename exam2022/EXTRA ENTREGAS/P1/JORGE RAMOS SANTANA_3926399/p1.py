#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Jorge Ramos Santana



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
        left=self._head
        right=self._head
        while left:
            if left.elem==start:
                break
            else:
                left=left.next
        while right:
            if right.elem==end:
                break
            else:
                right=right.next
        if left==None or right==None:
            return 
        #print(self._head.elem)
        if left.elem==self._head.elem:
            self._head=right.next
            #print(self._head.elem)
            self._size-=count
            print("AAAAAA")
            return
        if right.elem==self._tail.elem:
            left.next=None
            self._tail=left.prev
            self._size-=count
            print("BBBBBB")
            return
            
        else:
            print("CCCCC")
            left.prev.next=right.next
            right.next.prev=left.prev
            self._size-=count

    def remove_section_by_sum(self, k):
        """removes the consecutive nodes of the list
        whose elements sum k"""
        node=self._head
        node2=self._head
        total=0
        count=0
        while node:
            while node2:
                total=total+node2.elem
                #print(node2.elem)
                print("total",total)
                count+=1
                if total==k:
                    self.remove_sublist(node.elem,node2.elem,count)
                    return  
                else:
                    node2=node2.next

            node2=node
            total=0
            count=0
            node=node.next

                    



lista=MyDList()
lista2=[3,2,1,4]
for i in lista2:
    lista.append(i)

print(lista)

lista.remove_section_by_sum(4)
print(lista)
