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

    def height(self) -> int:
        """Returns the height of the tree"""
        return self._height(self._root)

    def _height(self, node: BinaryNode) -> int:
        """return the height of node"""
        if node is None:
            return -1
        else:
            return 1 + max(self._height(node.left), self._height(node.right))

    def right_sum(self) -> int:
        # Define a variable to track current level
        if self._root == None:
            return 0
        
        if self._root.right == None and self._root.left == None:
            return self._root.elem
        
        if self._height(self._root.left) > self._height(self._root.right) and self._root.right != None:
            diferencia = self._height(self._root.left) - self._height(self._root.right)
            current = self._root.left
            for i in range(diferencia):
                current = max(current.left.elem, current.right.elem)
                
            return self._right_sum(self._root) + self._right_sum(max(current.left.elem, current.right.elem))
        
        else:
            return self._right_sum(self._root)
        
    def _right_sum(self, node: BinaryNode) -> int:
        if node == None:
            return 0
        else:
            return node.elem + max(self._right_sum(node.left), self._right_sum(node.right))
        
