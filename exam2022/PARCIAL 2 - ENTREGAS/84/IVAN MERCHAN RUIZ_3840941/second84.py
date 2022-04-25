# -*- coding: utf-8 -*-
# Iván Merchán ruiz
# NIA: 100451135

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

    # Dado que está permitido implementar funciones auxiliares, implementaré la función 'find' y 'NumChild'
    # empleando recursividad

    def find(self,key):
        return self._find(self._root,key)
    def _find(self,node,key):
        if node.key == key:
            return node
        if key < node.key:
            return self._find(node.left,key)
        if key > node.key:
            return self._find(node.right,key)
    # Al final no la empleé

    def NumChild(self):
        node = self._root
        return _NumChild(self,node)
    def _NumChild(self,node):
        if node == None or (node.left == None and node.right == None):
            return 0
        if node.left != None and node.right != None:
            return 2
        return 1

    # Removes all leaf nodes having value outside the given range
    # returns a sorted list in ascending order
    def removeOutsideRange(self, min: int, max: int) -> []:
        node = self._root
        return _removeOutsideRange(self,min,max,node)
    def _removeOutsideRange(self, min:int, max:int, node):
        resultado = []
        sucesor = node.right
        while node:
            node = node.left
        if node.elem > max or node.elem < min:
            resultado.append(node.elem)
            node.key = None
            node.elem = None
        else:
            node = sucesor
            return self._removeOutsideRange(min,max,node)
        for n in range(1,len(resultado)):
            for i in range(len(resultado)-n):
                if resultado[i] > resultado[i+1]:
                    x = resultado[i]
                    resultado[i] = resultado[i+1]
                    resultado[i+1] = x
        return resultado

    # La complejidad del método es O(n^2) ya que solo hay un bucle anidado
    # Soy consciente de que da error en algunos nodos del árbol por un fallo en el algoritmo de recorrido para
    # cada recurrencia, pero tras varios intentos no he podido encontrar la solución y no dispongo del tiempo suficiente.


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
