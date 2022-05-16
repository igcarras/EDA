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
        if self.factorEquilibrio(node) > 1: #rotacion derecha
            if self.factorEquilibrio(node.left) < 0: #rotación izquierda derecha
                node.left = self.rotacionIzquierda(node.left)
            return self.rotacionDerecha(node)
        if self.factorEquilibrio(node) < -1:
            if self.factorEquilibrio(node.right) > 0:
                node.right = self.rotacionDerecha(node.right)
            return self.rotacionIzquierda(node)
        return node

    def factorEquilibrio(self,node):
        if not node:
            return 0
        else:
            return self._height(node.left) - self._height(node.right)
        
    def rotacionIzquierda(self,node):
       auxRightNode = node.right
       n = auxRightNode.left
       auxRightNode.left = node
       node.right = n
       return auxRightNode

    def rotacionDerecha(self,node):
        auxLeftNode = node.left
        n = auxLeftNode.right
        auxLeftNode.right = node
        node.left = n
        return auxLeftNode
    

        
    



