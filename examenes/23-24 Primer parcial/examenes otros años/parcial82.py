#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class SNode:
    def __init__(self, e, next_node= None):
        self.elem = e
        self.next = next_node

class MyList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def append(self, e):
        """ adds e at the end of the list"""
        new_node = SNode(e)
        if self._head is None:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def __len__(self):
        return self._size

    def __str__(self):
        """Returns a string with the elements of the list"""
        node = self._head
        result = '['
        while node:
            result += str(node.elem)+ ", "
            node = node.next

        if len(result) > 1:
            result = result[:-2]

        result += ']'
        return result

    def removeMultiplesOf(self, e):
        """searches the first occurrence of e at the list, and remove
         all multiples for e that happen after the first occurrence"""
        if len(self) > 1:
            prev = self._head
            node = prev.next
            delete = False
            if prev.elem == e:
                delete = True

            while node:
                if not delete:
                    if node.elem == e:
                        delete = True
                    prev = node
                    node = node.next
                else:

                    if node.elem%e == 0:
                        # we have to remove this node
                        prev.next = node.next
                        if node.next is None:
                            self._tail = prev
                        self._size -= 1
                    else:
                        prev = node
                    node = node.next


if __name__=='__main__':
    l=MyList()
    for i in [2, 6, 3, 2, 6, 6, 4, 7, 9, 2, 2, 1, 1, 3, 3, 3, 2, 4, 9]:
        l.append(i)

    print('before removeMultiplesOf(2)', str(l))
    l.removeMultiplesOf(2)

    print('after removeMultiplesOf(2)', str(l))
