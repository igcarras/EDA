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

    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        """función para obtener un arbol balanceado"""

        if node and abs(self.height_eq(node.elem)) >= 2:

            # Codigo de ayuda para ver lo que pasa
            """print("Equilibrar:", node.elem)"""

            # rotaciones simples
            #hay que rotar a la izquierda
            if self.height_eq(node.elem) <= -2 and self.height_eq(node.right.elem) <= 0:
                self.left_rotation(node)
            #hay que rotar a la derecha
            elif self.height_eq(node.elem) >= 2 and self.height_eq(node.left.elem) >= 0:
                self.right_rotation(node)

            # rotaciones compuestas (los dos factores de equilibrio tienen signo opuesto)
            elif self.height_eq(node.elem) >= 2 and self.height_eq(node.left.elem) <= 0:
                self.left_rotation(node.left)
                self.right_rotation(node)
            elif self.height_eq(node.elem) <= -2 and self.height_eq(node.right.elem) >= 0:
                self.right_rotation(node.right)
                self.left_rotation(node)

            #actualiza el nodo
            if not node == self._root:
                node = self.prev_node(node.elem)

        # Codigo de ayuda para ver lo que pasa
        """print("\tRevisando nodo:", node)"""
        """self.draw()"""
        return node

    def height_eq(self, elem: object) -> int:
        """calcula equilibrio en altura de un elemento
        si es positivo, el lado izquierdo pesa más
        si es negativo, el lado derecho pesa más"""
        #busco donde se encuentra el nodo
        node = self.search(elem)
        if node==None:
            return 0
        else:
            return self._height(node.left) - self._height(node.right)

    def right_rotation(self, node: BinaryNode):
        # Rotacion simple hacia la derecha
        node_prev = self.prev_node(node.elem)
        #cambios en el subarbol
        nodeIt = node.left.right
        sub_tree = AVLTree()
        sub_tree._root = node.left
        node.left.right = node
        node.left = nodeIt

        # Se conecta node_prev con el subarbol
        if node_prev:
            if node_prev.elem < sub_tree.prev_node(node.elem).elem:
                node_prev.right = sub_tree.prev_node(node.elem)
            elif node_prev.elem > sub_tree.prev_node(node.elem).elem:
                node_prev.left = sub_tree.prev_node(node.elem)

        else:
            self._root = sub_tree._root

    def left_rotation(self, node: BinaryNode):
        # Rotacion simple hacia la izquierda

        # Nodo que se conecta al subarbol
        node_prev = self.prev_node(node.elem)

        # Se realizan los cambios en el subarbol
        sub_tree = AVLTree()
        sub_tree._root = node.right
        nodeIt = node.right.left
        node.right.left = node
        node.right = nodeIt

        # Se conecta node_prev con el subarbol
        if node_prev:
            if node_prev.elem < sub_tree.prev_node(node.elem).elem:
                node_prev.right = sub_tree.prev_node(node.elem)
            elif node_prev.elem > sub_tree.prev_node(node.elem).elem:
                node_prev.left = sub_tree.prev_node(node.elem)

        #cuando la raiz del arbol es tambíen la del sub arbol
        else:
            self._root = sub_tree._root


    def prev_node(self, elem: object) -> BinaryNode:
        # nodo anterior a elem
        return self._prev_node(self._root, elem)

    def _prev_node(self, node: BinaryNode, elem: object) -> BinaryNode:
        # Funcion recursiva

        # Caso base
        if (node.elem > elem == node.left.elem) or (node.elem < elem == node.right.elem):
            return node
        # Caso recursivo
        elif elem < node.elem:
            return self._prev_node(node.left, elem)
        elif elem > node.elem:
            return self._prev_node(node.right, elem)




tree = AVLTree()
# insert
for x in [8, 50, 49, 90, 101, 82, 78, 13, 5, 17, 120, 47, 84, 16, 54, 38, 99]:
    print('#input tree:', x)
    tree.insert(x)
    tree.draw()
# remove
for x in [50, 49, 38]:
    print('#output tree:', x)
    tree.remove(x)
    tree.draw()
