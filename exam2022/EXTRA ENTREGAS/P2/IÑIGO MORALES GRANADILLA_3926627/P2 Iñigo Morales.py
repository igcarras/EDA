#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Iñigo Morales"""
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
        node = self._root
        if node == None:
            return 0
        elif node.left == None and node.right == None:
            return node.elem
        elif node.right == None:
            return node.elem + self._right_sum(node.left)
        return node.elem + self._right_sum(node.right)
        
    def _right_sum(self, node):
        if node.left == None and node.right == None:
            return node.elem
        elif node.right == None:
            return node.elem + self._right_sum(node.left)
        return node.elem + self._right_sum(node.right)
        
