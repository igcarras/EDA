#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BinaryNode:

    def __init__(self, elem: object, node_left: 'BinaryNode' = None, node_right: 'BinaryNode' = None) -> None:
        self.elem = elem
        self.left = node_left
        self.right = node_right

    def __str__(self):
        return str(self.elem)

class BinaryTree:
    def __init__(self) -> None:
        """creates an empty binary tree"""
        self._root = None

    def draw(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n\n')

    def _draw(self, prefix: str, node: BinaryNode, is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)

    def insert(self, elem: object) -> None:
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        if node is None:
            return BinaryNode(elem)

        if node.elem == elem:
            print('Error: elem already exist ', elem)
            return node

        if elem < node.elem:
            node.left = self._insert(node.left, elem)
        else:
            # elem>node.elem
            node.right = self._insert(node.right, elem)
        return node

    def right_sum(self) -> int:
        # Define a variable to track current level

        return self._right_sum(self._root, 0)
    
        
    def _right_sum(self, node, suma) -> int:
        if self is None or node is None:
            return 0
        print("suma", suma)
        suma += node.elem
        print("suma", suma)

        contadorderecha=0
        contadorizquierda=0
        nodoD=node
        nodoI=node

        #Si no tiene subarboles, devolver la suma
        if node.left is None and node.right is None:
            return suma
        while nodoD.right:
            contadorderecha+=1
            nodoD=nodoD.right
            suma += nodoD.elem


        while nodoI.left:
            contadorizquierda+=1
            nodoI=nodoI.left
        #Si siempre hay derecha mientras haya izquierda, devolver suma derecha
        if contadorderecha >= contadorizquierda:
            return suma
        for i in range(contadorderecha):
            node=node.left
        #Si no, empezar por el que se ha quedado de la izquierda
        self._right_sum(node.left, suma)
        return suma        
#No me suma el último elemento en algunos casos

   
    
