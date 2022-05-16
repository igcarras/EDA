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
        then remove this node (using super()._remove). After this, the function has to balance the node returned by the
        function super()._remove"""
        node = super()._remove(node, elem)
        node = self._rebalance(node)
        return node

    def _rebalance(self, node):
        # Si el node es none le ignoramos
        if node:
            # Calculamos su factor de equilibrio y en caso de que sea menor a dos le ignoramos
            if abs(self._height(node.left) - self._height(node.right)) > 1:
                # Rotación izquierda
                if self._height(node.right) > self._height(node.left):
                    # Rotación derecha(rotación derecha-izquierda)
                    if self._height(node.right.right) < self._height(node.right.left):
                        ele = node.right
                        node.right = node.right.left
                        node.right.right = ele
                        node.right.right.left = None

                    ele = node.right.left
                    node.right.left = node
                    node = node.right
                    node.left.right = ele
                # Rotación derecha
                elif self._height(node.right) < self._height(node.left):
                    # Rotación izquierda(rotación izquierda-derecha)
                    if self._height(node.left.right) > self._height(node.left.left):
                        ele = node.left
                        node.left = node.left.right
                        node.left.left = ele
                        node.left.left.right = None

                    ele = node.left.right
                    node.left.right = node
                    node = node.left
                    node.right.left = ele
        return node
