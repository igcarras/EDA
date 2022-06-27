import unittest
from p3 import Archipelago
#from p3 import Archipelago
import math

class Test_P3(unittest.TestCase):
    mark = 0
    def setUp(self):
        self.g1 = Archipelago(7)
        self.g1.add_bridge(0, 1, 2, 3)
        self.g1.add_bridge(0, 2, 5, 10)
        self.g1.add_bridge(1, 2, 3, 2)
        self.g1.add_bridge(1, 3, 3, 3)
        self.g1.add_bridge(2, 3, 4, 10)
        self.g1.add_bridge(2, 4, 5, 3)
        self.g1.add_bridge(3, 4, 4, 4)
       # print(self.g1)
       

        self.g2 = Archipelago(4)
        self.g2.add_bridge(0, 1, 3, 1)
        self.g2.add_bridge(0, 3, 4, 10)
        self.g2.add_bridge(1, 2, 3, 1)
        self.g2.add_bridge(2, 3, 2, 1)
        #print(self.g2)

    def test1(self):
        """ accessible_from: case island no found """
        expected = []
        result = self.g1.accessible_from(11, 0)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.05
        
    def test2(self):
        """ accessible_from: case isolated island"""
        expected = []
        result = self.g1.accessible_from(5, 0)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.05

    def test3(self):
        """ accessible_from: case tide > all bridges"""
        expected = []
        result = self.g1.accessible_from(0, 5)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.1

    def test4(self):
        """ accessible_from: 0 case tide = 1"""
        expected = [1, 2, 3, 4]
        result = self.g1.accessible_from(0, 1)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.1

    def test5(self):
        """ accessible_from: 0 case tide = 2"""
        expected = [1, 2, 3, 4]
        expected2 = [2, 1, 3, 4]

        result = self.g1.accessible_from(0, 2)
        try:
            self.assertEqual(result, expected)
        except:
            self.assertEqual(result, expected2)
        Test_P3.mark += 0.2


    def test6(self):
        """ accessible_from: 0 case tide = 3"""
        expected = [2, 3, 4]
        result = self.g1.accessible_from(0, 3)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.2

    def test7(self):
        """ accessible_from: 0 case tide = 4"""
        expected = [2, 4]
        result = self.g1.accessible_from(0, 4)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.2

    def test8(self):
        """ accessible_from: 4 case tide = 1"""
        expected = [2, 3, 0, 1]
        result = self.g1.accessible_from(4, 1)
        try:
            # bfs
            self.assertEqual(result, expected)
        except:
            # dfs
            expected = [2, 0, 1, 3]
            self.assertEqual(result, expected)
        Test_P3.mark += 0.2


    def test9(self):
        """ accessible_from: 4 case tide = 3"""
        expected = [2, 0, 3]
        result = self.g1.accessible_from(4, 3)
        try:
            # dfs
            self.assertEqual(result, expected)
        except:
            expected = [2, 3, 0]  # bfs
            self.assertEqual(result, expected)
        Test_P3.mark += 0.2


    def test_10(self):
        """ accessible_from: 4 case tide = 4"""
        expected = [2, 0]
        result = self.g1.accessible_from(4, 4)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.2

    def test_11(self):
        """ minimum_path: case isolated island"""
        expected = [], math.inf
        result = self.g1.minimum_path(0, 5, 1)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.1

    def test_12(self):
        """ minimum_path: case tide >= all connected bridges (graph 1)"""
        expected = [], math.inf
        result = self.g1.minimum_path(0, 3, 5)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.1

    def test_13(self):
        """ minimum_path: case tide < all connected  bridges (graph 1)"""
        expected = [0, 1, 2, 4], 8
        result = self.g1.minimum_path(0, 4, 1)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.2

    def test_14(self):
        """ minimum_path: start=0, end=4, tide=2"""
        expected = [0, 2, 4], 13
        result = self.g1.minimum_path(0, 4, 2)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.2

    def test_15(self):
        """ minimum_path: start=2, end=3, tide=1"""
        expected = [2, 1, 3], 5
        result = self.g1.minimum_path(2, 3, 1)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.2

    def test_16(self):
        """ minimum_path: start=2, end=3, tide=3"""
        expected = [2, 4, 3], 7
        result = self.g1.minimum_path(2, 3, 3)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.2

    def test_17(self):
        """ minimum_path: start=2, end=3, tide=4"""
        expected = [], math.inf
        result = self.g1.minimum_path(2, 3, 4)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.1

    def test_18(self):
        """ minimum_path: case tide < all connected  bridges  (graph 3)"""
        expected = [0, 1, 2, 3], 3
        result = self.g2.minimum_path(0, 3, 1)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.13

    def test_19(self):
        """ minimum_path: g2, start=0, end=3, tide=1"""
        expected = [0, 1, 2, 3], 3
        result = self.g2.minimum_path(0, 3, 1)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.15

    def test_20(self):
        """ minimum_path: g2, start=0, end=3, tide=2"""
        expected = [0, 3], 10
        result = self.g2.minimum_path(0, 3, 2)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.15

    def test_21(self):
        """ minimum_path: start=2, end=0, tide=1 (graph 2)"""
        expected = [2, 1, 0], 2
        result = self.g2.minimum_path(2, 0, 1)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.15

    def test_22(self):
        """ minimum_path: start=2, end=3, tide=2 (graph 2)"""
        expected = [2, 1, 0, 3], 12
        result = self.g2.minimum_path(2, 3, 2)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.15

    def test_print(self):
        print("Nota provisional:", Test_P3.mark)


if __name__ == "__main__":
    unittest.main()
