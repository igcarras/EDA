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

    def fe(self, node: BinaryNode):
        """ Calcula el factor de equilibrio"""
        # Si no hay nodo, no puede estar desbalanceado
        if node is None:
            return 0
        # Devuelve la diferencia absoluta entre la altura izquierda y la derecha
        return abs(self._height(node.right) - self._height(node.left))

    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        """ gets node and balances it"""
        # Calcula el factor de equilibrio para ver si está balanceado
        fe = self.fe(node)
        # Si el fe es más de 1, hace falta rebalancear
        if fe > 1:
            # Comprueba si el desbalanceo es hacia la izquierda o derecha
            if self._height(node.left) > self._height(node.right):
                # El desbalanceo es hacia la izquierda así que se toma el nodo izquierdo
                sig = node.left
                # Comprueba si hace falta una doble rotación izquierda derecha
                if self._height(sig.right) > self._height(sig.left):
                    # Cambia enlaces, node.left apunta a sig.right, sig.right.left apunta a sig y sig.right apunta a sig.right.left
                    node.left, sig.right.left, sig.right = sig.right, sig, sig.right.left
                    sig = node.left     #node.left ha cambiado al cambiar enlaces
                node.left, sig.right = sig.right, node  #rotación derecha
                return sig

            else:
                # El desbalanceo es hacia la derecha así que se toma el nodo derecho
                sig = node.right
                if self._height(sig.right) < self._height(sig.left):    # Doble rotación derecha izquierda
                    node.right, sig.left.right, sig.left = sig.left, sig, sig.left.right
                    sig = node.right
                node.right, sig.left = sig.left, node   #rotación izquierda
                return sig

        return node

