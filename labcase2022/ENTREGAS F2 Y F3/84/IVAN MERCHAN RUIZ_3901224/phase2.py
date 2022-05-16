'''
FASE 2
Nombre1: Iván Merchán Ruiz
NIA1:100451135
Nombre2: Rubén Zorrilla
NIA2:100451173
'''

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

    def _rebalance(self, node):
        if node:
            if abs(self.equilibrado(node.elem)) >= 2:
                # equilibrado mismo signo
                if self.equilibrado(node.elem) <= -2 and\
                        self.equilibrado(node.right.elem) <= 0:
                    self.rotar_izquierda(node)
                elif self.equilibrado(node.elem) >= 2 and\
                        self.equilibrado(node.left.elem) >= 0:
                    self.rotar_derecha(node)
                # si equilibrado  tienen signo opuesto)
                elif self.equilibrado(node.elem) >= 2 and\
                        self.equilibrado(node.left.elem) <= 0:
                    self.rotar_izquierda(node.left)
                    self.rotar_derecha(node)
                elif self.equilibrado(node.elem) <= -2 and \
                        self.equilibrado(node.right.elem) >= 0:
                    self.rotar_derecha(node.right)
                    self.rotar_izquierda(node)
                # si el no no es self._root, se pasa al anterior
                if not node == self._root:
                    node = self.anterior(node.elem)
        return node

    # La complejidad es O(1) ya que no contiene bucles.
    # El mejor caso es que no exista el árbol o  que tenga pocos elementos.
    # El peor caso es cuando es muy grande o está muy desbalanceado
#
    '''Funciones AUXILIARES'''

    def rotar_izquierda(self, node):
        # declaramos las variables que usaremos para rotar los elementos
        anterior= self.anterior(node.elem)
        arbol2 = AVLTree()
        arbol2._root = node.right
        aux_node = node.right.left
        node.right.left = node
        node.right = aux_node
        # si no existe anterior
        if not anterior:
            self._root = arbol2._root
        else:
            if arbol2.anterior(node.elem).elem > anterior.elem:
                anterior.right = arbol2.anterior(node.elem)
            elif arbol2.anterior(node.elem).elem < anterior.elem:
                anterior.left = arbol2.anterior(node.elem)

    def rotar_derecha(self, node):
        # declaramos las variables que usaremos para rotar los elementos
        anterior = self.anterior(node.elem)
        auxiliar = node.left.right
        arbol2 = AVLTree()
        arbol2._root = node.left
        node.left.right = node
        node.left = auxiliar

        if not anterior:
            self._root = arbol2._root
        else:
            if anterior.elem < arbol2.anterior(node.elem).elem:
                anterior.right = arbol2.anterior(node.elem)
            elif anterior.elem > arbol2.anterior(node.elem).elem:
                anterior.left = arbol2.anterior(node.elem)

    def anterior(self, elem):
        # Devuelve el nodo previo a elem
        return self._anterior(self._root, elem)

    def _anterior(self, node, elem) :
        # esta funcion nos ayuda  a encontrar el anterior
        if (node.elem > elem == node.left.elem) \
                or (node.elem < elem == node.right.elem):
            return node
        # Recursion con el siguiente
        elif node.elem > elem:
            return self._anterior(node.left,
                                  elem)
        elif node.elem < elem:
            return self._anterior(node.right,
                                  elem)

    def equilibrado(self, elem) -> int:
        # devuelve un int, que es un factor de equilibrio entre izq y derecha
        node = self.search(elem)
        if node:
            return self._height(node.left) - self._height(node.right)
        else:
            return 0