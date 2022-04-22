# -*- coding: utf-8 -*-

from bintree import BinaryNode
from bintree import BinaryTree


class MyBinarySearchTree(BinaryTree):


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

  # Removes all nodes having value inside the given range
  # returns a sorted list in descending order
    def removeInsideRange(self, min: int, max: int) -> []:
        # update the root with the new subtree after remove elem
        removelist = []
        self._removeInsideRange(self._root, min, max, removelist)
        return removelist

    # Removes all nodes having value inside the given range
    # returns a sorted list in descending order
    def _removeInsideRange(self, node: BinaryNode, min: int, max: int, removelist: []) -> None:
        # Base Case
        if node is None:
            return

        # check is node is not leaf
        if node.left or node.right:
            node.right = self._removeInsideRange(node.right, min, max, removelist)
            node.left = self._removeInsideRange(node.left, min, max,  removelist)

        else:
            if (node.left is None) and (node.right is None) and (min <= node.elem <= max):
                # node is a leave
                # append node in list
                # print("leaf node for removing:", node.elem)
                removelist.append(node.elem)
                return None

        # if node is not leaf, return node and continue recursion
        return node


if __name__ == "__main__":
    aux = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux.insert(x)
        # aux.draw()
    print("Original Tree")
    aux.draw()

    print("Remove leaf nodes in range: 1, 120")
    print("Nodos eliminados", aux.removeInsideRange(1,120))
    aux.draw()

    print("Remove leaf nodes in range: 15, 20")
    print("Nodos eliminados", aux.removeInsideRange(15,20))
    aux.draw()

    print("Remove leaf nodes in range: 0, 0")
    print("Nodos eliminados", aux.removeInsideRange(0,0))
    aux.draw()

