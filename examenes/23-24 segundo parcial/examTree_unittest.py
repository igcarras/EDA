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

import unittest

class Test(unittest.TestCase):
  def setUp(self):
    return
  
  def test0(self):
    print('Test 0')
    tree1 = ExamTree()
    input_list = [5, 1, 7, 2, 3]
    for x in input_list:
         tree1.insert(x)
    self.assertEqual(tree1.find_ceiling_node(3), 3)
    self.assertEqual(tree1.find_ceiling_node(1), 1)
    self.assertEqual(tree1.find_ceiling_node(5), 5)
    self.assertEqual(tree1.find_ceiling_node(7), 7)
    self.assertEqual(tree1.find_ceiling_node(6), 7)
    self.assertEqual(tree1.find_ceiling_node(12), -1)

  def test1(self):
    print('Test 1')
    tree1 = ExamTree()
    input_list = [10, 5, 11, 4, 7, 8]
    for x in input_list:
         tree1.insert(x)
    self.assertEqual(tree1.find_ceiling_node(6), 7)
    self.assertEqual(tree1.find_ceiling_node(7), 7)
    self.assertEqual(tree1.find_ceiling_node(4), 4)
    self.assertEqual(tree1.find_ceiling_node(2), 4)
    self.assertEqual(tree1.find_ceiling_node(8), 8)
    self.assertEqual(tree1.find_ceiling_node(9), 10)
    self.assertEqual(tree1.find_ceiling_node(10), 10)
    self.assertEqual(tree1.find_ceiling_node(11), 11)
    self.assertEqual(tree1.find_ceiling_node(15), -1)
    self.assertEqual(tree1.find_ceiling_node(12), -1)

  def test2(self):
    print('Test 2')
    tree1 = ExamTree()
    input_list = [9, 7, 3, 2, 1, 18, 22, 17, 15, 31]
    for x in input_list:
         tree1.insert(x)
    self.assertEqual(tree1.find_ceiling_node(9), 9)
    self.assertEqual(tree1.find_ceiling_node(1), 1)
    self.assertEqual(tree1.find_ceiling_node(4), 7)
    self.assertEqual(tree1.find_ceiling_node(7), 7)
    self.assertEqual(tree1.find_ceiling_node(3), 3)
    self.assertEqual(tree1.find_ceiling_node(2), 2)
    self.assertEqual(tree1.find_ceiling_node(18), 18)
    self.assertEqual(tree1.find_ceiling_node(22), 22)
    self.assertEqual(tree1.find_ceiling_node(17), 17)
    self.assertEqual(tree1.find_ceiling_node(15), 15)
    self.assertEqual(tree1.find_ceiling_node(31), 31)
    self.assertEqual(tree1.find_ceiling_node(16), 17)
    self.assertEqual(tree1.find_ceiling_node(30), 31)
    self.assertEqual(tree1.find_ceiling_node(32), -1)
    self.assertEqual(tree1.find_ceiling_node(19), 22)

  def test3(self):
    print('Test 3')
    tree1 = ExamTree()
    self.assertEqual(tree1.find_ceiling_node(9), -1)
    self.assertEqual(tree1.find_ceiling_node(1), -1)
    self.assertEqual(tree1.find_ceiling_node(4), -1)
    self.assertEqual(tree1.find_ceiling_node(7), -1)
    self.assertEqual(tree1.find_ceiling_node(3), -1)
    self.assertEqual(tree1.find_ceiling_node(2), -1)
    self.assertEqual(tree1.find_ceiling_node(18), -1)
    self.assertEqual(tree1.find_ceiling_node(22), -1)
    self.assertEqual(tree1.find_ceiling_node(17), -1)
    self.assertEqual(tree1.find_ceiling_node(15), -1)
    self.assertEqual(tree1.find_ceiling_node(31), -1)
    self.assertEqual(tree1.find_ceiling_node(16), -1)
    self.assertEqual(tree1.find_ceiling_node(30), -1)
    self.assertEqual(tree1.find_ceiling_node(32), -1)
    self.assertEqual(tree1.find_ceiling_node(19), -1)
  def test4(self):
    print('Test 4')
    tree1 = ExamTree()
    input_list = [12, 7, 11, 4, 3, 8, 96 ,42, 54,43 ,72,62]
    for x in input_list:
         tree1.insert(x)
    #tree1.draw()
    self.assertEqual(tree1.find_ceiling_node(6), 7)
    self.assertEqual(tree1.find_ceiling_node(7), 7)
    self.assertEqual(tree1.find_ceiling_node(4), 4)
    self.assertEqual(tree1.find_ceiling_node(2), 3)
    self.assertEqual(tree1.find_ceiling_node(8), 8)
    self.assertEqual(tree1.find_ceiling_node(9), 11)
    self.assertEqual(tree1.find_ceiling_node(52), 54)
    self.assertEqual(tree1.find_ceiling_node(11), 11)
    self.assertEqual(tree1.find_ceiling_node(63), 72)
    self.assertEqual(tree1.find_ceiling_node(73), 96)
    self.assertEqual(tree1.find_ceiling_node(100), -1)
  def test5(self):
    print('Test 5')
    tree1 = ExamTree()
    input_list = [6, 4, 7]
    for x in input_list:
      tree1.insert(x)
    # tree1.draw()
    self.assertEqual(tree1.find_ceiling_node(6), 6)
    self.assertEqual(tree1.find_ceiling_node(7), 7)
    self.assertEqual(tree1.find_ceiling_node(4), 4)
    self.assertEqual(tree1.find_ceiling_node(1), 4)
    self.assertEqual(tree1.find_ceiling_node(5), 6)
    self.assertEqual(tree1.find_ceiling_node(9), -1)

unittest.main(argv=['first-arg-is-ignored'], exit=False)



