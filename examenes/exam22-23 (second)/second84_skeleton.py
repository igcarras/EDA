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

    # Sum value of all nodes (NOT LEAF) having value inside the given range
    # return integer with sum values
    def sumInsideRange (self, min: int, max: int) -> int:
        return self._sumInsideRange(self._root, min, max, 0)


    # Sum value of all nodes (NOT LEAF) having value inside the given range
    def _sumInsideRange (self, node: BinaryNode, min: int, max: int, suma:int) -> int:
        pass



if __name__ == "__main__":

    # tree with several nodes
    tree = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        tree.insert(x)

    print("Original Tree")
    tree.draw()

    print("Sum not leaf nodes out range: 1, 1")
    print("Result ", tree.sumInsideRange(1,1))
    print("Sum not leaf nodes out range: 15, 20")
    print("Result ", tree.sumInsideRange(15,20))
    print("Sum not leaf nodes out range: 50, 80")
    print("Result ", tree.sumInsideRange(50, 80))
    print("Sum not leaf nodes out range: 5, 20")
    print("Result ", tree.sumInsideRange(5, 20))
    print("Sum not leaf nodes out range: 1, 200")
    print("Result ", tree.sumInsideRange(1, 200))

    #empty tree
    tree = MyBinarySearchTree()
    print("Sum not leaf nodes out range: 15, 20")
    print("Result ", tree.sumInsideRange(15,20))

    #tree with one node
    tree = MyBinarySearchTree()
    tree.insert(4)
    print("Tree: Sum not leaf nodes out range: 15, 20")
    print("Result ", tree.sumInsideRange(15, 20))
    print("Tree: Sum not leaf nodes out range: 5, 40")
    print("Result ", tree.sumInsideRange(5, 40))

    # tree with several nodes (statement example)
    tree = MyBinarySearchTree()
    for x in [46, 11, 5, 20, 81, 51, 56, 94]:
        tree.insert(x)

    print("Original Tree")
    tree.draw()

    print("Tree: Sum not leaf nodes out range: 1, 120")
    print("Result ", tree.sumInsideRange(1, 120))
    print("Tree: Sum not leaf nodes out range: 10, 20")
    print("Result ", tree.sumInsideRange(10, 20))
    print("Tree: Sum not leaf nodes out range: 0, 0")
    print("Result ", tree.sumInsideRange(0, 0))
    print("Tree: Sum not leaf nodes out range: 12, 93")
    print("Result ", tree.sumInsideRange(12, 93))
    print("Tree: Sum not leaf nodes out range: -10, 0")
    print("Result ", tree.sumInsideRange(-10, 0))
    print("Tree: Sum not leaf nodes out range: 5, 80")
    print("Result ", tree.sumInsideRange(5, 80))
    print("Tree: Sum not leaf nodes out range: 46, 94")
    print("Result ", tree.sumInsideRange(46, 94))