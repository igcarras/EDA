# from binarysearchtree import BinarySearchTree
from bst import BinarySearchTree
from bst import BinaryNode


class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root=self._insert(self._root,elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        """gets a node, searches the place to insert a new node with element e (using super()._insert),  and then,
        the function has to balance the node returned by the function super.()_insert"""
        node = super()._insert(node, elem)
        node = self._rebalance(node)
        return node

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """ gets a node, searches the node with element elem in the subtree that hangs down node , and
        then remove this node (using super()._remove). After this, the function has to balance the node returned by the function super()._remove"""
        node = super()._remove(node, elem)
        node = self._rebalance(node)
        return node

    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        """ gets node and balances it"""
        if node._balance() <= -2 and node._right._balance() <= -1:
            node = node._rotate_left(node)
        elif node._balance() >= 2 and node._left._balance() >= 1:
            node = node.rotate_right(node)
        elif node._balance() <= -2 and node._left._balance() >= 1:
            node._right = node._right._rotate_right(node._right)
            node = node._rotate_left(node)
        elif node._balance() >= 2 and node._right._balance() <= -1:
            node._left = node._left._rotate_left(node._left)
            node = node.rotate_right(node)

        return node

    def _balance(self):
        if self.left is None:
            left_height = 0
        else:
            left_height = self.left._height

        if self.right is None:
            right_height = 0
        else:
            right_height = self.right._height

        balance = left_height - right_height
        return balance

    def _rotate_left(self,node):
        a = node.right.left
        new  = node.right
        new.left = node
        node.right = a
        node._height()
        return new

    def _rotate_left(self,node):
        a = node.left.right
        nuevo = node.left
        nuevo.right = node
        node.left = a
        node._height()
        return a

    def node_height(self,node):
        '''ayuda a las funciones rotate right como left a determinar el peso del nodo'''
        if node is None:
            height = 0
        else:
            height = node.height
        return height

