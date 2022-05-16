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
        if self.factor_De_Equilibrio(node) < -1:  # inicia la rotación hacia la izquierda
            if self.factor_De_Equilibrio(node.right) > 0:  # continua con la rotación de la izquierda pero en el nodo derecho
                node.right = self.rotacion_para_Derecha(node.right)
            return self.rotacion_para_Izquierda(node)
        if self.factor_De_Equilibrio(node) > 1:     # inicia la rotacion hacia la  derecha
            if self.factor_De_Equilibrio(node.left) < 0:  # continua con la rotación de la derecha pero en el nodo izquierdo
                node.left = self.rotacion_para_Izquierda(node.left)
            return self.rotacion_para_Derecha(node)
        return node


    def factor_De_Equilibrio(self, node):    #calculamos el factor de equilibrio
        if not node:        #verificamos si existe el arbol
            return 0
        else:
            return self._height(node.left) - self._height(node.right)


    def rotacion_para_Derecha(self, node):   #metodo para la rotacion a la derecha
        auxLeftNode = node.left
        x = auxLeftNode.right
        auxLeftNode.right = node
        node.left = x
        return auxLeftNode

    def rotacion_para_Izquierda(self, node):   #metodo para la rotacion a la izquierda
        auxRightNode = node.right
        x = auxRightNode.left
        auxRightNode.left = node
        node.right = x
        return auxRightNode

