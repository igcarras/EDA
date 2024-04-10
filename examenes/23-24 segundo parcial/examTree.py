from bst import BinarySearchTree
from bintree import BinaryNode


""""
https://www.geeksforgeeks.org/problems/implementing-ceil-in-bst/1?page=2&category=Binary%20Search%20Tree&difficulty=Medium&sortBy=latest
Expected Approach
Intuition
We can use BST property to solve the problem . In BST all the keys are less than all the keys that are present in its right subtree and  greater than all the keys that are present in its left subtree. In this manner considering and comparing the given number with the root value, we can decide to move either in left or right.

Implementation
make a recursive function
If a node is Null  return -1.
If the key of a node is equal to X return key. 
If the key is smaller than X , then we can say that the ceil will be at right subtree , we will call the function with its right subtree .
If the key is grater than X , then the node can be a possible solution but to get immediate greater value we have to call the function with left subtree
"""

class ExamTree(BinarySearchTree):
    def find_ceiling_node(self, x):
        return self. _find_ceiling_node(self._root, x)

    def _find_ceiling_node(self, ceil_node: BinaryNode, x: int) -> int:
        # Caso base: si el nodo actual es None, retornamos -1
        if ceil_node is None:
            return -1

        # Caso base: si el nodo actual es None, retornamos el nodo candidato actual (ceil_node)
        if ceil_node.elem == x:
            return ceil_node.elem

        # Si el valor del nodo actual es menor que x, actualizamos ceil_node y exploramos el subárbol derecho
        if ceil_node.elem < x:
            return self._find_ceiling_node(ceil_node.right, x)

        #  los datos en el nodo actual son mayores que el número dado por lo que llamamos a
        #  la función recursivamente para el subárbol izquierdo.
        val = self._find_ceiling_node(ceil_node.left, x)
        # Devuelve el máximo del número dado (ceil_node)
        return val if val >= x else ceil_node.elem


if __name__ == "__main__":
    tree1 = ExamTree()
    input_list = [5, 1, 7, 2, 3]
    for x in input_list:
         tree1.insert(x)
        # you can see the tree after each insertion
   # show the resulting tree
    tree1.draw()
    print(tree1.find_ceiling_node(3))
    print(tree1.find_ceiling_node(7))
    print(tree1.find_ceiling_node(6))
    print(tree1.find_ceiling_node(12))

    tree2 = ExamTree()
    input_list = [10, 5, 11, 4, 7, 8]
    for x in input_list:
         tree2.insert(x)
        # you can see the tree after each insertion
   # show the resulting tree
    tree2.draw()
    print(tree2.find_ceiling_node(6))
    print(tree2.find_ceiling_node(7))
    print(tree2.find_ceiling_node(4))
    print(tree2.find_ceiling_node(2))
    print(tree2.find_ceiling_node(15))

    tree3 = ExamTree()
    input_list = [9, 7, 3, 2, 1, 18, 22, 17, 15, 31]
    for x in input_list:
        tree3.insert(x)
    # you can see the tree after each insertion
    # show the resulting tree
    tree3.draw()
    print(tree3.find_ceiling_node(9))
    print(tree3.find_ceiling_node(1))
    print(tree3.find_ceiling_node(4))
    print(tree3.find_ceiling_node(31))
    print(tree3.find_ceiling_node(16))
    print(tree3.find_ceiling_node(32))

