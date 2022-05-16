# from binarysearchtree import BinarySearchTree
from bst import BinarySearchTree
from bst import BinaryNode


class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root = self._insert(self._root,elem)

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

    def fact_equilibrio(self, node: BinaryNode):
        """ Me va a calcular el factor de equilibrio de cada nodo """
        if node is None:
            return 0
        else:
            return self._height(node.right) - self._height(node.left)

    def _rebalance(self, node):
        """ Se encarga de decidir que rotación va a realizarse en función del valor del factor de equilibrio que
        se ha devuelto """
        if self.fact_equilibrio(node) >= 2: # <= 1
            if self.fact_equilibrio(node.right) < 0:
                return self.doubleRightRotate(node)
            else:
                return self.singleRightRotate(node)
        elif self.fact_equilibrio(node) <= -2:
            if self.fact_equilibrio(node.left) > 0:
                return self.doubleLeftRotate(node)
            else:
                return self.singleLeftRotate(node)
        else:
            return node

    def singleLeftRotate(self, node:BinaryNode):
        """Encargado de la rotación simple izquierda """
        #               70
        #            /     \
        #          40      100
        #        /    \   /   \
        #       17    55 80  130   (55) node / node1.right
        #             /
        #            30    node1 / node
        #            /
        #           28

        node1 = node.left
        node.left = node1.right
        node1.right = node
        #node._height = max(self._height(node.right), self._height(node.left)) + 1
        #node1._height = max(self._height(node1.left), node._height) + 1
        return node1

    def singleRightRotate(self, node:BinaryNode):
        """Encargado de la rotación simple derecha """
        node1 = node.right
        node.right = node1.left
        node1.left = node
        #node._height = max(self._height(node.right), self._height(node.left)) + 1
        #node1._height = max(self._height(node1.right), node._height) + 1
        return node1

    def doubleRightRotate(self, node):
        node.right = self.singleLeftRotate(node.right)
        return self.singleRightRotate(node)

    def doubleLeftRotate(self, node):
        node.left = self.singleRightRotate(node.left)
        return self.singleLeftRotate(node)