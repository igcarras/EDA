# -*- coding: utf-8 -*-
# David Serrano Sangrador
class BinaryNode:
    def __init__(self, elem: int, node_left: 'BinaryNode' = None, node_right: 'BinaryNode' = None) -> None:
        self.elem = elem
        self.left = node_left
        self.right = node_right


class MyBinarySearchTree:
    def __init__(self) -> None:
        """creates an empty binary tree
        I only has an attribute: _root"""
        self._root = None

    def draw(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n\n')

    def _draw(self, prefix: str, node: BinaryNode, is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)


    def insert(self, elem: object) -> None:
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        if node is None:
            return BinaryNode(elem)

        if node.elem == elem:
            print('Error: elem already exist ', elem)
            return node

        if elem < node.elem:
            node.left = self._insert(node.left, elem)
        else:
            # elem>node.elem
            node.right = self._insert(node.right, elem)
        return node

    # Removes all leaf nodes having value outside the given range
    # returns a sorted list in ascending order
    def removeOutsideRange(self, min: int, max: int) -> []:
        lista = []
        if self._root == None:                            # si el arbol está vacio
            return []
        maspequeno = self.elementoMasPequeno()
        masgrande = self.elementoMasGrande()
        if min <= maspequeno and masgrande <= max:        # si el intervalo es mayor que los elementos mas grandes y pequeños, no devuelve nada porque no elimina nada
            return []
        if self._root.left == None and self._root.right == None and not (min <= self._root.elem <= max):  # si el arbol solo tiene un nodo y se elimina
            return [self._root.elem]
        # vamos a sacar el elemento más pequeño del arbol
        return self._removeOutsideRange(min, max, self._root, lista)
    def _removeOutsideRange(self, min, max, node, lista) -> []:          # los nodos se tienen que eliminar desde el padre, por tanto:
        if node.left.left != None and node.left.right != None:
            self._removeOutsideRange(min, max, node.left, lista)
        if node.right.left != None and node.right.right != None:
            self._removeOutsideRange(min, max, node.right, lista)
        if node.left.left == None and node.left.right == None and not (min <= node.left.elem <= max):    # si el nodo izquierdo es una hoja y
            lista.append(node.left.elem)
            node.left = None
        if node.right.left == None and node.right.right == None and not (min <= node.right.elem <= max):
            lista.append(node.right.elem)
            node.right = None
        return lista

    def elementoMasPequeno(self):
        return self._elementoMasPequeno(self._root)
    def _elementoMasPequeno(self, node):
        if node.left == None:
            return node.elem
        else:
            return self._elementoMasPequeno(node.left)

    def elementoMasGrande(self):
        return self._elementoMasGrande(self._root)
    def _elementoMasGrande(self, node):
        if node.right == None:
            return node.elem
        else:
            return self._elementoMasGrande(node.right)

if __name__ == "__main__":
    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)

    print("Original Tree")
    tree.draw()

    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)
    print("Remove leaf nodes out range: 1, 120")
    print("Nodes removed", tree.removeOutsideRange(1,120))
    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)
    print("Remove leaf nodes out range: 15, 20")
    print("Nodes removed", tree.removeOutsideRange(15,20))
    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)
    print("Remove leaf nodes out range: 0, 0")
    print("Nodes removed", tree.removeOutsideRange(0,0))
    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)
    print("Remove leaf nodes out range: 9, 23")
    print("Nodes removed", tree.removeOutsideRange(9, 23))
    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)
    print("Remove leaf nodes out range: -10, 0")
    print("Nodes removed", tree.removeOutsideRange(-10, 0))
    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)
    print("Remove leaf nodes out range: 5, 80")
    print("Nodes removed", tree.removeOutsideRange(5, 80))
