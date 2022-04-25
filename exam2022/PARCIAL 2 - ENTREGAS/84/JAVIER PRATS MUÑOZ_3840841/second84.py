# -*- coding: utf-8 -*-

# JAVIER PRATS MUÑOZ. GRUPO 84.

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
        aux = []
        removed_leaves = []
        # La lista "aux" se rellenará gracias al método "leaflist".
        self.leaf_list(self._root, aux)
        # Vamos mirando, uno por uno, los elementos que componen dicha lista. Si no están en el rango establecido, se
        # agregarán a la lista "removed_leaves", en la cual se encontrarán los nodos que finalmente eliminaremos.
        for i in aux:
            if i < min or i > max:
                removed_leaves.append(i)
        # Eliminamos los nodos cuyos elementos se encuentren en la lista "removed_leaves".
        for j in removed_leaves:
            self.removeleaf(j)
        return removed_leaves

    # Método auxiliar que construye una lista ordenada de forma ascendente (porque recorremos el árbol de forma
    # "inorder") y que está compuesta por los elementos de los nodos hoja que hay al principio de la ejecución.
    def leaf_list(self, node: BinaryNode, aux: list) -> None:
        if node is not None:
            self.leaf_list(node.left, aux)
            if (not node.left) and (not node.right):
                aux.append(node.elem)
            self.leaf_list(node.right, aux)

    # Método que se apoya en "_removeleaf". Elimina el elemento que pasemos por parámetro del árbol. Este elemento,
    # cabe destacar, está alojado en un nodo hoja.
    def removeleaf(self, elem: int) -> object:
        return self._removeleaf(self._root, elem)

    def _removeleaf(self, node: BinaryNode, elem: int) -> object:
        if node.elem is elem:
            return None
        if elem < node.elem:
            node.left = self._removeleaf(node.left, elem)
        if elem > node.elem:
            node.right = self._removeleaf(node.right, elem)
        return node

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
