# -*- coding: utf-8 -*-

from bintree import BinaryNode
from bintree import BinaryTree

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

    # Método para hallar el sucesor de un nodo (el nodo cuyo elemento es el menor del subárbol derecho).
    def _minimum_node(self, node: BinaryNode) -> BinaryNode:
        min_node = node
        while min_node.left is not None:
            min_node = min_node.left
        return min_node

    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:

        if node is None:
            print(elem, ' not found')
            return node

        if elem < node.elem:
            node.left = self._remove(node.left, elem)

        elif elem > node.elem:
            node.right = self._remove(node.right, elem)

        # Cuando encontremos el nodo que queremos eliminar...
        else:

            # CASO 1: NODO HOJA. Simplemente devolvemos "None" y así rompemos la conexión de dicho nodo con su padre.
            if node.left is None and node.right is None:
                return None

            # CASO 2: NODO CON UN HIJO. Devolvemos su hijo. Así, puenteamos el nodo.
            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            # CASO 3: NODO CON DOS HIJOS. Sustituimos el nodo que queremos eliminar por su sucesor y eliminamos el
            # duplicado de dicho sucesor del subárbol derecho del nodo.
            else:
                successor = self._minimum_node(node.right)
                node.elem = successor.elem
                node.right = self._remove(node.right, successor.elem)

        return node

    # EJERCICIOS

    # NODO MÍNIMO.
    def nodo_minimo(self, nodo: BinaryNode) -> BinaryNode:
        nodo_min = nodo
        while nodo_min.left is not None:
            nodo_min = nodo_min.left
        return nodo_min

    # NODO MÁXIMO.
    def nodo_maximo(self, nodo: BinaryNode) -> BinaryNode:
        nodo_max = nodo
        while nodo_max.right is not None:
            nodo_max = nodo_max.right
        return nodo_max

    # SUMA DE LOS ELEMENTOS DEL ÁRBOL.
    def suma_total(self, nodo: BinaryNode) -> int:
        suma = 0
        if nodo is not None:
            suma += nodo.elem
            self.suma_total(nodo.left)
            self.suma_total(nodo.right)
        return suma

    # FACTOR DE EQUILIBRIO.
    def factor_equilibrio(self, nodo: BinaryNode) -> int:
        factor = (self._height(nodo.left)) - (self._height(nodo.right))
        if factor < 0:
            factor = -1 * factor
        return factor

    # K’th Largest Element in BST when modification to BST is not allowed.
    def _numeroGrandeK(self, node: BinaryNode, k: int, c: int):
        if (node is None) or c >= k:
            return
        self._numeroGrandeK(node.right, k, c)
        c += 1
        if c == k:
            print("K'th largest element is", node.elem)
            return
        self._numeroGrandeK(node.left, k, c)

    def numeroGrandeK(self, k):
        c = 0
        self._numeroGrandeK(self._root, k, c)

tree = BinarySearchTree()

tree.insert(20)
tree.insert(22)
tree.insert(8)
tree.insert(12)
tree.insert(4)
tree.insert(14)
tree.insert(10)

tree.draw()

tree.numeroGrandeK(3)
