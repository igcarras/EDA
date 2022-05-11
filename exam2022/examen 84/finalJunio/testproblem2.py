# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 10:20:39 2022

@author: user
"""

import unittest # package that contains the classes t

from problem2_skeleton import MyBST

class Test(unittest.TestCase):
    """
    - test1: tree.getCount(0,5) = 0
    - test2: tree.getCount(5,0) = 0
    - test3: tree.getCount(1,4) = 0
    - test4: tree.getCount(95,100) = 0
    - test5: tree.getCount(21,45) = 0
    - test6: tree.getCount(57,80) = 0
    - test7: tree.getCount(4,100) = 8
    - test8: tree.getCount(10,81) = 6
    - test9: tree.getCount(12,81) = 6
    - test_10: tree.getCount(4,50) = 4
    - test_11: tree.getCount(50, 90) = 3
    - test_12: tree.getCount(5, 10) = 1
    """
    mark = 0

    def setUp(self) -> None:
        self.tree = MyBST()
        self.data = [46, 11, 81, 51, 56, 94, 5, 20]
        for x in self.data:
            self.tree.insert(x)
        # self.tree.draw()

    def test1(self) -> None:
        print("test1: tree.getCount(0,5)")
        input_tree = MyBST()
        # print('Input tree:')
        # input_tree.draw()
        expected = 0
        result = input_tree.getCount(0, 5)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 0.5

    def test2(self) -> None:
        print("\ntest2: tree.getCount(5,0)")
        # print('Input tree:')
        # self.tree.draw()
        expected = 0
        result = self.tree.getCount(5, 0)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 0.5

    def test3(self) -> None:
        print("\ntest3: tree.getCount(1,4)")
        # print('Input tree:')
        # self.tree.draw()
        expected = 0
        result = self.tree.getCount(1, 4)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 0.5

    def test4(self) -> None:
        print("\ntest4: tree.getCount(95,100)")
        # print('Input tree:')
        # self.tree.draw()
        expected = 0
        result = self.tree.getCount(95, 100)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 0.5

    def test5(self) -> None:
        print("\ntest5: tree.getCount(21,45)")
        # print('Input tree:')
        # self.tree.draw()
        expected = 0
        result = self.tree.getCount(21, 45)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 0.75

    def test6(self) -> None:
        print("\ntest6: tree.getCount(57,80)")
        # print('Input tree:')
        # self.tree.draw()
        expected = 0
        result = self.tree.getCount(57, 80)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 0.75

    def test7(self) -> None:
        print("\ntest7: tree.getCount(4,100)")
        # print('Input tree:')
        # self.tree.draw()
        print(sorted(self.data))
        expected = 8
        result = self.tree.getCount(4, 100)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 1.5

    def test8(self) -> None:
        print("\ntest8: tree.getCount(10,81)")
        # print('Input tree:')
        # self.tree.draw()
        aux = [11, 20, 46, 51, 56, 81]
        expected = 6
        result = self.tree.getCount(10, 81)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 2

    def test9(self) -> None:
        print("\ntest9: tree.getCount(12,81)")
        # print('Input tree:')
        # self.tree.draw()
        expected = 6
        result = self.tree.getCount(12, 100)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 2

    def test_10(self) -> None:
        print("\ntest_10: tree.getCount(4, 50)")
        # print('Input tree:')
        # self.tree.draw()
        expected = 4
        result = self.tree.getCount(4, 50)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 2

    def test_11(self) -> None:
        print("\ntest_11: tree.getCount(50, 90)")
        # print('Input tree:')
        # self.tree.draw()
        expected = 3
        result = self.tree.getCount(50, 90)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 2

    def test_12(self) -> None:
        print("\ntest_12: tree.getCount(5, 10)")
        # print('Input tree:')
        # self.tree.draw()
        expected = 1
        result = self.tree.getCount(5, 10)
        print("expected= ", expected)
        print("result= ", result)
        self.assertEqual(result, expected)

        Test.mark += 2

    def test_z(self):
        print("Nota provisional:", Test.mark)


if __name__ == "__main__":
    unittest.main()
