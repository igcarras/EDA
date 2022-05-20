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
    
    # Exam starts here...
    
    def right_sum(self) -> int:
        # Define a variable to track current level
        self._currentLevel = 0
        return self._right_sum_recursive(self._root, self._currentLevel + 1)
    
    def _right_sum_recursive(self, node, level):        
        if not node:
            return 0
                
        sum = 0
        # If we detect a level change
        if self._currentLevel < level:
            # We accumulate item value to the sum
            sum += node.elem
            # We update current level to keep going
            self._currentLevel = level

        # Recursion: right first since we want to sum last items of each level only
        sum += self._right_sum_recursive(node.right, level + 1)
        sum += self._right_sum_recursive(node.left, level + 1)
        return sum

