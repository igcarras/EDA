# -*- coding: utf-8 -*-


class BinaryNode:

    def __init__(self, elem: object, node_left: 'BinaryNode' = None, node_right: 'BinaryNode' = None) -> None:
        self.elem = elem
        self.left = node_left
        self.right = node_right

    def __str__(self):
        return str(self.elem)

class BinaryTree:
    def __init__(self) -> None:
        """creates an empty binary tree"""
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

    def right_sum(self) -> int:
        # Define a variable to track current level
        self._currentLevel = 0
        return self._right_sum_recursive(self._root, self._currentLevel + 1)

    def _right_sum_recursive(self, node, level):
        if not node:
            return 0
        print("Estoy en el nodo", node.elem)
        sum = 0
        # If we detect a level change
        print("Estoy buscando en el nivel", level, "y en el arbol estoy en el nivel ", self._currentLevel)
        if self._currentLevel < level:
            # We accumulate item value to the sum
            sum += node.elem
            # We update current level to keep going
            self._currentLevel = level
            print("Suma es:", sum, "y bajo un nivel en el arbol hasta el nivel ", self._currentLevel)


        # Recursion: right first since we want to sum last items of each level only
        sum += self._right_sum_recursive(node.right, level + 1)
        sum += self._right_sum_recursive(node.left, level + 1)
        return sum

if __name__ == "__main__":
    input_tree = BinaryTree()
    values = [25, 20, 36, 10, 22, 30, 40, 5, 12, 28, 38]
    for x in values:
        input_tree.insert(x)
    input_tree.draw()

    print("La suma final aculumada es ", input_tree.right_sum())