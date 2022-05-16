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
        then remove this node (using super()._remove). After this, the function has to balance the node returned by the function super()._remove"""
        node = super()._remove(node, elem)
        node = self._rebalance(node)

        return node

    #Rotación derecha
    def right_rotation(self,node: BinaryNode) -> BinaryNode:
        aux = node.elem
        aux2 = node.left.right
        aux3 = node.right
        node.elem = node.left.elem
        node.left = node.left.left
        node.right = BinaryNode(aux)
        node.right.left = aux2
        node.right.right = aux3
        return node

    #Rotación izquierda
    def left_rotation(self, node: BinaryNode) -> BinaryNode:
        aux = node.elem
        aux2 = node.right.left
        aux3 = node.left
        node.elem = node.right.elem
        node.right = node.right.right
        node.left = BinaryNode(aux)
        node.left.right = aux2
        node.left.left = aux3
        return node

    #Rotación izquierda-derecha
    def left_right_rotation(self, node: BinaryNode) -> BinaryNode:
        aux = node.left.right.right
        aux2 = node.left.right.left
        aux3 = node.left.left
        elem_l = node.left.elem
        elem_l_r = node.left.right.elem
        new_node = BinaryNode(elem_l)
        new_node.left = aux3
        new_node.right = aux2
        node.left.elem = elem_l_r
        node.left.right = aux
        node.left.left = new_node

        return self.right_rotation(node)

    #Rotación derecha-izquierda
    def right_left_rotation(self, node: BinaryNode) -> BinaryNode:
        aux = node.right.left.left
        aux2 = node.right.left.right
        aux3 = node.right.right
        elem_r = node.right.elem
        elem_r_l = node.right.left.elem
        new_node = BinaryNode(elem_r)
        new_node.right = aux3
        new_node.left = aux2
        node.right.elem = elem_r_l
        node.right.left = aux
        node.right.right = new_node

        return self.left_rotation(node)

    #Método que evalua si un nodo está equilibrado en avl. Si no lo está aplica la rotación correspondiente
    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        """ gets node and balances it"""
        if not node:
            return node
        else:
            balance = abs(self._height(node.left) - self._height(node.right))
            if balance < 2:
                return node
            else:
                if self._height(node.left) > self._height(node.right) and self._height(node.left.left) >= self._height(
                        node.left.right):
                    return self.right_rotation(node)

                elif self._height(node.right) > self._height(node.left) and self._height(
                        node.right.right) >= self._height(node.right.left):
                    return self.left_rotation(node)

                elif self._height(node.left) > self._height(node.right) and self._height(
                        node.left.right) > self._height(node.left.left):
                    return self.left_right_rotation(node)
                elif self._height(node.right) > self._height(node.left) and self._height(
                        node.right.left) > self._height(node.right.right):
                    return self.right_left_rotation(node)


