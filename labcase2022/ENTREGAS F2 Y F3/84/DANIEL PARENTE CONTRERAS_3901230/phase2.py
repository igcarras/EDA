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
        if self.f_equilibrio(node) > 1: # Primero comprobamos el factor de equilibrio
            """Si el árbol está desequilibrado, dependiendo de la configuración de los nodos elegimos el tipo de rotación,
            empezando por las más sencillas"""
            if node.left != None and node.left.left != None: 
                node = self.rotacion_derecha(node)
                return node
            
            if node.right != None and node.right.right != None:
                node = self.rotacion_izquierda(node)
                return node
            if node.left != None and node.left.right != None:
                node = self.rotacion_izquierda_derecha(node)
                return node
            if node.right != None and node.right.left != None:
                node = self.rotacion_derecha_izquierda(node)
                return node

        return node

    def f_equilibrio(self, node : BinaryNode) -> int:
        """Comprueba el factor de equilibrio viendo la diferencia de altura de las ramas de los dos hijos del nodo"""
        if node == None:
            return 0
        return abs(self._height(node.left) - self._height(node.right))

    def rotacion_derecha(self, node):
        """Rotación derecha y rotación izquierda siguen los pasos indicados en la teoría, añadiendo dos punteros para poder
            conservar los subárboles cuando sea necesario"""
        puntero_a = node.left.right
        puntero_b = node.left
        node.left.right = node
        node.left = puntero_a
        node = puntero_b
        return node

    def rotacion_izquierda(self,node): # Rotación igual a la derecha pero en el otro sentido
        puntero_a = node.right.left
        puntero_b = node.right
        node.right.left = node
        node.right = puntero_a
        node = puntero_b
        return node
        
    def rotacion_izquierda_derecha(self, node): 
        """Primero se manipulan los nodos y se añaden dos punteros para poder conservar los distintos subárboles y poder
            colocar los nodos de tal forma que se pueda completar el movimiento con una rotaciónd derecha"""
        puntero_h2 = node.left.right.left
        puntero_a = node.left
        node.left = puntero_a.right
        node.left.left = puntero_a
        puntero_a.right = puntero_h2
        return self.rotacion_derecha(node)

    def rotacion_derecha_izquierda(self, node): # Igual que el método anterior pero en el otro sentido
        puntero_h2 = node.right.left.right
        puntero_a = node.right
        node.right = puntero_a.left
        node.right.right = puntero_a
        puntero_a.left = puntero_h2
        return self.rotacion_izquierda(node)
