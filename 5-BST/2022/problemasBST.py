# -*- coding: utf-8 -*-

from bst import BinarySearchTree
from bst import BinaryNode


class BST2(BinarySearchTree):
    def minimum(self) -> object:
        """returns the smallest key of the tree. What is its temporal complexity?"""
        # Complexity: O(log n)
        if self._root is None:
            print('tree is empty')
            return None

        node = self._root
        while node.left:
            node = node.left

        return node.elem

    def minimum_rec(self) -> object:
        """recursive function to return the smallest elem"""
        return self._minimum_rec(self._root)

    def _minimum_rec(self, node: 'BSTNode') -> object:
        if node is None:
            return None  # base case
        elif node.left is None:
            return node.elem  # base case
        else:
            return self._minimum_rec(node.left)  # recursive case

    def maximum(self) -> object:
        """returns the greatest elem of the tree. What is its temporal complexity?"""
        # Complexity: O(log n)
        if self._root is None:
            print('tree is empty')
            return None

        node = self._root
        while node.right:
            node = node.right

        return node.elem

    def maximum_rec(self) -> object:
        """recursive function that returns the largest object"""
        return self._maximum_rec(self._root)

    def _maximum_rec(self, node: 'BSTNode') -> object:
        if node is None:
            return None  # base case
        elif node.right is None:
            return node.elem  # base case
        else:
            return self._maximum_rec(node.right)  # base recursive

    def sum_elems(self) -> object:
        """ returns the sum of all its elems. What is its temporal complexity?"""
        # Complexity: O(n), where n is the _size of the tree.
        # The function has to visit all the nodes of the tree.
        return self._sum_elems(self._root)

    def _sum_elems(self, node: 'BSTNode') -> object:
        if node:
            return node.elem + self._sum_elems(node.left) + self._sum_elems(node.right)
        else:
            return 0

    def prints10(self) -> None:
        """prints the elems of those nodes whose grandparents' elems are multiply of 10
        What is its temporal complexity"""
        # Complexity: O(n), where n is the _size of the tree.
        # The function has to visit all the nodes of the tree.
        self._prints10(self._root, None, None)

    def _prints10(self, node: 'BSTNode', parent: 'BSTNode', grand: 'BSTNode') -> None:
            if grand and grand.elem % 10 == 0:
                print(node.elem, end=' ')
            self._prints10(node.right, node, parent)

    def _maximum_node(self, node: 'BSTNode') -> 'BSTNode':
        """returns the node with the maximum elem in the subtree node.
        This is the node that is furthest to the right
        """
        max_node = node
        while max_node.right is not None:
            max_node = max_node.right
        return max_node

    def _remove(self, node: 'BSTNode', elem: object) -> 'BSTNode':
        if node is None:
            return None

        if elem < node.elem:
            node.left = self._remove(node.left, elem)
        elif elem > node.elem:
            node.right = self._remove(node.right, elem)
        else:
            # elem == node.elem
            if node.left is None and node.right is None:
                # node is a leave
                node = None
            elif node.left is None:  # only has the right child
                return node.right
            elif node.right is None:  # only has the left child
                return node.left
            else:  # elem == node.elem
                predecessor = self._maximum_node(node.left)
                print('predecessor: ', predecessor.elem)
                node.elem = predecessor.elem
                node.left = self._remove(node.left, predecessor.elem)

        return node

    def fe_size(self, elem: object) -> int:
        """gives an elem, and returns the _size balance factor of
        its node """
        node = self.search(elem)
        return self._fe_size(node)

    def _fe_size(self, node: 'BSTNode') -> int:
        """returns the _size balance factor of the input node"""
        if node is None:
            return 0
        else:
            return abs(self._size(node.left) - self._size(node.right))

    def is_size_balanced(self) -> bool:
        """return True if the tree is _size balanced"""
        return self._is_size_balanced(self._root)

    def _is_size_balanced(self, node: 'BSTNode') -> bool:
        """returns True if the node is _size balanced;
        a node is balanced if its _size factor is <=1 and
        its two children are _size balanced"""
        if node:
            return self._fe_size(node) <= 1 and \
                   self._is_size_balanced(node.left) and \
                   self._is_size_balanced(node.right)
        else:
            return True

    def fe_height(self, elem: object) -> int:
        """gives an elem, and returns the height balance factor of
        its node """
        node = self.search(elem)
        return self._fe_height(node)

    def _fe_height(self, node: 'BSTNode') -> int:
        """returns the height balance factor of the input node"""
        if node is None:
            return 0
        else:
            return abs(self._height(node.left) - self._height(node.right))

    def is_height_balanced(self) -> bool:
        """return True if the tree is height balance, that is,
        if its root is height balanced"""
        return self._is_height_balanced(self._root)

    def _is_height_balanced(self, node: 'BSTNode') -> bool:
        """return True if the node is balanced, False e.o.c
        A node is balanced if its height balance <=1 and
        its two children are height balanced"""
        if node:
            return self._fe_height(node) <= 1 and \
                   self._is_height_balanced(node.left) and \
                   self._is_height_balanced(node.right)
        else:
            return True

    def findMaxforN(self, n: int) -> int:
        return self._findMaxforN(self._root, n)

    def _findMaxforN(self, node: 'BSTNode', n:int)->int:
        # Base cases
        if node == None:
            return -1
        if node.elem == n:
            return n

        # If root's value is smaller, try in
        # right subtree
        elif node.elem  < n:
            k = self._findMaxforN(node.right, n)
            if k == -1:
                return node.elem
            else:
                return k

        # If root's key is greater, return
        # value from left subtree.
        elif node.elem > n:
            return  self._findMaxforN(node.left, n)


    def lwc(self, a, b):
        """returns the lowest common ancestor of a and b"""
        nodeA = self.search(a)
        if nodeA == None:
            return None

        nodeB = self.search(b)
        if nodeB == None:
            return None

        return self._lwc(self._root, nodeA, nodeB)


    def _lwc(self, node, nodeA, nodeB):
        if node == None:
            return None

        if nodeA.elem < node.elem and nodeB.elem < node.elem:
            return self._lwc(node.left, nodeA, nodeB)

        if nodeA.elem > node.elem and nodeB.elem > node.elem:
            return self._lwc(node.right, nodeA, nodeB)

        return node.elem


