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

    def node_prev(self, elem: object) -> BinaryNode:
        """Devuelve el nodo anterior"""
        return self._node_prev(self._root, elem)

    def _node_prev(self, node: BinaryNode, elem: object) -> BinaryNode:
        if (node.elem > elem and elem == node.left.elem) or \
        (node.elem < elem and elem == node.right.elem): # Si es el elemento que queremos, lo devolvemos
           return node
        elif elem > node.elem: # Si el elemento es menor, nos movemos al nodo de la izquierda y volvemos a empezar
            return self._node_prev(node.right, elem)
        elif elem < node.elem: # Si el elemento es menor, nos movemos al nodo de la izquierda y volvemos a empezar
            return self._node_prev(node.left, elem)

    def fac_equ(self, elem: object) -> int:
        """Devuelve el factor de equilibrio"""
        node = self.search(elem) # Buscamos el elemento
        if node: # Si existe el nodo, realizamos la resta de la altura de ambos lados del arbol
            factor = self._height(node.left) - self._height(node.right)
            return factor # Devuelve el valor de la resta
        return 0 # Si no existe el nodo, el factor de equilibrio es 0

    def rot_izq(self, node: BinaryNode):
        """Rotacion Simple Izquierda"""
        node_prev = self.node_prev(node.elem) # Nodo desiquilibrado
        newtree = AVLTree() # Creamos el nuevo arbol
        newtree._root = node.right # La raiz es el nodo de la derecha
        node_next = node.right.left # node_next sera el nodo izquierdo de la raiz
        node.right.left = node # El nodo desiquilibrado pasa a ser nodo izquierdo
        node.right = node_next # El nodo derecho será el siguiente a node_next
        if node_prev:
            if node_prev.elem < newtree._root.elem: # Si el nodo anterior es menor que la raiz del nuevo arbol
                node_prev.right = newtree._root # La raiz es el nodo de la derecha
            elif node_prev.elem > newtree._root.elem: # Si el nodo anterior es mayor que la raiz del nuevo arbol
                node_prev.left = newtree._root # La raiz es el nodo de la izquierda
        else: # Si no hay nodo anterior, las raices son las mismas
            self._root = newtree._root

    def rot_der(self, node: BinaryNode):
        """Rotacion Simple Derecha"""
        node_prev = self.node_prev(node.elem) # Nodo anterior al desiquilibrado
        newtree = AVLTree() # Creamos el nuevo arbol
        newtree._root = node.left # La raiz es el nodo de la izquierda
        node_next = node.left.right # node_next sera el nodo derecho de la raiz
        node.left.right = node # El nodo desiquilibrado pasa a ser nodo derecho
        node.left = node_next # El hijo izquierdo será el siguiente a node_next
        if node_prev:
            if node_prev.elem < newtree._root.elem: # Si el nodo anterior es menor que la raiz del nuevo arbol
                node_prev.right = newtree._root # La raiz es el nodo de la derecha
            elif node_prev.elem > newtree._root.elem: # Si el nodo anterior es mayor que la raiz del nuevo arbol
                node_prev.left = newtree._root # La raiz es el nodo de la izquierda
        else: # Si no hay nodo anterior, las raices son las mismas
            self._root = newtree._root

    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        """Comprobacion si el arbol esta balanceado"""
        if node and (self.fac_equ(node.elem) > 1 or self.fac_equ(node.elem) < -1): # Si el factor de equilibrio es mayor que 1 o menor que -1,
                                                                                    # es que el arbol no esta equilibrado
            if self.fac_equ(node.elem) < -1 and self.fac_equ(node.right.elem) < 1: # Si el factor de equilibrio a ambos lados es negativo,
                self.rot_izq(node)                                                 # se necesita una rotación simple a la izquierda
            elif self.fac_equ(node.elem) > 1 and self.fac_equ(node.left.elem) > -1: # Si el factor de equilibrio a ambos lados es positivo,
                self.rot_der(node)                                                  # se necesita una rotación simple a la derecha
            elif self.fac_equ(node.elem) < -1 and self.fac_equ(node.right.elem) > -1: # Si el facor de equilibrio es negativo a un lado y positivo en el otro,
                self.rot_der(node.right)                                              # se necesita una rotación simple a la derecha del lado derecho
                self.rot_izq(node)                                                    # y una rotación simple a la izquierda
            elif self.fac_equ(node.elem) > 1 and self.fac_equ(node.left.elem) < 1: # Si el facor de equilibrio es positivo a un lado y negativo en el otro,
                self.rot_izq(node.left)                                            # se necesita una rotación simple a la izquierda del lado izquierdo
                self.rot_der(node)                                                 # y una rotación simple a la derecha
            if node != self._root: # Como hemos balanceado el arbol, hay que encontrar la nueva raiz
               node = self.node_prev(node.elem)
        return node