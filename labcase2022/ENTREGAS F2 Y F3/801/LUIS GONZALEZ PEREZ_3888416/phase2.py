#Álvaro Moreno Martín y Luis González Pérez, Grupo 801

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
        if node is not None:
            #Comparamos subárbol derecho e izquierdo
            equilibrio = self._height(node.right) - self._height(node.left)
            #Desequilibrado por la izquierda, rotación derecha
            if equilibrio < -1:
                #Si hace falta se rota el nodo inferior (rotacion izquierda-derecha)
                if node.left is not None and self._height(node.left.right) - self._height(node.left.left) > 0:
                    node.left = self._rotarizq(node.left)
                    
                node = self._rotarder(node)
            #Desequilibrado por la derecha, rotación izquierda
            elif equilibrio > 1:
                #Si hace falta se rota el nodo inferior (rotacion derecha-izquierda)
                if node.right is not None and self._height(node.right.right) - self._height(node.right.left) < 0:
                    node.right = self._rotarder(node.right)
                    
                node = self._rotarizq(node)
                                 
        return node
    
    def _rotarizq(self, node):
        #Rotación simple izquierda
        node2 = node.right
        left = node2.left
        node2.left = node
        node.right = left
        return node2
    
    def _rotarder(self, node):
        #Rotación simple derecha
        node2 = node.left
        right = node2.right
        node2.right = node
        node.left = right
        return node2