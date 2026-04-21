from bst import BinarySearchTree
    
class BT(BinarySearchTree):
    
    
    """CREATE A recursive function that REMOVES the GREATEST NODE"""
    def remove_max(self):
        return self._remove_max(self._root)

    def _remove_max(self, node) -> object:
        
        if node is None:
            return None   # base case to protect from self._root None
        elif node.right is None:
            return node.left  # base case
        else:
            node.right = self._remove_max(node.right)  # base recursive
        
        return node
    
    


     """prints the elements of those nodes whose grandparents' elements are multiply of 10
    def prints10(self) -> None:
        What is its temporal complexity"""
        # Complexity: O(n), where n is the size of the tree.
        # The function has to visit all the nodes of the tree.
        self._prints10(self._root, None, None)

    def _prints10(self, node: BinaryNode, parent: BinaryNode, grand: BinaryNode) -> None:
        if node:
            self._prints10(node.left, node, parent)
            if grand and grand.elem % 10 == 0:
                print(node.elem, end=' ')
            self._prints10(node.right, node, parent)


    


    """Calculate the length of the longest path passing through the root . 
       Return length"""
    def max_path_root(self):
    
        if self._root is None:
            return 0
        node =self._root
        left_h = 0
        right_h = 0
        if node.left:
            left_h = 1 + self._height(node.left)
        if node.right:
            right_h = 1 + self._height(node.right)
        
        return left_h + right_h
    
    """
    Implement a recursive method that returns the distance between  two elements a and b within the tree. 
    Suppose a and be belong to the tree.The solution must have a recursive approach.
    """
    def getDist(self, a, b):
        node = self._root
        return self._getDist(node, a, b)
    
    def _getDist(self, node, a, b):
        # Base case: If the node is None
        if node is None:
            return None
    
        # If both a and b are smaller than node's key, then LCA (Lowest Common Ancestor) lies in the left
        if a < node.elem and b < node.elem:
            return self._getDist(node.left, a, b)
        # If both a and b are greater than node's key, then LCA (Lowest Common Ancestor) lies in the right
        if a > node.elem and b > node.elem:
            return self._getDist(node.right, a, b)
    
        # If one key is on the left and the other is on the right or one of them matches the node's key
        if a <= node.elem <= b or b <= node.elem <= a:
            return self.distance_from_lca(node, a) + self.distance_from_lca(node, b)
    

    def distance_from_lca(self, node, key):
        if node.elem == key:
            return 0
        elif key < node.elem:
            return 1 + self.distance_from_lca(node.left, key)
        else:
            return 1 + self.distance_from_lca(node.right, key)
    
    # iterative function to distance_from_lca
    def distance_from_lca2(node, key):
        distance = 0
        while node.elem != key:
            if key < node.elem:
                node = node.left
            else:
                node = node.right
            distance += 1
        return distance
    
tree =BT()
values = [25, 20, 36, 10, 22, 30, 40, 5, 12, 28, 38, 48]
for x in values:
   tree.insert(x)
tree.draw()
print(tree.getDist(25,38))
print(tree.getDist(36,5))
tree.remove_max()
tree.draw()
tree.remove_max()
tree.draw()
tree.remove_max()
print(tree.max_path_root())
