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
        if self._fe_height(node) > 1: # Está desiquilibrado el lado derecho
            if node.left is not None:
                if super()._height(node.left.left) > super()._height(
                        node.left.right): # Si la altura del nieto izquierdo
                    # es mayor signfica rotación simple hacia la derecha
                    node = self.rightRotate(node)
                else: # Si la altura es mayor en el nieto derecho tiene forma
                    # de zigzag y por tanto hay que hacer doble rotación
                    node = self.left_rightrotate(node)
        elif self._fe_height(node) < -1:
            if node.right is not None: # Está desiquilibrado el lado derecho
                if (super()._height(node.right.right) > super()._height(
                        node.right.left)):  # Si la altura del nieto derecho
                    # es mayor signfica rotación simple hacia la izquierda
                    node = self.leftRotate(node)
                else: # Si la altura es mayor en el nieto izquierdo tiene forma
                    # de zigzag y por tanto hay que hacer doble rotación
                    node = self.right_leftrotate(node)
        return node

    def leftRotate(self, node: BinaryNode) -> BinaryNode:
        if node is not None and node.right is not None:
            hijo = node.right
            aux = hijo.left
            hijo.left = node
            node.right = aux
            return hijo

    def rightRotate(self, node: BinaryNode) -> BinaryNode:
        if node.left is not None:
            hijo = node.left
            aux = hijo.right
            hijo.right = node
            node.left = aux
            return hijo

    def right_leftrotate(self, node: 'BinaryNode'):
        node.right = self.rightRotate(node.right)
        node.right = self._rebalance(node.right) 
        return self.leftRotate(node)

    def left_rightrotate(self, node):
        node.left = self.leftRotate(node.left)
        node.left = self._rebalance(node.left)
        return self.rightRotate(node)

    def _fe_height(self, node: BinaryNode) -> int:
        """returns the height balance factor of the input node"""
        if node is None:
            return 0
        else:
            return self._height(node.left) - self._height(node.right)
