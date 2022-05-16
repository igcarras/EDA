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
        then remove this node (using super()._remove). After this, the function has to balance the node returned by the
        function super()._remove"""
        node = super()._remove(node, elem)
        node = self._rebalance(node)
        return node

    # Método para calcular el factor de equilibrio de un nodo en específico.
    def factor_equilibrio(self, node: BinaryNode) -> int:
        if node is None:
            return 0
        else:
            return self._height(node.left) - self._height(node.right)

    # Método "_rebalance", que sirve para rebalancear el árbol en caso de que se desequilibre. Siempre que insertamos
    # o eliminamos un nodo accedemos a él, pero realmente incide en el árbol creado sí y sólo sí el factor de equilibrio
    # del nodo en el que nos encontremos es mayor que 1 o menor que -1.
    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        factor_equilibrio = self.factor_equilibrio(node)
        # Si el factor de equilibrio es mayor que 1, quiere decir que el subárbol izquierdo del nodo es mayor que el
        # derecho.
        if factor_equilibrio > 1:
            # Si la altura del subárbol izquierdo del hijo izquierdo del nodo es mayor que la altura del otro subárbol
            # (el derecho), tendremos que hacer una rotación simple derecha.
            # Si las alturas son iguales, querrá decir que estamos en el caso en el cual ambos subárboles de dicho
            # nodo están compuestos únicamente de un nodo, es decir, son nodos hoja.
            if self._height(node.left.left) >= self._height(node.left.right):
                node = self.rotacion_derecha(node)
            # Si tenemos una situación en la que esta rama del árbol hace un "zig-zag", tendremos que hacer una doble
            # rotación. En este caso, habrá que hacer una doble rotación izquierda-derecha.
            else:
                node = self.doble_rotacion_izquierda_derecha(node)

        # Si el factor de equilibrio es menor que -1, quiere decir que el subárbol derecho del nodo es mayor que el
        # izquierdo.
        if factor_equilibrio < -1:
            # Si la altura del subárbol derecho del hijo derecho del nodo es mayor que la altura del otro subárbol
            # (el izquierdo), tendremos que hacer una rotación simple izquierda.
            # Si las alturas son iguales, querrá decir que estamos en el caso en el cual ambos subárboles de dicho
            # nodo están compuestos únicamente de un nodo, es decir, son nodos hoja.
            if self._height(node.right.right) >= self._height(node.right.left):
                node = self.rotacion_izquierda(node)
            # Si tenemos una situación en la que esta rama del árbol hace un "zig-zag", tendremos que hacer una doble
            # rotación. En este caso, habrá que hacer una doble rotación derecha-izquierda.
            else:
                node = self.doble_rotacion_derecha_izquierda(node)
        return node

    def rotacion_derecha(self, c: BinaryNode) -> BinaryNode:
        # Subárbol inicial:
        #           C
        #         /   \
        #        B     T4
        #      /   \
        #     A     T3
        #   /   \
        # T1     T2
        b = c.left
        t3 = b.right

        b.right = c
        c.left = t3
        # Subárbol final:
        #           B
        #      /        \
        #     A          C
        #   /   \      /   \
        # T1     T2  T3     T4
        return b

    def doble_rotacion_izquierda_derecha(self, c: BinaryNode) -> BinaryNode:
        # Subárbol inicial:
        #           C
        #         /   \
        #        B     T4
        #      /   \
        #    T1     A
        #         /   \
        #       T2     T3
        b = c.left
        a = b.right
        t2 = a.left
        # Subárbol intermedio:
        #           C
        #         /   \
        #        A     T4
        #      /   \
        #     B     T3
        #   /   \
        # T1     T2
        c.left = a
        a.left = b
        b.right = t2
        # Subárbol final (después del return):
        #           A
        #      /        \
        #     B          C
        #   /   \      /   \
        # T1     T2  T3     T4
        return self.rotacion_derecha(c)

    def rotacion_izquierda(self, c: BinaryNode) -> BinaryNode:
        # Subárbol inicial:
        #           C
        #         /   \
        #       T1     B
        #            /   \
        #          T2     A
        #               /   \
        #             T3     T4
        b = c.right
        t2 = b.left

        b.left = c
        c.right = t2
        # Subárbol final:
        #           B
        #      /        \
        #     C          A
        #   /   \      /   \
        # T1     T2  T3     T4
        return b

    def doble_rotacion_derecha_izquierda(self, c: BinaryNode) -> BinaryNode:
        # Subárbol inicial:
        #           C
        #         /   \
        #       T1     B
        #            /   \
        #           A     T4
        #         /   \
        #       T2     T3
        b = c.right
        a = b.left
        t3 = a.right
        # Subárbol intermedio:
        #           C
        #         /   \
        #       T1     A
        #            /   \
        #          T2     B
        #               /   \
        #             T3     T4
        c.right = a
        a.right = b
        b.left = t3
        # Subárbol final (después del return):
        #           A
        #      /        \
        #     C          B
        #   /   \      /   \
        # T1     T2  T3     T4
        return self.rotacion_izquierda(c)


