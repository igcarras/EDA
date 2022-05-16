#from binarysearchtree import BinarySearchTree
from bst import BinarySearchTree
from bst import BinaryNode


class AVLTree(BinarySearchTree):

    def __str__(self):
        self.draw()

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root = self._insert(self._root, elem)

    def _insert(self, nodo: BinaryNode, elem: object) -> BinaryNode:
        """gets a node, searches the place to insert a new node with element e (using super()._insert),  and then,
        the function has to balance the node returned by the function super.()_insert"""
        nodo = super()._insert(nodo, elem)
        nodo = self._rebalance(nodo)
        return nodo

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, nodo: BinaryNode, elem: object) -> BinaryNode:
        """ gets a node, searches the node with element elem in the subtree that hangs down node , and
        then remove this node (using super()._remove). After this, the function has to balance the node returned by
        the function super()._remove"""
        nodo = super()._remove(nodo, elem)
        nodo = self._rebalance(nodo)
        return nodo

    def _rebalance(self, nodo: BinaryNode) -> BinaryNode:
        """ gets node and balances it"""
        self.__str__()
        fe = self.factor_equilibrio(nodo)
        if fe >= 2:
            caso = self.caso(nodo)
            if caso == "izquierda":
                nodo = self.mover_arbol_izq(nodo)
            elif caso == "derecha":
                nodo = self.mover_arbol_dcha(nodo)
            elif caso == "derecha-izquierda":
                nodo.right = self.mover_arbol_dcha(nodo.right)
                nodo = self.mover_arbol_izq(nodo)
            elif caso == "izquierda-derecha":
                nodo.left = self.mover_arbol_izq(nodo.left)
                nodo = self.mover_arbol_dcha(nodo)
        self.__str__()
        return nodo

    def factor_equilibrio(self, nodo: BinaryNode):
        """calcula el factor de equilibrio de un nodo"""
        if nodo:
            return abs(self._height(nodo.left) - self._height(nodo.right))
        else:
            return 0

    def caso(self, nodo):
        if self._height(nodo.left) > self._height(nodo.right):
            if self._height(nodo.left.left) >= self._height(nodo.left.right):
                caso = "derecha"
            else:
                caso = "izquierda-derecha"
        else:
            if self._height(nodo.right.left) <= self._height(nodo.right.right):
                caso = "izquierda"
            else:
                caso = "derecha-izquierda"
        return caso

    def mover_arbol_izq(self, nodo):
        nodoAux = nodo.right
        nodo.right = nodoAux.left
        nodoAux.left = nodo
        return nodoAux

    def mover_arbol_dcha(self, nodo):
        nodoAux = nodo.left
        nodo.left = nodoAux.right
        nodoAux.right = nodo
        return nodoAux
