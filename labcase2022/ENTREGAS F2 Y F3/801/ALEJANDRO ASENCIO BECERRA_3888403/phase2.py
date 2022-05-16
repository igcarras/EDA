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

    def balancefactor(self, node):

        if node:
            return self._height(node.left) - self._height(node.right)
        else:
            return 0

    def leftRotation(self, node):
        rightnode = node.right
        aux = rightnode.left
        rightnode.left = node
        node.right = aux
        return rightnode

    def rightRotaton(self, node):
        leftnode = node.left
        aux = leftnode.right
        leftnode.right = node
        node.left = aux
        return leftnode

    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        """ gets node and balances it"""
        """left rotation"""
        if self.balancefactor(node) < -1:
            """right-left rotation"""
            if self.balancefactor(node.right) > 0:
                node.right = self.rightRotaton(node.right)
            return self.leftRotation(node)
        """right rotation"""
        if self.balancefactor(node) > 1:
            """left right rotation"""
            if self.balancefactor(node.left) < 0:
                node.left = self.leftRotation(node.left)
            return self.rightRotaton(node)

        return node












