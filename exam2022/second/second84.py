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

    # Removes all nodes having value outside the given range
    def removeOutsideRange(self, min: int, max: int) -> None:
        # update the root with the new subtree after remove elem
        notremovelist =[]
        self._removeOutsideRange(self._root, min, max, notremovelist)
        #print("Saved notes for not removing:", notremovelist)

    # Removes all nodes having value outside the given range
    def _removeOutsideRange(self, node: BinaryNode, min: int, max: int, notremovelist: []) -> None:
        # Base Case
        if node is None:
            return

        # check is node is not leaf
        # append to list for not removing
        if node.left or node.right:
            #print("append node for not removing", node.elem)
            notremovelist.append(node.elem)

        node.left = self._removeOutsideRange(node.left, min, max, notremovelist)
        node.right = self._removeOutsideRange(node.right, min, max, notremovelist)

        # if node.elem == elem
        # and node is out of range
        # then remove node (return None)
        if node.left is None and node.right is None and node.elem not in range(min, max):
            if node.elem not in notremovelist:
                #  node is a leave
                #print("leaf node for removing:", node.elem)
                return None

        #if node is not leaf, return node and continue recursion
        return node

    # Removes all nodes having value outside the given range
    def removeOutsideRange2(self, min: int, max: int) -> None:
        # update the root with the new subtree after remove elem
        self._removeOutsideRange2(self._root, min, max)


    # Removes all nodes having value outside the given range
    def _removeOutsideRange2(self, node: BinaryNode, min: int, max: int) -> None:
        # Base Case
        if node is None:
            return

        # check is node is not leaf
        if node.left or node.right:
            node.left = self._removeOutsideRange2(node.left, min, max)
            node.right = self._removeOutsideRange2(node.right, min, max)
        else:
            if node.left is None and node.right is None and node.elem not in range(min, max):
                #  node is a leave
                # print("leaf node for removing:", node.elem)
                return None

        # if node is not leaf, return node and continue recursion
        return node

    # Removes all nodes having value outside the given range
    # returns a sorted list in ascending order
    def removeOutsideRange3(self, min: int, max: int) -> []:
        # update the root with the new subtree after remove elem
        removelist = []
        self._removeOutsideRange3(self._root, min, max, removelist)
        return removelist

    # Removes all nodes having value outside the given range
    # returns a sorted list in ascending order
    def _removeOutsideRange3(self, node: BinaryNode, min: int, max: int, removelist: []) -> None:
        # Base Case
        if node is None:
            return

        # check is node is not leaf
        if node.left or node.right:
            node.left = self._removeOutsideRange3(node.left, min, max,  removelist)
            node.right = self._removeOutsideRange3(node.right, min, max,  removelist)
        else:
            if node.left is None and node.right is None and node.elem not in range(min, max):
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

    print("Remove leaf nodes out range: 1, 120")
    print("Nodos eliminados", aux.removeOutsideRange3(1,120))
    aux.draw()

    print("Remove leaf nodes out range: 15, 20")
    print("Nodos eliminados", aux.removeOutsideRange3(15,20))
    aux.draw()


    print("Remove leaf nodes out range: 0, 0")
    print("Nodos eliminados", aux.removeOutsideRange3(0,0))
    aux.draw()


