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
        #equilibrio = self._equilibrado(node)
        equilibrio = self._factorequilibrio(node)
        if abs(equilibrio) < 2:
            return node
        else:
            if equilibrio < 0: #rama dcha > izq
                if self._factorequilibrio(node.right) > 0:
                    node.right = self._simpledcha(node.right)
                return self._simpleizq(node)
            else: #rama izq > dcha
                if self._factorequilibrio(node.left) < 0:
                    node.left = self._simpleizq(node.left)
                return self._simpledcha(node)

    def _factorequilibrio(self, node):
        if node is None:
            return 0
        else:
            return self._height(node.left) - self._height(node.right)

    def _simpleizq(self, node: BinaryNode):
        aux = node
        node = node.right
        aux2 = node.left
        node.left = aux
        node.left.right = aux2
        return node

    def _simpledcha(self, node: BinaryNode):
        aux = node
        node = node.left
        aux2 = node.right
        node.right = aux
        node.right.left = aux2
        return node