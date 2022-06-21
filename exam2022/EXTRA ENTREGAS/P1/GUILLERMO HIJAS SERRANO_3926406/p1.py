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
        node=self._head
        index=0
        while node:
            if node.elem==e:
                return index
            node=node.next
            index += 1
        return -1

    def remove_sublist(self, start: DNode, end: DNode, count:int) -> None:
        """remove the sublist from node start to node end, both included
        count is the number of nodes to be removed.
        It is not necessary to check it"""
        aux1 = self.index(start.elem)
        aux2 = self.index(end.elem)
        if start == self._head and end == self._tail:
            return None
        start = self._head
        end = self._head
        for i in range(aux1):
            start = start.next
        for i in range(aux2):
            end = end.next
        if start == self._head:
            self._head = end
            end.prev = None 
            self._head.next = end.next
        if end == self._tail:
            self._tail = start
            start.next = None
            self._tail.prev = start.prev
        start.next = end
        end.prev = start
        self._size -= count
        return self

    def remove_section_by_sum(self, k):
        """removes the consecutive nodes of the list
        whose elements sum k"""
        if self == None:
            return None
        if k <= 0:
            print('k tiene que ser mayor que 0')
            return self
        encontrado = False
        nodo_inicio = self._head
        while not encontrado or nodo_inicio == None:
            suma = 0
            count = 0          
            nodoaux = nodo_inicio
            while nodoaux != None:
                if suma != k:
                    suma += nodoaux.elem
                    nodoaux = nodoaux.next
                    print('impreso')
                    count += 1
                    print(k,suma)
                else:
                    return self.remove_sublist(nodo_inicio, nodoaux, count)
                    encontrado = True
                    print('ha llegado al else')
            nodo_inicio = nodo_inicio.next
                
            

