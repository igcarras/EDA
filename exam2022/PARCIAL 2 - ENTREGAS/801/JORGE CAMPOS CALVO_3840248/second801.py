# -*- coding: utf-8 -*-

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
    def removeInsideRange(self, min: int, max: int) -> []:
        result = []
        self._removeInsideRange(self._root, min, max, result)
        return result
    def _removeInsideRange(self, node:BinaryNode, min:int, max:int, lst_leaves: list)-> None:
        if node!=None:
            self._removeInsideRange(node.right, min, max, lst_leaves)
            if node.left==None and node.right==None:
                if node.elem >= min and node.elem <= max:
                    lst_leaves.append(node.elem)
                    return None
            self._removeInsideRange(node.left, min, max, lst_leaves)


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