# from binarysearchtree import BinarySearchTree
from bst import BinarySearchTree
from bst import BinaryNode


class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        """gets a node, searches the place to insert a new node with
        element e (using super()._insert),  and then, the function has to
        balance the node returned by the function super.()_insert"""
        node = super()._insert(node, elem)
        node = self._rebalance(node)
        return node

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """ gets a node, searches the node with element elem in the subtree
        that hangs down node , and then remove this node (using super(
        )._remove). After this, the function has to balance the node
        returned by the function super()._remove"""
        node = super()._remove(node, elem)
        node = self._rebalance(node)
        return node

    def fe_height(self, elem): # calcular factor equilibrio
        node = self.search(elem)
        return self._fe_height(node)

    def _fe_height(self, node):
        if node is None:
            return 0
        else:
            return self._height(node.left) - self._height(node.right)

    def is_balanced(self): # comprobar si está balanceado
        return self._is_balanced(self._root)

    def _is_balanced(self, node):
        if node:
            if (1 >= self._fe_height(node) >= -1) \
                    and self._is_balanced(node.left) and self._is_balanced(
                    node.right):
                return True
            return False
        return True

    def rebalance(self, elem):
        node = self.search(elem)
        return self._rebalance(node)

    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        """ gets node and balances it"""
        if not self._is_balanced(node):
            x = node.left
            if self._fe_height(node) > 0 and x.right is None:
            #    # Rotación simple derecha
                x.right = node


        return node



if __name__ == "__main__":
    tree = AVLTree()
    for x in [50, 60, 30, 20, 70, 66, 65, 10, 80, 35, 5]:
        tree.insert(x)

    print('input tree:')
    tree.draw()
  #  print()
   # tree.rebalance(30)
   # print()
  ##  print("height-balanced factor of 30 is:", tree.fe_height(30))
