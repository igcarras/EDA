# from binarysearchtree import BinarySearchTree
from bst import BinarySearchTree
from bst import BinaryNode
"""author: Daniel Consuegra Álvarez """

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

    def is_balanced(self) -> bool: # metodo para saber si un arbol esta desbalanceado comrpobando las alturas de los nodos
        """return True if the tree is height balance, that is,
        if its root is height balanced"""
        return self._is_balanced(self._root)

    def _is_balanced(self, node: 'BinaryNode') -> bool:
        """return True if the node is balanced, False e.o.c
        A node is balanced if its height balance <=1 and
        its two children are height balanced"""
        if node:
            return self._height(node) <= 1 and \
                   self._is_balanced(node.left) and \
                   self._is_balanced(node.right)
        else:
            return True

    def _rotleft(self,node:BinaryNode)-> BinaryNode:  #rotacion simple hacia la izquierda
        """el hijo derecho se convierte en raiz y la raiz en hijo izq"""
        newroot=node.right  #el hijo derecho se convierte en la nueva raiz
        aux=node.right.left  # guardamos el valor del nieto izq en un nodo auxiliar
        newroot.left=node    # el nodo izq de la nueva raiz es ahora el anterior nodo principal
        node.right=aux       # el hijo derecho ahora es el anterior nieto izq
        return newroot

    def _rotright(self,node:BinaryNode)-> BinaryNode: #rotacion simple hacia la derecha
        """el hijo izq se convierte en raiz y la raiz en hijo derecho"""
        newroot=node.left    #el hijo izq se convierte en la nueva raiz
        aux=node.left.right  # guardamos el valor del nieto derecho en un nodo auxiliar
        newroot.right=node   # el nodo dercho de la nueva raiz es ahora el anterior nodo principal
        node.left=aux        # el hijo izq ahora es el anterior nieto derecho
        return newroot

    def _rotdlr(self,node:BinaryNode)-> BinaryNode:
        node.left = self._rotleft(node.left)   # primero rotamos el hijo izq con una rotacion simple izq
        return self._rotright(node)  #devolvemos la rotacion derecha del nodo tras haber rotado el hijo izq

    def _rotdrl(self,node:BinaryNode)-> BinaryNode:
        node.right = self._rotright(node.right)   # primero rotamos el hijo derecho con una rotacion simple derecha
        return self._rotleft(node)      #devolvemos la rotacion izq del nodo tras haber rotado el hijo derecha


    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        """ gets node and balances it"""
        if not self._is_balanced(node): # si el nodo esta desbalanceado
            if node.left==None and node.right!=None and node.right.right!=None: # cuando hay hijo y nieto derecho y no hay hijo izq
                node=self._rotleft(node)   # aplicamos rotsimpleizq
            if node.right == None and node.left!=None and node.left.left!=None: # cuando hay hijo y nieto derecho y no hay hijo izq 
                node=self._rotright(node)   # aplicamos rotsimplederecha
            if node.left == None and node.right!=None and node.right.left!=None: # cuando hay nodo derecho y nieto izq pero no hay nodo izq
                node=self._rotdrl(node)  #rotacion doble derecha-izq
            if node.right == None and node.left!=None and node.left.right!=None: # cuando hay nodo izq y nieto derecho pero no nodo derecho
                node=self._rotdlr(node)  #rotacion doble izq-derecha
            # volvemos a comprobar las alturas por si hemos desbalanceado el arbol principal al balancear los subarboles
            if self._height(node.right)-self._height(node.left)>1:
                node=self._rotleft(node)
            if self._height(node.right)-self._height(node.left)<-1:
                node=self._rotright(node)
        return node



