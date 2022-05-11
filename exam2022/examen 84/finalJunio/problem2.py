# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 14:38:54 2022

@author: halju
"""

from typing import Tuple


class MyNode:
    def __init__(self, elem: int, node_left: 'MyNode' = None, node_right: 'MyNode' = None) -> None:
        self.elem = elem
        self.left = node_left
        self.right = node_right

class MyBST:
    def __init__(self) -> None:
        """creates an empty binary tree
        I only has an attribute: _root"""
        self._root = None

    def insert(self, elem: int) -> None:
        if self._root is None:
            self._root = MyNode(elem)  # if tree is empty, new node will be the root
            return  # we can leave!!!

        node = self._root  # to search the place
        not_exist = True
        while not_exist and node:
            if elem < node.elem:
                if node.left is None:  # this is the place to insert it
                    node.left = MyNode(elem)
                    not_exist = False
                else:
                    node = node.left
            elif elem > node.elem:
                if node.right is None:  # this is the place to insert it
                    node.right = MyNode(elem)
                    not_exist = False
                else:
                    node = node.right
            elif elem == node.elem:
                print('duplicate elements not allowed!!', elem, node.elem)
                not_exist = False

    def draw(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n\n')

    def _draw(self, prefix: str, node: MyNode, is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)

    def inorder_lst(self):
        result = []
        self._inorder_lst(self._root, result)
        return result

    def _inorder_lst(self, node: MyNode, elems: list) -> None:
        if node:
            self._inorder_lst(node.left, elems)
            elems.append(node.elem)
            self._inorder_lst(node.right, elems)


    def getCount(self, low, high):
        """counts the number of nodes that lie in the given range"""

        return self._getCount(self._root, low, high)
        
    def _getCount(self, node, low, high):
         
        # Base case
        if node == None:
            return 0
             
        # Special Optional case for improving
        # efficiency
        if node.elem == high and node.elem == low:
            return 1
     
        # If current node is in range, then
        # include it in count and recur for
        # left and right children of it
        if node.elem <= high and node.elem >= low:
            return (1 + self._getCount(node.left, low, high) +
                        self._getCount(node.right, low, high))
     
        # If current node is smaller than low,
        # then recur for right child
        elif node.elem < low:
            return self._getCount(node.right, low, high)
     
        # Else recur for left child
        elif node.elem > high:
            return self._getCount(node.left, low, high)    


if __name__ == "__main__":
    tree = MyBST()
    for x in [46, 11, 81, 51, 56, 94, 5, 20]:
        tree.insert(x)

    tree.draw()


    low, high = 5, 0
    print('getCount({}, {}) = {}'.format(low, high, tree.getCount(low, high)))

    low, high = 1, 4
    print('getCount({}, {}) = {}'.format(low, high, tree.getCount(low, high)))

    low, high = 95, 100
    print('getCount({}, {}) = {}'.format(low, high, tree.getCount(low, high)))

    low, high = 21, 45
    print('getCount({}, {}) = {}'.format(low, high, tree.getCount(low, high)))

    low, high = 57, 80
    print('getCount({}, {}) = {}'.format(low, high, tree.getCount(low, high)))
    
    low, high = 4, 100
    print('getCount({}, {}) = {}'.format(low, high, tree.getCount(low, high)))

    low, high = 10, 81
    print('getCount({}, {}) = {}'.format(low, high, tree.getCount(low, high)))
    
    low, high = 12, 100
    print('getCount({}, {}) = {}'.format(low, high, tree.getCount(low, high)))
    
    low, high = 4, 50
    print('getCount({}, {}) = {}'.format(low, high, tree.getCount(low, high)))
    
    low, high = 50, 90
    print('getCount({}, {}) = {}'.format(low, high, tree.getCount(low, high)))

    low, high = 5, 10
    print('getCount({}, {}) = {}'.format(low, high, tree.getCount(low, high)))

    
    
    