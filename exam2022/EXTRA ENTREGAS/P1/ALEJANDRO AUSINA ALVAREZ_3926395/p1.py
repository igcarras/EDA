#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Alejandro Ausina
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
        contador_aux = 0
        Head = self._head
        Tail = self._tail       
        anterior = None
        siguiente = None
        while Head != start:
            anterior = Head
            Head = Head.next
        while Tail != end:
            siguiente = Tail
            Tail = Tail.prev
        if start == self._head:
            self._head = siguiente
        if end == self._tail and anterior != None:
            anterior.next = None
            self._tail = anterior

        elif start == self._head and end == self._tail:
            return []
        else:
            if anterior:
                anterior.next = siguiente
                siguiente.prev = anterior
        self._size -= count
            

    def remove_section_by_sum(self, k):
        """removes the consecutive nodes of the list
        whose elements sum k"""
        if self._size == 0:
            return None
        elif k < 0:
            return self
        suma = 0
        head = self._head
        siguiente = head.next
        suma += head.elem
        contador = 1
        while suma != k:
            if siguiente.next == None:
                return None
            if suma < k:
                suma += siguiente.elem
                contador += 1   
                siguiente = siguiente.next
            if suma > k:
                suma -= head.elem
                head = head.next
                contador -= 1
        return self.remove_sublist(head, siguiente, contador)
