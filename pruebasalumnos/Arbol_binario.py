# -*- coding: utf-8 -*-

# Implementación de un Árbol Binario.
# Los nodos únicamente apuntan a sus hijos. A sus padres no.

from Lista_simplemente_enlazada import SList


class BinaryNode:

    def __init__(self, elem: object, node_left: 'BinaryNode' = None, node_right: 'BinaryNode' = None) -> None:
        self.elem = elem
        self.left = node_left
        self.right = node_right

    # Método que dice si dos nodos son iguales.

    def __eq__(self, other: 'BinaryNode') -> bool:
        return other is not None and self.elem == other.elem and self.left == other.left and self.right == other.right

    # Método que imprime el elemento de un nodo.

    def __str__(self):
        return str(self.elem)


class BinaryTree:

    def __init__(self) -> None:
        self._root = None

    # Método que dice si dos árboles son iguales.

    def __eq__(self, other: 'BinaryTree') -> bool:
        return other is not None and self._root == other._root

    # Método que dice el tamaño del árbol.

    def size(self) -> int:
        return self._size(self._root)

    # Submétodo que dice el tamaño de un subárbol.

    def _size(self, node: BinaryNode) -> int:
        if node is None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)

    # Método que dice la altura del árbol.

    def height(self) -> int:
        return self._height(self._root)

    # Submétodo que dice la altura de un subárbol.

    def _height(self, node: BinaryNode) -> int:
        if node is None:
            return -1
        else:
            return 1 + max(self._height(node.left), self._height(node.right))

    # MÉTODOS PARA RECORRER EL ÁRBOL.

    def preorder(self) -> None:
        print('Preorder: ', end=' ')
        self._preorder(self._root)
        print()

    def _preorder(self, node: BinaryNode) -> None:
        if node is not None:
            print(node.elem, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self) -> None:
        print('Postorder: ', end=' ')
        self._postorder(self._root)
        print()

    def _postorder(self, node: BinaryNode) -> None:
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.elem, end=' ')

    def inorder(self) -> None:
        print('Inorder: ', end=' ')
        self._inorder(self._root)
        print()

    def _inorder(self, node: BinaryNode) -> None:
        if node is not None:
            self._inorder(node.left)
            print(node.elem, end=' ')
            self._inorder(node.right)

    def level_order(self) -> None:
        if self._root is None:
            print('tree is empty')
        else:
            print("Level order: ", end=' ')

            list_nodes = SList()
            list_nodes.addLast(self._root)
            while len(list_nodes) > 0:
                current = list_nodes.removeFirst()
                print(current.elem, end=' ')
                if current.left is not None:
                    list_nodes.addLast(current.left)
                if current.right is not None:
                    list_nodes.addLast(current.right)

            print()

    def depth(self, node):
        depth_level = None

        if self._root is None:
            print('Error: the tree is empty')
        else:
            depth_level = 0

            list_nodes = SList()
            list_nodes.addLast(self._root)

            while len(list_nodes) > 0:
                current = list_nodes.removeFirst()
                if current == node:
                    return depth_level
                if current.left is not None:
                    list_nodes.addLast(current.left)
                if current.right is not None:
                    list_nodes.addLast(current.right)
                depth_level += 1

        print('Not found ', node.elem)
        return None

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


if __name__ == '__main__':
    tree = BinaryTree()

    newNode = BinaryNode(2)
    left = BinaryNode(3, newNode, None)

    right = BinaryNode(9)

    right.left = BinaryNode(8)
    right.right = BinaryNode(20)
    rrNode = right.right
    rrNode.right = BinaryNode(30)

    root = BinaryNode(5, left, right)

    tree._root = root
    tree.draw()

    print('Size of the tree:', tree.size())
    print('Height of the tree:', tree.height())
    print('root of the tree:', tree._height(root))

    tree.preorder()
    tree.postorder()
    tree.inorder()

    print('depth of root:', tree.depth(root))
    print('depth of root.left:', tree.depth(left))
    print('depth of root.right:', tree.depth(right))
