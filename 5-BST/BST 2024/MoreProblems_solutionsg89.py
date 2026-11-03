from bst import BinarySearchTree
from bintree import BinaryNode
    
class BT(BinarySearchTree):

    def removeNodeMultiple(self) -> list:
        removelist = []

        if self._root is None:
            return removelist

        multiple = self._root.elem
        self._root = self._removeNodeMultiple(self._root, multiple, removelist)
        return removelist

    def _removeNodeMultiple(self, node: BinaryNode,
                            multiple: int, removelist: list) -> object:
        if node is None:
            return None
        # Only check nodes that are originally leaves
        if node.left is None and node.right is None:
            if ((multiple != 0 and node.elem % multiple == 0)
                    or (node.elem != 0 and multiple % node.elem == 0)
                    or (multiple == 0 and node.elem == 0)):
                removelist.append(node.elem)
                return None
        else:
            # Right subtree first to obtain descending order
            node.right = self._removeNodeMultiple(node.right, multiple, removelist)
            node.left = self._removeNodeMultiple(node.left, multiple, removelist)
        return node

    def secondLargest(self):
        result = []
        self._secondLargest(self._root, result)

        if len(result) < 2:
            return -1

        return result[1]

    def _secondLargest(self, node, result):

        if node is None or len(result) >= 2:
            return

        # Visit right subtree
        self._secondLargest(node.right, result)

        if len(result) >= 2:
            return

        # Visit current node
        result.append(node.elem)

        if len(result) >= 2:
            return

        # Visit left subtree
        self._secondLargest(node.left, result)


tree =BT()
values = [25, 20, 36, 10, 22, 30, 40, 5, 12, 28, 38, 48]
for x in values:
   tree.insert(x)
tree.draw()

print(tree.removeNodeMultiple())
print(tree.secondLargest())


