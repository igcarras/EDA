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
    def removeNodeMultiple(self) -> []:
        removelist = []
        self._removeNodeMultiple(self._root, self._root.elem, removelist)
        return removelist

    # Removes all nodes having value inside the given range
    def _removeNodeMultiple(self, node: BinaryNode, multiple: int, removelist: []) -> object:
        # Base Case
        if node is None:
            return None

        # check is node is not leaf
        if node.left or node.right:
            node.right = self._removeNodeMultiple(node.right, multiple, removelist)
            node.left = self._removeNodeMultiple(node.left, multiple, removelist)

        else:
            if (node.left is None) and (node.right is None) and ((node.elem % multiple == 0) or (multiple % node.elem == 0)):
                # node is a leave
                # append node in list
                # print("leaf node for removing:", node.elem)
                removelist.append(node.elem)
                return None

        # if node is not leaf, return node and continue recursion
        return node



if __name__ == "__main__":

    aux = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux.insert(x)
    print("Original Tree 1")
    aux.draw()

    print("Remove leaf nodes multiple of", aux._root.elem)
    lista=aux.removeNodeMultiple()
    print("Nodes removed in Tree 1", lista)
    aux.draw()
    print("------------------------------------------------------------")

    aux = MyBinarySearchTree()
    for x in [50, 55, 54, 15, 60, 18, 10, 5, 25, 75, 100]:
        aux.insert(x)
    print("Original Tree 2")
    aux.draw()

    print("Remove leaf nodes multiple of", aux._root.elem)
    lista = aux.removeNodeMultiple()
    print("Nodes removed in Tree 2", lista)
    aux.draw()
    print("------------------------------------------------------------")

    aux = MyBinarySearchTree()
    for x in [40, 55, 54, 30, 60, 10, 1, 20, 75, 80]:
        aux.insert(x)
    print("Original Tree 3")
    aux.draw()

    print("Remove leaf nodes multiple of", aux._root.elem)
    lista = aux.removeNodeMultiple()
    print("Nodes removed", lista)
    aux.draw()
    print("------------------------------------------------------------")

    aux = MyBinarySearchTree()
    for x in [20, 8, 6, 10, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux.insert(x)
    print("Original Tree 4")
    aux.draw()

    print("Remove leaf nodes multiple of", aux._root.elem)
    lista = aux.removeNodeMultiple()
    print("Nodes removed", lista)
    aux.draw()
    print("------------------------------------------------------------")



    aux = MyBinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux.insert(x)
    print("Original Tree 5")
    aux.draw()

    print("Remove leaf nodes multiple of", aux._root.elem)
    lista = aux.removeNodeMultiple()
    print("Nodes removed", lista)
    aux.draw()
    print("------------------------------------------------------------")

    aux = MyBinarySearchTree()
    for x in [5,10,15]:
        aux.insert(x)
    print("Original Tree 6")
    aux.draw()

    print("Remove leaf nodes multiple of", aux._root.elem)
    lista = aux.removeNodeMultiple()
    print("Nodes removed", lista)
    aux.draw()
    print("------------------------------------------------------------")


