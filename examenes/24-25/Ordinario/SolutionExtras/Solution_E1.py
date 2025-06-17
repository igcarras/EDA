# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:16:50 2024

@author: user
"""
from bst import BinarySearchTree

class MyBST(BinarySearchTree):
    
    def getDist(self, a, b):
        node = self._root
        return self._getDist(node, a, b)
    
    def _getDistance(self, node, a, b):
        # Base case: If the node is None
        if node is None:
            return None
    
        # If both a and b are smaller than node's key, then LCA (Lowest Common Ancestor) lies in the left
        if a < node.elem and b < node.elem:
            return self._getDist(node.left, a, b)
        # If both a and b are greater than node's key, then LCA (Lowest Common Ancestor) lies in the right
        if a > node.elem and b > node.elem:
            return self._getDist(node.right, a, b)
    
        # If one key is on the left and the other is on the right or one of them matches the node's key
        if a <= node.elem <= b or b <= node.elem <= a:
            return self.distance_from_lca(node, a) + self.distance_from_lca(node, b)
    

    def distance_from_lca(self, node, key):
        if node.elem == key:
            return 0
        elif key < node.elem:
            return 1 + self.distance_from_lca(node.left, key)
        else:
            return 1 + self.distance_from_lca(node.right, key)
    
    # iterative function to distance_from_lca
    def distance_from_lca(node, key):
        distance = 0
        while node.elem != key:
            if key < node.elem:
                node = node.left
            else:
                node = node.right
            distance += 1
        return distance




if __name__ == "__main__":

    bst = BinarySearchTree()

    bst.insert(8)
    bst.insert(4)
    bst.insert(2)
    bst.insert(6)
    bst.insert(7)
    bst.insert(5)
    bst.insert(3)
    bst.insert(1)
    bst.insert(12)
    bst.insert(10)
    bst.insert(14)
    bst.insert(9)
    bst.insert(11)
    bst.insert(13)
    bst.insert(15)
    bst.draw()
    a = 1
    b = 15
    dist = bst.getDist(a, b)
    if dist is not None:
        print(f"Distance between {a} and {b} is: {dist}")
