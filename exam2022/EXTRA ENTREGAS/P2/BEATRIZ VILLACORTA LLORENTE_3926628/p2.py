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

    @property
    def right_sum(self) -> int:
        suma = 0
        if self._root == None:
            return suma
        # Define a variable to track current level
        self._right_sum(self._root, suma)

    def _right_sum(self, node, suma):
        #devuelve la suma del nodo que esté más a la derecha en cada nivel
        if node == None:
            return suma
        if self.grado(node) == 0:
            return suma
        while node:
            # sumo todos los nodos de la derecha, ya que son los que más a la derecha están
            self._right_sum(node.right, suma)
            suma += node.elem

            if self.grado(node) == 1 and node.right == None:
                suma += node.elem
                self._right_sum(node.right, suma)

            if self.grado(node) == 2 :
                suma += node.elem
                self._right_sum(node.right, suma)

            self._right_sum(self, node.left, suma)
        return suma





    def grado(self, node):
        #calcula el número de hijos de un nodo
        grado = 0
        if node.left != None:
            grado += 1

        if node.right != None:
            grado += 1

        return grado



    
