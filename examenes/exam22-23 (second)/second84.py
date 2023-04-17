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

    # Removes all nodes having value outside the given range
    # returns a sorted list in ascending order
    def sumInsideRange (self, min: int, max: int) -> int:
        return self._sumInsideRange(self._root, min, max, 0)


    # Removes all nodes having value outside the given range
    def _sumInsideRange (self, node: BinaryNode, min: int, max: int, sum:int) -> int:
        # Base Case
        if node is None:
            return 0

        sum += self._sumInsideRange(node.left, min, max,  sum)
        sum += self._sumInsideRange(node.right, min, max,  sum)

        if (node.left is None) and (node.right is None):
            # node is a leave
             return 0
        # check is node is not leaf and elem is in range
        if (node.elem >= min and node.elem <= max):
            print("Sumo el valor ", node.elem)
            return node.elem
        else:
            return 0


if __name__ == "__main__":
    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)

    print("Original Tree")
    tree.draw()

    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)
    print("Sum not leaf nodes out range: 1, 1")
    print("Result ", tree.sumInsideRange(1,1))
    print("Sum not leaf nodes out range: 15, 20")
    print("Result ", tree.sumInsideRange(15,20))



    # tree = MyBinarySearchTree()
    # for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
    #     tree.insert(x)
    # print("Sum not leaf nodes out range: 15, 20")
    # print("Result ", tree.sumInsideRange(15,20))
    # tree = MyBinarySearchTree()
    # for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
    #     tree.insert(x)
    # print("Sum not leaf nodes out range: 0, 0")
    # print("Result ", tree.sumInsideRange(0,0))
    # tree = MyBinarySearchTree()
    # for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
    #     tree.insert(x)
    # print("Sum not leaf nodes out range: 9, 23")
    # print("Result ", tree.sumInsideRange(9, 23))
    # tree = MyBinarySearchTree()
    # for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
    #     tree.insert(x)
    # print("Sum not leaf nodes out range: -10, 0")
    # print("Result ", tree.sumInsideRange(-10, 0))
    # tree = MyBinarySearchTree()
    # for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
    #     tree.insert(x)
    # print("Sum not leaf nodes out range: 5, 80")
    # print("Result ", tree.sumInsideRange(5, 80))
