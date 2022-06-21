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
        if len(self)==0: #No hay lista
            return []
        if start == None or end==None:
            return []
        nodeIt=self._head
        final=self._tail
        while nodeIt.elem != start:
            nodeIt=nodeIt.next
        while final.elem != end:
            final=final.prev
        for i in range(count):
            nodeIt.prev.next=final.next
            final.prev=nodeIt.prev
            return self
        
        
            

    def remove_section_by_sum(self, k):
        """removes the consecutive nodes of the list
        whose elements sum k"""
        if k == 0: #Si la k es 0
            return None
        if k<0: #Si k negativa
            return self and print("error")
        start= self._head
        aux=self._head
        end=self._tail
        suma=0
        count=0
        primerelemento=0
        for i in range(len(self)):
            count=1
            if start.elem== k:
                self.remove_sublist(start, start, count)
            start=start.next

       
        while start: #debería ser while aux porque es el que muevo pero entra en bucle infinito que no sé como arreglar
            for i in range(primerelemento):
                #Situa el start en la posición desde la que intenta la suma
                start=start.next #start ya se queda en esa posición y ya solo se va a mover aux
                aux=aux.next
            while suma != k and aux.elem <(k-suma): #Mientras suma diferente a k y el siguiente elemento siguiente sea menor a k-suma
                suma += aux.elem
                aux = aux.next
                count+=1
                if aux.elem <(k-suma): #si es igual, se prueba desde el siguiente elemento como start
                    primerelemento += 1
                    break #Sale del while
            self.remove_sublist(start, aux.next, count)
        
        
        return [] #No ha encontrado lista posible

        
        ''' while suma != k:
            suma+= aux.elem
            aux=aux.next
            count+=1
            end=aux.next
        self.remove_sublist(start, end, count)
#Mientras haya elementos, comenzando por el primero, va a probar sumas'''





























