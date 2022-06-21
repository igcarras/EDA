#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from p2_sol import BinaryTree

import unittest


class Test(unittest.TestCase):
    mark = 0

    def setUp(self):
        self.tree = BinaryTree()

    def test1(self):
        print('\nCase 1: tree is empty')

        self.assertEqual(self.tree.right_sum(), 0)
        Test.mark += 0.1

    def test2(self):
        print('\nCase 2: tree not empty. Unbalanced (root with two branches)')
        for x in [5, 3, 9, 1, 8, 20, 30]:
            self.tree.insert(x)

        self.tree.draw()

        self.assertEqual(self.tree.right_sum(), 64)
        Test.mark += 0.3

    def test3(self):
        print('\nCase 3: tree not empty. Unbalanced (only right branch). Right leaf alone')

        for x in [1, 3, 9, 2, 20, 22, 5]:
            self.tree.insert(x)

        #self.tree.draw()

        self.assertEqual(self.tree.right_sum(), 55)
        Test.mark += 0.3

    def test4(self):
        print('\nCase 4: tree not empty. Unbalanced (only right branch)')

        for x in [1, 3, 9, 2, 20, 12, 5, 23]:
            self.tree.insert(x)

        #self.tree.draw()

        self.assertEqual(self.tree.right_sum(), 56)
        # self.assertEqual(self.tree.right_sum(), 27)
        Test.mark += 0.3

    def test5(self):
        print('\nCase 5: tree not empty. Unbalanced (only right branch). Left leaf alone')

        for x in [1, 3, 2, 23, 5]:
            self.tree.insert(x)

        #self.tree.draw()

        self.assertEqual(self.tree.right_sum(), 32)
        Test.mark += 0.3

    def test6(self):
        print('\nCase 6: tree not empty. Unbalanced (only left branch). Left leaf alone')

        for x in [18, 3, 2, 6, 17, 12]:
            self.tree.insert(x)

        #self.tree.draw()

        self.assertEqual(self.tree.right_sum(), 56)
        Test.mark += 0.3

    def test7(self):
        print('\nCase 7: tree not empty. Unbalanced (only left branch). Right leaf alone')

        for x in [18, 3, 2, 6, 10, 12]:
            self.tree.insert(x)

        #self.tree.draw()

        self.assertEqual(self.tree.right_sum(), 49)
        Test.mark += 0.3

    def test8(self):
        print('\nCase 8: tree not empty. Unbalanced (only left branch). Fully degenerated tree')

        for x in [55, 9, 6, 4, 2, 1]:
            self.tree.insert(x)

        #self.tree.draw()

        self.assertEqual(self.tree.right_sum(), 77)
        Test.mark += 0.3

    def test9(self):
        print('\nCase 9: tree not empty. Only root')

        for x in [55]:
            self.tree.insert(x)

        #self.tree.draw()

        self.assertEqual(self.tree.right_sum(), 55)
        Test.mark += 0.2

    def test10(self):
        print('\nCase 10: tree not empty. Balanced three-levels')

        for x in [15, 7, 21, 3, 9, 19, 24]:
            self.tree.insert(x)

        #self.tree.draw()
        self.assertEqual(self.tree.right_sum(), 60)
        Test.mark += 0.3

    def test11(self):
        print('\nCase 11: tree not empty. Balanced four-levels')

        for x in [15, 7, 21, 3, 9, 19, 24, 4, 2, 8, 10, 18, 23, 25]:
            self.tree.insert(x)

        #self.tree.draw()

        self.assertEqual(self.tree.right_sum(), 85)
        Test.mark += 0.3

    def test12(self):
        print('\nCase 12: tree not empty. Unbalanced (only right branch). Fully degenerated tree')

        for x in [1, 6, 8, 14, 22, 31]:
            self.tree.insert(x)

        #self.tree.draw()

        self.assertEqual(self.tree.right_sum(), 82)
        Test.mark += 0.3

    def test_print(self):
        print("Nota provisional: ", Test.mark)

if __name__ == '__main__':
    unittest.main()
