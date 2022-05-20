#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from exer2 import BinaryNode, BinaryTree

import unittest 

class Test(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTree()
   
    def test1(self):
        print('\nCase 1: tree is empty')

        self.assertEqual(self.tree.right_sum(), 0)
        
    def test2(self):
        print('\nCase 2: tree not empty (1)')

        left = BinaryNode(3, BinaryNode(1), None)
        right = BinaryNode(9, BinaryNode(8), BinaryNode(20))
        right.right.right = BinaryNode(30)
        self.tree._root = BinaryNode(5, left, right)

        self.assertEqual(self.tree.right_sum(), 64)

    def test3(self):
        print('\nCase 3: tree not empty (2)')

        left = BinaryNode(3, BinaryNode(2), BinaryNode(20))
        right = BinaryNode(9, None, BinaryNode(22))
        right.right.left = BinaryNode(5)
        left.left.left = BinaryNode(23)
        self.tree._root = BinaryNode(1, left, right)

        self.assertEqual(self.tree.right_sum(), 37)
    
    def test4(self):
        print('\nCase 4: tree not empty (3)')

        left = BinaryNode(3, BinaryNode(2), BinaryNode(20))
        right = BinaryNode(9, None, BinaryNode(12))
        right.right.left = BinaryNode(5)
        left.left.left = BinaryNode(23)
        self.tree._root = BinaryNode(1, left, right)

        self.assertEqual(self.tree.right_sum(), 27)
        self.assertEqual(self.tree.right_sum(), 27)
        
    def test5(self):
        print('\nCase 5: tree not empty (4)')

        left = BinaryNode(3, BinaryNode(2), None)        
        left.left.left = BinaryNode(23)
        left.left.right = BinaryNode(5)
        self.tree._root = BinaryNode(1, left, None)

        self.assertEqual(self.tree.right_sum(), 11)

#If you are using Spyder, please comment the following line: 
# unittest.main(argv=['first-arg-is-ignored'], exit=False)

#To use Spyder, remove the following comments:
if __name__ == '__main__':
   unittest.main()