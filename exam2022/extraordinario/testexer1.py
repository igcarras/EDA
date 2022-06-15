#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from exer1 import MyDList

import unittest 

class Test(unittest.TestCase):

    def setUp(self):
        self.list = MyDList()
   
    def test1(self):
        print('\nCase 1: list empty with any k')
        expected=[]
        self.list.remove_section_by_sum(7)

        self.assertEqual(str(self.list), str(expected))
        
    def test2(self):
        print('\nCase 2: k lower than 0, nothing removed')
        expected=[]
        self.list.remove_section_by_sum(-3)

        self.assertEqual(str(self.list), str(expected))
        
    def test3(self):
        print('\nCase 3: pattern not found, nothing removed')
        [self.list.append(i) for i in range(1, 4)]

        expected=[1, 2, 3]
        self.list.remove_section_by_sum(28)

        self.assertEqual(str(self.list), str(expected))
        
    def test4(self):
        print('\nCase 4: pattern found at the beggining')
        [self.list.append(i) for i in range(1, 4)]

        expected=[3]
        self.list.remove_section_by_sum(3)

        self.assertEqual(str(self.list), str(expected))
        self.assertEqual(len(self.list), 1)
        
    def test5(self):
        print('\nCase 5: pattern found at the end')
        [self.list.append(i) for i in range(1, 4)]

        expected=[1]
        self.list.remove_section_by_sum(5)

        self.assertEqual(str(self.list), str(expected))
        self.assertEqual(len(self.list), 1)

    def test6(self):
        print('\nCase 6: pattern found in the middle')
        self.list.append(5)
        [self.list.append(1) for _ in range(4)]
        self.list.append(7)
        
        expected=[5, 7]
        self.list.remove_section_by_sum(4)

        self.assertEqual(str(self.list), str(expected))
        self.assertEqual(len(self.list), 2)

    def test7(self):
        print('\nCase 7: pattern found containing the whole list')
        self.list.append(5)
        self.list.append(5)        
        self.list.append(7)
        
        expected=[]
        self.list.remove_section_by_sum(17)

        self.assertEqual(str(self.list), str(expected))
        self.assertEqual(len(self.list), 0)

    def test8(self):
        print('\nCase 8: remove sublist at the beggining')
        [self.list.append(i) for i in range(1, 6)]

        node = self.list._head
        expected=[3, 4, 5]
        self.list.remove_sublist(node, node.next, 2)

        self.assertEqual(str(self.list), str(expected))
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list._head.elem, 3)
        self.assertEqual(self.list._tail.elem, 5)

    def test9(self):
        print('\nCase 9: remove sublist at the end')
        [self.list.append(i) for i in range(1, 6)]       
        
        node = self.list._tail 
        expected=[1, 2 ,3]
        self.list.remove_sublist(node.prev, node, 2)

        self.assertEqual(str(self.list), str(expected))
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list._head.elem, 1)
        self.assertEqual(self.list._tail.elem, 3)

    def test10(self):
        print('\nCase 10: remove sublist in the middle')
        [self.list.append(i) for i in range(1, 6)]        
        
        expected=[1,5]
        self.list.remove_sublist(self.list._head.next, self.list._tail.prev, 3)

        self.assertEqual(str(self.list), str(expected))
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list._head.elem, 1)
        self.assertEqual(self.list._tail.elem, 5)

    def test11(self):
        print('\nCase 11: remove whole list')
        [self.list.append(i) for i in range(1, 6)] 
        
        expected=[]
        self.list.remove_sublist(self.list._head, self.list._tail, 5)

        self.assertEqual(str(self.list), str(expected))
        self.assertEqual(len(self.list), 0)
        self.assertIsNone(self.list._head)
        self.assertIsNone(self.list._tail)


#If you are using Spyder, please comment the following line: 
# unittest.main(argv=['first-arg-is-ignored'], exit=False)

#To use Spyder, remove the following comments:
if __name__ == '__main__':
   unittest.main()