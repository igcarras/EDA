# Daniel Sánchez de la Cruz. NIA: 100475344
# Simón Benzaquen Aserraf. NIA: 100475237

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
        if node is None:
            return None

        # Calculamos el factor de equilibrio para el subárbol
        bf = super()._height(node.left) - super()._height(node.right)

        # Equilibramos el subárbol con las rotaciones correspondientes
        if bf > 1:
            # Rotación simple derecha o rotación doble izquierda-derecha
            aux = node.left
            if aux.left:
                node = self._rot_dcha(node)
            else:
                node = self._rot_izda_dcha(node)
        elif bf < -1:
            # Rotación simple izquierda o rotación doble derecha-izquierda
            aux = node.right
            if aux.right:
                node = self._rot_izda(node)
            else:
                node = self._rot_dcha_izda(node)

        return node

    # Rotación izquierda
    def _rot_izda(self, node: BinaryNode) -> BinaryNode:
        aux = node.right
        node.right = aux.left
        aux.left = node
        return aux

    # Rotación derecha
    def _rot_dcha(self, node: BinaryNode) -> BinaryNode:
        aux = node.left
        node.left = aux.right
        aux.right = node
        return aux

    # Rotación izquierda-derecha
    def _rot_izda_dcha(self, node: BinaryNode) -> BinaryNode:
        node.left = self._rot_izda(node.left)
        return self._rot_dcha(node)

    # Rotación derecha-izquierda
    def _rot_dcha_izda(self, node: BinaryNode) -> BinaryNode:
        node.right = self._rot_dcha(node.right)
        return self._rot_izda(node)