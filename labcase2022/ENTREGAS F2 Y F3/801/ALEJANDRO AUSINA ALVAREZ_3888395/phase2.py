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
        if node != None:
            fheight = self._height(node.left) - self._height(node.right)

            if fheight <= -2:
                if node.right:
                    if self._height(node.right.left) - self._height(node.right.right) > 0:
                        node.right = self.rightrot(node.right)

                node = self.leftrot(node)

            elif fheight >= 2:
                if node.left:
                    if self._height(node.left.left) - self._height(node.left.right) < 0:
                        node.left = self.leftrot(node.left)

                node = self.rightrot(node)

        return node

    def leftrot(self, node):
        noderight = node.right
        left = noderight.left
        noderight.left = node
        node.right = left

        return noderight

    def rightrot(self, node):
        nodeleft = node.left
        right = nodeleft.right
        nodeleft.right = node
        node.left = right

        return nodeleft



