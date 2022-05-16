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
        then remove this node (using super()._remove). After this, the function has to balance the node
        returned by the function super()._remove"""
        node = super()._remove(node, elem)
        node = self._rebalance(node)
        return node

    # ------------------------------- BY US ----------------------------------------------------------------------------

    def _rebalance(self, node: BinaryNode) -> BinaryNode:

        if node and abs(self.fe_height(node.elem)) >= 2:

            # Codigo de ayuda para ver lo que pasa
            """print("Equilibrar:", node.elem)"""

            # rotaciones simples (los dos factores de equilibrio tienen el mismo signo)
            if self.fe_height(node.elem) <= -2 and self.fe_height(node.right.elem) <= 0:
                self.rotar_izq(node)

            elif self.fe_height(node.elem) >= 2 and self.fe_height(node.left.elem) >= 0:
                self.rotar_dcho(node)

            # rotaciones compuestas (los dos factores de equilibrio tienen signo opuesto)
            elif self.fe_height(node.elem) >= 2 and self.fe_height(node.left.elem) <= 0:
                self.rotar_izq(node.left)
                self.rotar_dcho(node)

            elif self.fe_height(node.elem) <= -2 and self.fe_height(node.right.elem) >= 0:
                self.rotar_dcho(node.right)
                self.rotar_izq(node)

            # Al refactorizar el arbol el nodo se mueve de sitio, por lo que hay que actualizarlo
            if not node == self._root:
                node = self.prev_node(node.elem)

        # Codigo de ayuda para ver lo que pasa
        """print("\tRevisando nodo:", node)"""
        """self.draw()"""
        return node

    def rotar_izq(self, node):
        # Rotacion simple hacia la izquierda

        # Nodo que se conecta al subarbol
        prev_node = self.prev_node(node.elem)

        # Se realizan los cambios en el subarbol
        sub_tree = AVLTree()
        sub_tree._root = node.right
        aux_node = node.right.left
        node.right.left = node
        node.right = aux_node

        # Se conecta prev_node con el subarbol
        if prev_node:
            if prev_node.elem < sub_tree.prev_node(node.elem).elem:
                prev_node.right = sub_tree.prev_node(node.elem)
            elif prev_node.elem > sub_tree.prev_node(node.elem).elem:
                prev_node.left = sub_tree.prev_node(node.elem)
        # Si no habia nodo anterior la raiz del arbol es la misma que la del subarbol
        else:
            self._root = sub_tree._root

    def rotar_dcho(self, node):
        # Rotacion simple hacia la derecha

        # Nodo que se conecta al subarbol
        prev_node = self.prev_node(node.elem)

        # Se realizan los cambios en el subarbol
        aux_node = node.left.right
        sub_tree = AVLTree()
        sub_tree._root = node.left
        node.left.right = node
        node.left = aux_node

        # Se conecta prev_node con el subarbol
        if prev_node:
            if prev_node.elem < sub_tree.prev_node(node.elem).elem:
                prev_node.right = sub_tree.prev_node(node.elem)
            elif prev_node.elem > sub_tree.prev_node(node.elem).elem:
                prev_node.left = sub_tree.prev_node(node.elem)
        # Si no habia nodo anterior la raiz del arbol es la misma que la del subarbol
        else:
            self._root = sub_tree._root

    def prev_node(self, elem):
        # Devuelve el nodo previo a elem
        return self._prev_node(self._root, elem)

    def _prev_node(self, node, elem):
        # Funcion recursiva

        # Caso base, el proximo elemento es el buscado
        if (node.elem > elem == node.left.elem) or (node.elem < elem == node.right.elem):
            return node
        # Recursion con el siguiente elemento
        elif elem < node.elem:
            return self._prev_node(node.left, elem)
        elif elem > node.elem:
            return self._prev_node(node.right, elem)

    def fe_height(self, elem):
        # Devuelve el factor de equilibrio de un elemento, si es positivo pesa mas por el lado izquierdo y viceversa
        node = self.search(elem)
        if not node:
            return 0
        else:
            return self._height(node.left) - self._height(node.right)