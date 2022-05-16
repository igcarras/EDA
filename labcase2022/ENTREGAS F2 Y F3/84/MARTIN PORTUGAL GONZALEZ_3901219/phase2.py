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

        if self.equilibrio(node) < -1:
            if self.equilibrio(node.right) <=0:
                return self.rotate_left(node)
            else: # doble rotacion derecha-izquierda
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        if self.equilibrio(node) > 1:
            if self.equilibrio(node.left) >=0:
                return self.rotate_right(node)
            else: # doble rotacion izquierda-derecha
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
        return node

    def equilibrio(self, node: BinaryNode):
        if node == None:
            return 0
        else:
             return self._height(node.left) - self._height(node.right)
        # se encarga de calcular el coeficiente de equilibrio a partir del cual funciona el rebalance

    def rotate_left(self, node):
        k1=node.right
        right_part = k1.left
        k1.left=node
        node.right = right_part
        return k1
        # se desbalancea con tres nodos seguidos hacia la derecha, y lo convierte en un nodo con dos hijos

    def rotate_right(self, node):
        k1 = node.left
        left_part= k1.right
        k1.right = node
        node.left = left_part
        return k1
        # se desbalancea con tres nodos seguidos hacia la izquierda, y lo convierte en un nodo con dos hijos
