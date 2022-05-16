# from binarysearchtree import BinarySearchTree
from bst import BinarySearchTree
from bst import BinaryNode


class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root = self._insert(self._root, elem)

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
        equilibrio = self._equilibrio(node)
        if equilibrio >= 2 and self._equilibrio(node.left) >= 0:
            return self._rot_der(node)
        if equilibrio <= -2 and self._equilibrio(node.right) <= 0:
            return self._rot_izq(node)
        if equilibrio >= 2 and self._equilibrio(node.left) < 0:
            node.left = self._rot_izq(node.left)
            return self._rot_der(node)
        if equilibrio <= -2 and self._equilibrio(node.right) >0:
            node.right = self._rot_der(node.right)
            return self._rot_izq(node)
        return node

    def _rot_izq(self, nodo):
        der = nodo.right
        izq = der.left

        der.left = nodo
        nodo.right = izq

        return der

    def _rot_der(self, nodo):
        izq = nodo.left
        der = izq.right

        izq.right = nodo
        nodo.left = der

        return izq

    def _equilibrio(self, nodo):
        """Devuelve el factor de equilibrado en altura"""
        if not nodo:
            return 0
        return self._height(nodo.left) - self._height(nodo.right)
