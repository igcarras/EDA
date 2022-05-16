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
        
        if self.fac_height(node) > 1:
            if self.fac_height(node.left) < 0:
                node.left = self.rot_simple_izq(node.left)
            return self.rot_simple_dch(node)
        if self.fac_height(node) < -1:
            if self.fac_height(node.right) > 0:
                node.right = self.rot_simple_dch(node.right)
            return self.rot_simple_izq(node)
        return node

    def fac_height(self, nodeIt: BinaryNode) -> int:

        if nodeIt:
            return self._height(nodeIt.left)-self._height(nodeIt.right)
        else:
            return 0


    def rot_simple_izq(self, node):

        raiz = node.right
        aux = raiz.left
        raiz.left = node
        node.right = aux
        return raiz

    def rot_simple_dch(self, node):

        raiz = node.left
        aux = raiz.right
        raiz.right = node
        node.left = aux
        return raiz



