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
        if self._root !=None:
            
            if self.rebalance(node) > 1 and self.rebalance(node.left)>=0:
                return self.rotar_derecha(node)
            if self.rebalance(node) < -1 and self.rebalance(node.right) <= 0:
                return self.rotar_izquierda(node)
            if self.rebalance(node) > 1 and self.rebalance(node.left) < 0:
                node.left = self.rotar_izquierda(node.left)
                return self.rotar_derecha(node)
            if self.rebalance(node) < -1 and self.rebalance(node.right) > 0:
                node.right = self.rotar_derecha(node.right)
                return self.rotar_izquierda(node)
        return node 
      
    def rotar_izquierda(self, node:BinaryNode) -> BinaryNode: 
        mirar_derech = node.right 
        nod_derc_izqu = mirar_derech.left 
        mirar_derech.left = node
        node.right = nod_derc_izqu
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        mirar_derech.height = 1 + max(self._height(mirar_derech.left), self._height(mirar_derech.right))
        return mirar_derech
        
    def rotar_derecha(self, node:BinaryNode) -> BinaryNode:
        mirar_izquie = node.left
        nod_izqu_derec = mirar_izquie.right
        mirar_izquie.right = node
        node.left = nod_izqu_derec
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        mirar_izquie.height = 1 + max(self._height(mirar_izquie.left), self._height(mirar_izquie.right))
        return mirar_izquie

    def rebalance(self, node:BinaryNode) -> BinaryNode:
        if node is None:
            return 0
        else:
            return self._height(node.left) - self._height(node.right)