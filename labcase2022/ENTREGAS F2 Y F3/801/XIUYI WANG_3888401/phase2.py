from bst import BinarySearchTree
from bst import BinaryNode


class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        """gets a node, searches the place to insert a new node with
        element e (using super()._insert),  and then, the function has to
        balance the node returned by the function super.()_insert"""
        node = super()._insert(node, elem)
        node = self._rebalance(node)
        return node

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """ gets a node, searches the node with element elem in the subtree
        that hangs down node , and then remove this node (using super(
        )._remove). After this, the function has to balance the node
        returned by the function super()._remove"""
        node = super()._remove(node, elem)
        node = self._rebalance(node)
        return node

    def fe_height(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def rebalance(self):
        return self._rebalance(self._root)

    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        """ gets node and balances it"""
        if self.fe_height(node) > 1:
            if node.elem > node.left.elem and node.left.left is not None:
                # rotación derecha
                return self.rotate_right(node)

            if node.elem > node.left.elem and node.left.left is None:
                # rotación LR
                return self.double_rotate_lr(node)

        if self.fe_height(node) < -1:
            if node.elem < node.right.elem and node.right.right is not None:
                # rotación izquierda
                return self.rotate_left(node)
            if node.elem < node.right.elem and node.right.right is None:
                # rotación RL
                return self.double_rotate_rl(node)
        return node

    def rotate_right(self, node):
        y = node.left
        temp = y.right
        y.right = node
        node.left = temp
        return y

    def rotate_left(self, node):
        y = node.right
        temp = y.left
        y.left = node
        node.right = temp
        return y

    def double_rotate_lr(self, node):
        y = node.left
        temp = y.left
        temp2 = y.right
        node.left = temp2
        temp2.left = y
        y.right = temp
        return self.rotate_right(node)

    def double_rotate_rl(self, node):
        y = node.right
        temp = y.right
        temp2 = y.left
        node.right = temp2
        temp2.right = y
        y.left = temp
        return self.rotate_left(node)
