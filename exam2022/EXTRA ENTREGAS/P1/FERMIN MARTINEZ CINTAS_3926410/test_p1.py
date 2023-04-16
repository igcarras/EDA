#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# from p1_sol import MyDList
from p1 import MyDList

import unittest 

class Test(unittest.TestCase):
    mark = 0
    def setUp(self):
        self.list = MyDList()

    def test1(self):
        print('\nCase 1: remove sublist at the beginning')
        [self.list.append(i) for i in range(1, 6)]
        # print(self.list)
        node = self.list._head
        expected = [3, 4, 5]
        self.list.remove_sublist(node, node.next, 2)

        self.assertEqual(str(self.list), str(expected))
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list._head.elem, 3)
        self.assertEqual(self.list._tail.elem, 5)
        Test.mark += 0.2

    def test2(self):
        print('\nCase 2: remove sublist at the end')
        [self.list.append(i) for i in range(1, 6)]
        # print(self.list)

        node = self.list._tail
        expected = [1, 2 ,3]
        self.list.remove_sublist(node.prev, node, 2)

        self.assertEqual(str(self.list), str(expected))
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list._head.elem, 1)
        self.assertEqual(self.list._tail.elem, 3)
        Test.mark += 0.2

    def test3(self):
        print('\nCase 3: remove sublist in the middle')
        [self.list.append(i) for i in range(1, 6)]
        # print(self.list)

        expected = [1,5]
        self.list.remove_sublist(self.list._head.next, self.list._tail.prev, 3)

        self.assertEqual(str(self.list), str(expected))
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list._head.elem, 1)
        self.assertEqual(self.list._tail.elem, 5)
        Test.mark += 0.2

    def test4(self):
        print('\nCase 4: remove_sublist, remove whole list')
        [self.list.append(i) for i in range(1, 6)]
        # print(self.list)

        expected = []
        self.list.remove_sublist(self.list._head, self.list._tail, 5)

        self.assertEqual(str(self.list), str(expected))
        self.assertEqual(len(self.list), 0)
        self.assertIsNone(self.list._head)
        self.assertIsNone(self.list._tail)
        Test.mark += 0.2

    def test5(self):
        print('\nCase 5: remove_section_by_sum, list empty with any k')
        expected = []
        self.list.remove_section_by_sum(7)
        self.assertEqual(str(self.list), str(expected))
        Test.mark += 0.1

    def test6(self):
        print('\nCase 6: remove_section_by_sum, k lower than 0, nothing removed')
        expected = []
        self.list.remove_section_by_sum(-3)
        self.assertEqual(str(self.list), str(expected))
        Test.mark += 0.1

    def test7(self):
        print('\nCase 7: remove_section_by_sum, pattern not found, nothing removed')
        [self.list.append(i) for i in range(1, 4)]
        # print(self.list)
        expected = [1, 2, 3]
       # self.list.remove_section_by_sum(28)
        self.assertEqual(str(self.list), str(expected))
        Test.mark += 0.2

    def test8(self):
        print('\nCase 8: remove_section_by_sum, pattern found at the beggining')
        [self.list.append(i) for i in range(1, 4)]
        # print(self.list)
        expected = [3]
        self.list.remove_section_by_sum(3)
        self.assertEqual(str(self.list), str(expected))
        self.assertEqual(len(self.list), 1)
        Test.mark += 0.6

    def test9(self):
        print('\nCase 9: remove_section_by_sum, pattern found at the end')
        [self.list.append(i) for i in range(1, 4)]
        expected = [1]
        self.list.remove_section_by_sum(5)
        self.assertEqual(str(self.list), str(expected))
        self.assertEqual(len(self.list), 1)
        Test.mark += 0.6

    def test_10(self):
        print('\nCase 10: remove_section_by_sum, pattern found in the middle')
        self.list.append(5)
        [self.list.append(1) for _ in range(4)]
        self.list.append(7)
        # print(self.list)
        expected=[5, 7]
        self.list.remove_section_by_sum(4)
        self.assertEqual(str(self.list), str(expected))
        self.assertEqual(len(self.list), 2)
        Test.mark += 0.6

    def test_11(self):
        print('\nCase 11: remove_section_by_sum, pattern found containing the whole list')
        self.list.append(5)
        self.list.append(5)
        self.list.append(7)
        # print(self.list)
        expected = []
        self.list.remove_section_by_sum(17)
        self.assertEqual(str(self.list), str(expected))
        self.assertEqual(len(self.list), 0)
        Test.mark += 0.3

    def test_print(self):
        print(Test.mark)

if __name__ == '__main__':
   unittest.main()
