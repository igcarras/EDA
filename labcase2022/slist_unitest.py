# -*- coding: utf-8 -*-

from slist import SList
import unittest #package that contains the classes t

class Test(unittest.TestCase):

    def setUp(self):
        """This functions is executed for each of the test functions"""
        self.lEmpty=SList()

        self.l1=SList()
        self.l1.addFirst(5)
        
        self.l4=SList()
        self.l4.addFirst(1)
        self.l4.addFirst(3)
        self.l4.addFirst(8)
        self.l4.addFirst(1)
        
        # print(self.lEmpty)
        # print(self.l1)
        # print(self.l4)
        
        


    def test1_len(self):
        print('\nCase 1: len in a list of length ==0')
        expected=[]
        self.assertEqual(len(self.lEmpty), len(expected), "Fail: len in a length of length==0")

    def test2_len(self):
        print('Case 2: len in a list of length > 0')

        expected=[1,8,3,1]
        self.assertEqual(len(self.l4), len(expected), "Fail: len in a lest with length>0")
        print()

    def test4_addLast(self):
        print('Case 4: addLast in an empty list')
        self.lEmpty.addLast(10)
        expected=[10]
        self.assertEqual(str(self.lEmpty), str(expected),"Fail: addLast an empty list")
        print()
        
    def test5_addLast(self):
        print('Case 5: addLast in a list of size 1')
        self.l1.addLast(3)
        expected=[5,3]
        self.assertEqual(str(self.l1), str(expected),"Fail: addLast in a list of length==1")
        print()
        
    def test6_addLast(self):
        print('Case 6: addLast in a list with lenght>1')
        self.l4.addLast(5)
        expected=[1,8,3,1,5]
        self.assertEqual(str(self.l4), str(expected),"Fail: addLast in a list of length>0")
        print()

    def test7_removeFirst(self):
        print('Case 7: removeFirst in an empty list')
        first=self.lEmpty.removeFirst()

        expected=[]
        self.assertEqual(first, None, "Fail: removeFirst in a list of length==0")
        self.assertEqual(str(self.lEmpty), str(expected), "Fail: removeFirst in a list of length == 0")

    def test8_removeFirst(self):
        print('Case 7: remvoveFirst in a list of length 1')
        
        first=self.l1.removeFirst()
        expected=[]
        self.assertEqual(first, 5, "Fail: removeFirst in a list of length>1")
        self.assertEqual(str(self.l1), str(expected), "Fail: removeFirst in a list of length == 1")
    
    def test9_removeFirst(self):
        print('Case 9: removeFirst in a list of length >1')
        top_expected = self.l4.removeFirst()
        expected=[8,3,1]

        self.assertEqual(top_expected, 1, "Fail: removeFirst in a list of length>1")
        self.assertEqual(str(self.l4), str(expected), "Fail: removeFirst in a list of length>1")
        print()

    def test_10_removeLast(self):
        print('Case 10: removeLast in an empty list')
        top_expected=self.lEmpty.removeLast()
        expected=[]
        self.assertEqual(top_expected, None, "Fail: removeLast in an empty list")

        self.assertEqual(str(self.lEmpty), str(expected), "Fail: removeLast in an empty list")

    def test_11_removeLast(self):
        print('Case 11: removeLast in a list of length 1')
        top_expected=self.l1.removeLast()
        expected=[]
        self.assertEqual(top_expected, 5, "Fail: removeLast in a list of length==1")
        self.assertEqual(str(self.l1), str(expected), "Fail: removeLast in a list of length == 1")
    
    def test_12_removeLast(self):
        print('Case 12: removeLast in a list with length > 1')
        top_expected=self.l4.removeLast()
        expected=[1,8,3]
        self.assertEqual(top_expected, 1, "Fail: removeLast in a list of length>1")
        self.assertEqual(str(self.l4), str(expected), "Fail: removeLast in a list of length > 1")
        print()

    def test_13_getAt(self):
        print('Case 13: getAt')
        expected=[1,8,3,1]
        for i in range(len(self.l4)):
            self.assertEqual(self.l4.getAt(i), expected[i], "Fail: front in a dequeue empty")

    def test_14_index(self):
        print('Case 14: index of an element that does not exist')
        self.assertEqual(self.l4.index(33), -1, "Fail: index of an element")

    def test_15_index(self):
        print('Case 15: index of an element does  exist')
        self.assertEqual(self.l4.index(8), 1, "Fail: index of an element")
        self.assertEqual(self.l4.index(1), 0, "Fail: index of an element")
        self.assertEqual(self.l4.index(3), 2, "Fail: index of an element")
    
    def test_16_insertAt(self):
        print('Case 16: insertAt(0,2) Index=0, elem=2')
        self.l4.insertAt(0,2)
        expected=[2,1,8,3,1]
        self.assertEqual(str(self.l4), str(expected), "Fail: 15: insertAt(0,C) ")

    def test_17_insertAt(self):
        print('Case 17: insertAt(len,7) Index=len, elem=7')
        self.l4.insertAt(4,7)
        expected=[1,8,3,1,7]
        self.assertEqual(str(self.l4), str(expected), "Fail: 16: insertAt(len(l4),.) ")

    def test_18_insertAt(self):
        print('Case 18: insertAt(2,7) in the middle; index=2, elem=7')
        self.l4.insertAt(2,7)
        expected=[1,8,7,3,1]
        self.assertEqual(str(self.l4), str(expected), "Fail: 'Case 17: insertAt(2,C) ")

    def test_19_insertAt(self):
        print('Case 19: insertAt(7,7) in a wrong position')
        self.l4.insertAt(7,7)
        expected=[1,8,3,1]
        self.assertEqual(str(self.l4), str(expected), "Fail: Case 19: insertAt(7,7) in a wrong position")
        
        
    def test_20_insertAt(self):
        print('Case 20: insert at an empty list')
        self.lEmpty.insertAt(0,7)
        expected=[7]
        self.assertEqual(str(self.lEmpty), str(expected), "Fail: Case 20: insert at an empty list")    
        
        
    def test_21_removeAt(self):
        print('Case 21: removeAt(len), index=out of range')
        
        result=self.l4.removeAt(4)
        self.assertEqual(result, None, "Case 21: removeAt(len), index=out of range")

        expected=[1,8,3,1]
        self.assertEqual(str(self.l4), str(expected), "Case 21: removeAt(len), index=out of range")

    def test_22_removeAt(self):
        print('Case 22: removeAt(2) index=2')
        result=self.l4.removeAt(2)
        self.assertEqual(result, 3, "Fail: Case 22: removeAt(2) rindex=2")
        
        expected=[1,8,1]
        self.assertEqual(str(self.l4), str(expected), "Fail: Case 22: removeAt(2) rindex=2")
        
        
    def test_23_remveAt(self):
        print('Case 23: removeAt(0) index=0')
        result=self.l4.removeAt(0)
        self.assertEqual(result, 1, "Case 23: removeAt(0) rindex=0")
        expected=[8,3,1]
        self.assertEqual(str(self.l4), str(expected), "Case 23: removeAt(0) rindex=0")
        
   
    def test_24_remveAt(self):
        print('Case 24: removeAt(len-1) index=len-1')
        result=self.l4.removeAt(len(self.l4)-1)
        self.assertEqual(result, 1, "Fail: Case 24: removeAt(len-1) index=len-")

        expected=[1,8,3]
        self.assertEqual(str(self.l4), str(expected), "Fail: Case 24: removeAt(len-1) index=len-1")
        
    def test_25_remveAt(self):
        print('Case 25: removeAt(0) in a list of length == 1')
        result=self.l1.removeAt(0)
        self.assertEqual(result, 5, "Fail: Case 25: removeAt(0) in a list of length == 1")

        expected=[]
        self.assertEqual(str(self.l1), str(expected), "Fail: Case 25: removeAt(0) in a list of length == 1")
        
    def test_26_remveAt(self):
        print('Case 26: removeAt(0) in an empty list')
        result=self.lEmpty.removeAt(0)
        self.assertEqual(result, None, "Fail: Case 26: removeAt(0) in an empty list")

        expected=[]
        self.assertEqual(str(self.lEmpty), str(expected), "Fail: Case 26: removeAt(0) in an empty list")



#If you are using Spyder, please comment the following line: 
#unittest.main(argv=['first-arg-is-ignored'], exit=False)

#To use Spyder, remove the following comments:
if __name__ == '__main__':
    unittest.main()