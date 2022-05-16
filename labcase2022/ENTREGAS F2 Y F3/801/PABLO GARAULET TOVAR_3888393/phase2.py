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

    def fe_height(self, node: BinaryNode) -> int:
        return self._fe_height(node)

    def _fe_height(self, node: BinaryNode) -> int:
        if node is None:
            return 0
        else:
            return self._height(node.right) - self._height(node.left)

    def simple_left_rotation(self, node:BinaryNode) ->BinaryNode:
        aux = node.right
        aux1 = aux.left
        aux.left = node
        node.right = aux1
        return aux
    def simple_right_rotation(self, node:BinaryNode) ->BinaryNode:
        aux = node.left
        aux1 = aux.right
        aux.right = node
        node.left = aux1
        return aux

    #las dobles pueden desequilibrar
    #puede que vuelvas a tener que equilibrar los nodeos que vuelven
    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        """ gets node and balances it"""
        """ si el factor de equilibrio es positivo quiere decir, que está
        cargado a la izq y si ocurre lo contrario (el balance de un nodo es 
        negativo) quiere decir que está cargado a la der """
        #cargado a la derecha -----> left rotation
        #cargado a la izquierda ----> right rotation
        fe = self.fe_height(node)
        if fe >= 2 and self.fe_height(node.right) == 1: #rotación simple izquierda
            node = self.simple_left_rotation(node)
        if fe <= -2 and self.fe_height(node.left) == -1: #rotación simple derecha
            node = self.simple_right_rotation(node)
        if fe <= -2 and node.left != None:
            if node.left.right != None:
                node.left = self.simple_left_rotation(node.left)
                node.left = self._rebalance(node.left)
                node = self.simple_right_rotation(node)
        if fe >= 2 and node.right != None:
            if node.right.left != None:
                node.right = self.simple_right_rotation(node.right)
                node.right = self._rebalance(node.right)
                node = self.simple_left_rotation(node)
        return node

