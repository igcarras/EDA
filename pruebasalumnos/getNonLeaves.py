# -*- coding: utf-8 -*-

from Arbol_binario import BinaryNode
from Arbol_binario import BinaryTree


class BinarySearchTree(BinaryTree):

    def search(self, elem: object) -> BinaryNode:
        return self._search(self._root, elem)

    def _search(self, node: BinaryNode, elem: object) -> BinaryNode:
        if node is None or node.elem == elem:
            return node
        elif elem < node.elem:
            return self._search(node.left, elem)
        elif elem > node.elem:
            return self._search(node.right, elem)

    def insert(self, elem: object) -> None:
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:

        if node is None:
            return BinaryNode(elem)

        # No se admiten duplicados.
        if node.elem == elem:
            print('Error: elem already exist ', elem)
            return node

        if elem < node.elem:
            node.left = self._insert(node.left, elem)

        else:
            node.right = self._insert(node.right, elem)

        # Este "return" sirve para salir de todas las llamadas recursivas a partir del return BinaryNode(elem).
        return node

    def isFather(self, node: BinaryNode) -> bool:
        if node == None:
            return False
        elif node.right.elem or node.right.elem:
            return True
        return False

    def getNonLeaves(self):
        return self._getNonLeaves(self._root)

    def _getNonLeaves(self, node: BinaryNode, lista:[]):
        if node.right:
            if node.right.elem not in lista:
                if self.isFather(node.right):
                    return self._getNonLeaves(node.right)
        elif node.left:
            if (node.left.elem not in lista):
                if self.isFather(node.left):
                    return self._getNonLeaves(node.left)
        lista.append(node.elem)
        return lista


arbol = BinarySearchTree()

print("hola")
raiz=arbol._root
print(arbol.isFather(raiz))
arbol.insert(25)
arbol.insert(36)
arbol.insert(20)
arbol.insert(40)
arbol.insert(30)
arbol.insert(22)
arbol.insert(10)
arbol.insert(48)
arbol.insert(38)
arbol.insert(28)
arbol.insert(12)
arbol.insert(5)
raiz=arbol._root
print(arbol.isFather(raiz))

"""print(arbol.getNonLeaves())"""
