# -*- coding: utf-8 -*-
"""BEATRIZ VILLACORTA LLORENTE"""
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
        #caso base, si root es none
        if self._root == None:
            return []

        return self._removeOutsideRange(self._root, min, max)

    def _removeOutsideRange(self, node, min, max):
        #creo la lista que tengo que devolver
        newList = []

        #si hay nodo siguiente (no es hoja)
        if node.left or node.right:
            if node.left:
                #recorro los siguientes
                recorrer = self._removeOutsideRange(node.left, min, max)
                #si es hoja elimino el siguiente
                if len(recorrer) > 0:
                    node.left = None
                for i in recorrer:
                    newList.append(i)
        #recorro por la derecha
            if node.right:
                recorrer = self._removeOutsideRange(node.right, min, max)
                if len(recorrer) > 0:
                    node.right = None
                for i in recorrer:
                    #añado a la nueva lista
                    newList.append(i)
        else:
            if not min <= node.elem <= max:
                newList.append(node.elem)

        return newList
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
