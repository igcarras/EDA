#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from parcial82 import MyList

import unittest # package that contains the classes t

class Test(unittest.TestCase):
    """
        test1: empty  list
        test2: e=10 no exist
        test3: e = 1 and e is the first
        test4: e = 7, there is no multiples after the first occurrence
        test5: e = 2,there are several multiples after
        test6: e = 3, there are several multiples, 3 is the last element
        test7: e = 2, e first, there are multiples after

    """

    def setUp(self):
        """executed for each test"""
        self.l1 = MyList()
        self.data1 = [1, 6, 3, 2, 6, 6, 4, 7, 9, 2, 1, 1, 3, 3, 3, 2, 4, 9]
        for x in self.data1:
            self.l1.append(x)

        self.data2 = [2, 6, 3, 2, 6, 6, 4, 7, 9, 2, 2, 1, 1, 3, 3, 3, 2, 4, 9]
        self.l2 = MyList()
        for x in self.data2:
            self.l2.append(x)

    def test1(self):
        print('\nCase 1: list empty')
        result = MyList()
        print("input:", result)

        expected = []
        result.removeMultiplesOf(5)

        print("result:", result)
        print("expected:", expected)
        self.assertEqual(str(result), str(expected), "Fail: Case 1: list empty'")

        print('Case 1: list empty, ok!!!')
        
    def test2(self):
        print('\nCase 2: e=10 no exist')
        print("input:", str(self.l1))
        self.l1.removeMultiplesOf(10)

        result = self.l1
        expected = self.data1

        print("result:", result)
        print("expected:", expected)
        self.assertEqual(str(result), str(expected), "Fail: test2")

        print('Case 2: e=10 no exist, OK')
        
    def test3(self):
        print('\nCase 3: e = 1 and e is the first')
        print("input:", str(self.l1))

        self.l1.removeMultiplesOf(1)

        result = self.l1
        expected = [1]

        print("result:", result)
        print("expected:", expected)

        self.assertEqual(str(result), str(expected), "Fail: test3")
        print('Case 3: e=1, e first OK')

    def test4(self):
        print('\nCase 4: e = 7, there is no multiples after the first occurrence')
        print("input:", str(self.l1))

        self.l1.removeMultiplesOf(7)
        result = self.l1
        expected = self.data1

        print("result:", result)
        print("expected:", expected)

        self.assertEqual(str(result), str(expected), "Fail: test4")
        print('Case 4: OK')
        
    def test5(self):
        print('\nCase 5: e = 2,there are several multiples after')
        print("input:", str(self.l1))

        self.l1.removeMultiplesOf(2)

        result = self.l1
        expected = [1, 6, 3, 2, 7, 9, 1, 1, 3, 3, 3, 9]

        print("result:", result)
        print("expected:", expected)

        self.assertEqual(str(result), str(expected), "Fail: test5")

        print('Case 5: OK')
        
    def test6(self):
        print('\nCase 6: e = 3, there are several multiples, 3 is the last element')
        print("input:", str(self.l1))

        self.l1.removeMultiplesOf(3)
        result = self.l1
        expected = [1, 6, 3, 2, 4, 7, 2, 1, 1, 2, 4]

        print("result:", result)
        print("expected:", expected)

        self.assertEqual(str(result), str(expected), "Fail: test6")
        print('Case 6: OK')
        
    def test7(self):
        print('\nCase 7: e = 2, e first, there are multiples after')
        print("input:", str(self.l2))

        expected = [2, 3, 7, 9, 1, 1, 3, 3, 3, 9]
        self.l2.removeMultiplesOf(2)
        result = self.l2
        print("result:", result)
        print("expected:", expected)

        self.assertEqual(str(result), str(expected), "Fail: test7")
        print('Case 7: OK')

if __name__ == '__main__':
    unittest.main()
