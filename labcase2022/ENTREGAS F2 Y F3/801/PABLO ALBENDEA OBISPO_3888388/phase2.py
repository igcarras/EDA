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

    def _izq_simple(self, node):
        # Necesitamos 3 punteros, uno para el padre de node, otro para node y otro para node.left , me he dado cuenta de que si guardo el root en una variable y el hijo derecho en otra puedo cambiarlos
        if node and node.right is not None:
            hijo = node.right
            ayuda = hijo.left
            hijo.left = node
            node.right = ayuda
            return hijo

    def _der_simple(self, node):
        if node and node.left is not None:
            hijo = node.left
            ayuda = hijo.right
            hijo.right = node
            node.left = ayuda
            return hijo

    def _rotDerIzq(self, node):
        node.right = self._der_simple(node.right)
        node.right =self._rebalance(node.right)
        return self._izq_simple(node)

    def _rotIzqDer(self, node):
        node.left = self._izq_simple(node.left)
        node.left = self._rebalance(node.left)
        return self._der_simple(node)


    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        """ gets node and balances it"""
        if self._factorequilibrio(node) > 1: #Desiquilibrado al lado derecho

            if node.left:
                if super()._height(node.left.left) > super()._height(node.left.right):
                    #Si el nieto izquierdo tiene mayor altura rotación simple hacia la derecha

                    node = self._der_simple(node)

                else:
                    #Si el nieto derecho tiene mayor altura hace zigzag, hacer doble rotación izquierda derecha

                    node = self._rotIzqDer(node)


        elif self._factorequilibrio(node) < -1:
            if node.right:
                if (super()._height(node.right.right) > super()._height(node.right.left)):
                    #Si el nieto derecho tiene mayor altura rotación simple hacia la izquierda

                    node = self._izq_simple(node)

                else:
                    #Si el nieto izquierdo tiene mayor altura, doble rotación derecha izquierda
                    node= self._rotDerIzq(node)

        return node



    def _factorequilibrio(self, node: BinaryNode) -> int:
        """Saca el factor de equilibrio del nodo, positivo si tiene más peso el lado izquiero y negativo si tiene más peso el derecho"""
        if node is None:
            return 0
        else:
            return self._height(node.left) - self._height(node.right)