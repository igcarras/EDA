import unittest
from p3 import Archipelago, AdjacentIsland
import copy
import math

class Test_P3(unittest.TestCase):
    mark = 0

    def setUp(self):
       self.g1 = Archipelago(10)
       self.g1.add_bridge(0, 1, 5, 10)
       self.g1.add_bridge(0, 2, 4, 3)
       self.g1.add_bridge(0, 3, 3, 15)
       self.g1.add_bridge(2, 3, 4, 3)
       self.g1.add_bridge(3, 8, 3, 3)
       self.g1.add_bridge(6, 8, 2, 3)
       self.g1.add_bridge(8, 9, 2, 3)
       # print(self.g1)
       
       self.g2 = Archipelago(5)
      
       self.g3 = Archipelago(4)
       self.g3.add_bridge(0, 1, 2, 1)
       self.g3.add_bridge(0, 3, 4, 10)
       self.g3.add_bridge(1, 2, 2, 1)
       self.g3.add_bridge(2, 3, 2, 1)
       print(self.g3)
       

    def test1(self):
        """ non_accessible_islands: general case """
        expected = [4, 5, 7]
        result = self.g1.non_accessible_islands()
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
        
    def test2(self):
        """ non_accessible_islands: case all """
        expected = [0,1,2,3,4]
        result = self.g2.non_accessible_islands()
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
        
    def test3(self):
        """ non_accessible_islands: case none """
        expected = []
        result = self.g3.non_accessible_islands()
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
    
    
        
    def test4(self):
        """ islands_k_bridges: case 0 bridges """
        expected = [4,5,7]
        result = self.g1.islands_k_bridges(0)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
        
    def test5(self):
        """ islands_k_bridges: case 1 bridge"""
        expected = [2]
        result = self.g1.islands_k_bridges(2)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
        
    def test6(self):
        """ islands_k_bridges: case 3 bridges"""
        expected = [0,3,8]
        result = self.g1.islands_k_bridges(3)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
        
    def test7(self):
        """ islands_k_bridges: case no bridges """
        expected = []
        result = self.g2.islands_k_bridges(3)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
        
        
    def test8(self):
        """ accessible_from: case island no found """
        expected = []
        result = self.g1.accessible_from(11,0)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
        
    def test9(self):
        """ accessible_from: case isolated island"""
        expected = []
        result = self.g1.accessible_from(5,1)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
        
    def test10(self):
        """ accessible_from: case tide > all bridges"""
        expected = []
        result = self.g1.accessible_from(5,20)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
    
    def test11(self):
        """ accessible_from: 0 case tide = 1"""
        expected = [1, 2, 3, 8, 6, 9]
        result = self.g1.accessible_from(0,1)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
        
    def test12(self):
        """ accessible_from: 0 case tide = 3"""
        expected = [1,2,3]
        result = self.g1.accessible_from(0,3)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
        
    def test13(self):
        """ accessible_from: 9 case tide = 4"""
        expected = []
        result = self.g1.accessible_from(9,4)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
  
    
    
    def test14(self):
        """ minimum_path: graph with no edges"""
        expected = [],math.inf
        result = self.g2.minimum_path(0, 9, 3)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
        
    def test15(self):
        """ minimum_path: case island not found"""
        expected = [],math.inf
        result = self.g1.minimum_path(0, 9, 3)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
        
    def test16(self):
        """ minimum_path: case isolated island"""
        expected = [],math.inf
        result = self.g1.minimum_path(5, 4, 3)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
        
    def test17(self):
        """ minimum_path: case tide > all connected bridges"""
        expected = [],math.inf
        result = self.g3.minimum_path(0, 3, 10)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5

    def test18(self):
        """ minimum_path: case tide < all connected  bridges"""
        expected = [0,1,2,3],3
        result = self.g3.minimum_path(0, 3, 1)
        self.assertEqual(result, expected)
        Test_P3.mark += 0.5
        
    def test19(self):
        """ minimum_path: case tide < some connected  bridges"""
        expected = [0,3],10
        result = self.g3.minimum_path(0, 3, 4)
        self.assertEqual(result, expected)
        Test_P3.mark += 1
        
    def test_z(self):
        print('\n\n\nNota provisional: ', Test_P3.mark)


if __name__ == "__main__":
    unittest.main()
