# -*- coding: utf-8 -*-
"Pablo Albendea Obispo"

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

  # Removes all leaf nodes having value inside the given range
  # returns a sorted list in descending order
    listanodoshoja = []
    def removeInsideRange(self, min: int, max: int, listanodoshoja= listanodoshoja) -> []:
        if self._root:
            if not self._root.right and not self._root.left:
                if self._root.elem < max and self._root.elem > min:
                    listanodoshoja.append(self._root.elem)
                    self._root= None
                    return listanodoshoja
                else:
                    return self._removeInsideRange(self._root, min, max, listanodoshoja)
    def _removeInsideRange(self, node, min, max, listanodoshoja):
        if node:
            if max == min:
                if max > node.elem:
                    if max == node.right.elem and not (node.right.right or node.right.left):
                        listanodoshoja.append(node.right.elem)
                        node.right = None
                        return listanodoshoja
                    else:
                        return self._removeInsideRange(node.right, min, max, listanodoshoja)
                if max < node.elem:
                    if max == node.left.elem and not (node.left.right or node.left.left):
                        listanodoshoja.append(node.left.elem)
                        node.left = None
                        return listanodoshoja
                    else:
                        return self._removeInsideRange(node.right, min, max, listanodoshoja)
            if not (node.right.right or node.right.left):
                if node.right.elem < max and node.right.elem > min:
                    listanodoshoja.append(node.right.elem)
                    node.right = None
            if not (node.left.right or node.left.left):
                if node.left.elem < max and node.left.elem > min:
                    listanodoshoja.append(node.left.elem)
                    node.right = None
            if node.right.left or node.right.right:
                return self._removeInsideRange(node.right, min, max, listanodoshoja)
            if node.left.left or node.left.right:
                return self._removeInsideRange(node.left, min, max, listanodoshoja)
        else:
            return listanodoshoja







if __name__ == "__main__":

    aux = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux.insert(x)
    print("Original Tree")
    aux.draw()

    print("Remove leaf nodes in range: 1, 120")
    print("Nodes removed", aux.removeInsideRange(1,120))

    aux2 = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux2.insert(x)


    print("Remove leaf nodes in range: 15, 20")
    print("Nodes removed", aux2.removeInsideRange(15,20))

    aux3 = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux3.insert(x)


    print("Remove leaf nodes in range: 0, 0")
    print("Nodes removed", aux3.removeInsideRange(0,0))

    aux4 = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux4.insert(x)


    print("Remove leaf nodes in range: 54, 80")
    print("Nodes removed", aux4.removeInsideRange(54,80))

    aux5 = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux5.insert(x)

    print("Remove leaf nodes in range: -10, 0")
    print("Nodes removed", aux4.removeInsideRange(-10,0))