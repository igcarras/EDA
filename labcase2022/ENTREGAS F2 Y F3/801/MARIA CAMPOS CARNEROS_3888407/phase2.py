# from binarysearchtree import BinarySearchTree
from bst import BinarySearchTree
from bst import BinaryNode


class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root = self._insert(self._root,elem)


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
        if node is None:
            return node
        
        hija_izq = node.left
        hija_der = node.right        
        altura_izq = super()._height(hija_izq)
        altura_der = super()._height(hija_der)
        dif = altura_izq - altura_der
        
        if -1 <= dif <= 1: #no hay desequilibrio
            return node
        
        nieta_izq = None
        nieta_der = None
        if altura_izq < altura_der:
            if hija_der is not None:
                nieta_izq = hija_der.left
                nieta_der = hija_der.right
        
            altura_n_izq = super()._height(nieta_izq)
            altura_n_der = super()._height(nieta_der)
            if altura_n_izq > altura_n_der:
                return self.rot_der_izq(node)
            else:
                return self.rot_izq(node)
        
        else:
            if hija_izq is not None:
                nieta_izq = hija_izq.left
                nieta_der = hija_izq.right
        
            altura_n_izq = super()._height(nieta_izq)    #si no existe esa nieta la altura es -1#
            altura_n_der = super()._height(nieta_der)
            if altura_n_izq < altura_n_der:
                return self.rot_izq_der(node)
            else:
                return self.rot_der(node)
            
    
    '''Implemento los m??todos de giro, para usarlos seg??n el tipo de desequilibrio que tenga'''
    #ROTACION A DERECHAS#
    def rot_der(self, node: BinaryNode) -> BinaryNode:
        '''
        PASOS:
        1??:Indico cual va a ser la nueva ra??z, en este caso a ser a drchas la ra??z ser?? el hijo izqdo del nodo desequilibrado
        2??:En el caso de que este tuviese hijos habr??a que reasignarles un lugar, para no perderlos -> variable auxiliar
        3??:La nueva ra??z va a tener como hijo drcho al nodo desequilibrado 
        4??:El antiguo nodo desequilibrado va a tener como hijo izqdo al antiguo hijo del actual nodo ra??z
        5??:Devuelvo la nueva ra??z para equilibrar el ??rbol 
        '''
        nuevo_root = node.left
        aux = node.left.right
        nuevo_root.right = node
        node.left = aux
        return nuevo_root

    #ROTACION A IZQUIERDAS#
        '''
        PASOS:
        1??:Indico cual va a ser la nueva ra??z, en este caso a ser a izqdas la ra??z ser?? el hijo drcho del nodo desequilibrado
        2??:En el caso de que este tuviese hijos habr??a que reasignarles un lugar, para no perderlos -> variable auxiliar
        3??:La nueva ra??z va a tener como hijo drcho al nodo desequilibrado 
        4??:El antiguo nodo desequilibrado va a tener como hijo drcho al antiguo hijo del actual nodo ra??z
        5??:Devuelvo la nueva ra??z para equilibrar el ??rbol 
        '''
    def rot_izq(self, node: BinaryNode) -> BinaryNode:
        nuevo_root = node.right
        aux = node.right.left
        node.right.left = node
        node.right = aux
        return nuevo_root

    #ROTACION DRCHA-IZQUIERDA#
    '''Es una compisici??n de las dos rotaciones previas, por lo que las llamamos para que realicen su funci??n'''
    def rot_der_izq(self, node:BinaryNode) -> BinaryNode:
        '''Ordeno una rotaci??n a drchas del hijo derecho del nodo desequilibrado, la cual me devuelve el nuevo nodo ra??z,
        el cual a ser el nuevo hijo drcho del nodo desequilibrado'''
        node.right = self.rot_der(node.right)
        '''Aplico una rotaci??n a izqdas sobre el nodo desequilibrado'''
        return self.rot_izq(node)

    #ROTACI??N IZQDA-DRCHA#
    def rot_izq_der(self, node:BinaryNode) -> BinaryNode:
        '''Ordeno una rotaci??n a izqdas del hijo izqdo del nodo desequilibrado, la cual me devuelve el nuevo nodo ra??z,
        el cual a ser el nuevo hijo izqdo del nodo desequilibrado'''
        node.left = self.rot_izq(node.left)
        '''Aplico una rotaci??n a drchas sobre el nodo desequilibrado'''
        return self.rot_der(node)

'''  
if _name_ == "_main_":
    arbol = AVLTree()
    for i in range(1, 10):
        arbol.insert(i)
    arbol.draw()
'''