# from binarysearchtree import BinarySearchTree
from bst import BinarySearchTree
from bst import BinaryNode

class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        """gets a node, searches the place to insert a new node with element e (using super()._insert),  and then,
        the function has to balance the node returned by the function super.()_insert"""
        node = super()._insert(node, elem)
        if self.factor_equilibrio(node) >= 2:
            print("balanceo", elem)
            self.draw()
            node = self._rebalance(node, elem)
        return node

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """ gets a node, searches the node with element elem in the subtree that hangs down node , and
        then remove this node (using super()._remove). After this, the function has to balance the node returned by the
        function super()._remove"""
        node = super()._remove(node, elem)
        if self.factor_equilibrio(node) >= 2:
            node = self._rebalance(node, elem)
        return node

    def factor_equilibrio(self, node: BinaryNode) -> int:
        if node is None:
            return 0
        else:
            return abs(self._height(node.left) - self._height(node.right))

    def findFather(self, node: BinaryNode) -> BinaryNode:
        current = self._root
        found = False
        while not found:
            if (current.right == node or current.left == node) or current == node:
                found = True
            else:
                if node.elem < current.elem:
                    current = current.left
                else:
                    current = current.right
        return current

    def _rebalance(self, node: BinaryNode, x: object) -> BinaryNode:
        nodeP = self.findFather(self.search(x))
        print("el padre es: ", nodeP)
        while self.factor_equilibrio(nodeP) < 2:
            nodeP = self.findFather(nodeP)
            print("el padre del padre es: ", nodeP)
        nodeR = nodeP.right
        print("el hijo derecho es:", nodeP.right)
        nodeL = nodeP.left
        print("el hijo izquierdo es:", nodeP.left)
        parent = self.findFather(nodeP)
        # ROTACIÓN SIMPLE IZQUIERDA
        if self._height(nodeR) > self._height(nodeL):
            if self._height(nodeR.right) > self._height(nodeR.left):
                if parent.right == nodeP:
                    parent.right = nodeR
                else:
                    parent.left = nodeR
                nodeP.right = nodeR.left
                nodeR.left = nodeP
        return node

tree = AVLTree()

data = [12, 8, 17, 6, 19]
for n in data:
    tree.insert(n)
tree.draw()
# inserting 20 will do 17 unbalanced
# simple left rotation
tree.insert(20)
tree.draw()