if __name__ == "__main__":
    tree = BST2()
    for x in [50, 60, 30, 20, 24, 70, 66, 65, 10, 80, 21, 15, 35, 45, 22]:
        tree.insert(x)

    print('input tree:')
    tree.draw()
    print()
    print('Minimum elem of the tree:', tree.minimum())
    print('Maximum elem of the tree:', tree.maximum())
    print('sum of all its elems:', tree.sum_elems())
    print("elems whose grandparents' elems are multiply of 10")
    tree.prints10()
    print()

    tree.remove(50)
    # 50 should have been replaced by 45 as root
    print('after remove 50')
    tree.draw()

    tree.remove(70)
    print('after remove 70')
    # 70 should have been replaced by 66 as root
    tree.draw()

    tree.remove(20)
    # 20 should have been replaced by 15 as root
    print('after remove 20')
    tree.draw()

    tree.insert(55)
    tree.insert(36)
    tree.insert(50)
    tree.insert(32)
    tree.insert(56)
    print('after insert 55,36,50,32,56')
    tree.draw()
    print()
    for x in [45, 60, 30, 15, 35, 10, 24, 21, 66, 80, 63, 55, 36, 50, 32, 56]:
        print('_size-balanced factor of  {} is {}'.format(x, tree.fe_size(x)))
        print('height-balanced factor of  {} is {}'.format(x, tree.fe_height(x)))
        print()

    n=1
    tree.draw()
    print("encontrado para ", n, " el valor ", tree.findMaxforN(n))


    values = [50, 48, 70, 30, 65, 90, 20, 32, 67, 98, 15, 25, 31, 35, 66, 69, 94, 99]

    tree = BST2()
    for x in values:
        tree.insert(x)

    tree.draw()

    print(tree.lwc(48,70),50)
    print(tree.lwc(30,70),50)
    print(tree.lwc(30,65),50)
    print(tree.lwc(20,32),30)
    print(tree.lwc(67,90),70)
    print(tree.lwc(69,99),70)
    print(tree.lwc(31,94),50)
    print(tree.lwc(15,25),20)
    print(tree.lwc(15,35),30)
    print(tree.lwc(67,70),70)
    print(tree.lwc(30,35),30)

    values = [20,8,4,12,10,14,22]

    tree = BST2()
    for x in values:
        tree.insert(x)

    tree.draw()

    print(tree.prints10())
