
from problem1_skeleton import MyDList

import unittest #package that contains the classes t

class Test(unittest.TestCase):
    
    '''
    Case 1: list empty
    Case 2: list is not sorted
    Case 3: list with 1 node
    Case 4: list with zeros
    Case 5: a complete list
    '''
    
    def setUp(self):
        """This functions is executed for each of the test functions"""
        self.l2=MyDList()
        self.data=[9, 4, 4, 6, 3, 12, 2, 1]
        for x in self.data:
            self.l2.append(x)

        self.l3=MyDList()
        self.l3.append(11)
        
        self.l4=MyDList()
        self.data=[0, 0, 0, 1, 1, 3, 3, 3, 5, 6, 7, 8, 11,12, 13, 15, 16]
        for x in self.data:
            self.l4.append(x)
        
        
        self.l5=MyDList()
        self.data=[1, 1, 2, 2, 4, 5, 7, 7, 8, 9, 9, 10, 10, 13, 14]
        for x in self.data:
            self.l5.append(x)
        
        
    def test1_removeDividers(self):
        print('\nCase 1: list empty')
        self.empty=MyDList()
        self.empty.removeDividers()
        expected=[]
        self.assertEqual(str(self.empty), str(expected), 'Fail: Case 1:')
        self.assertEqual(len(self.empty), len(expected), 'Fail: Case 1:')

        print('Case 1: OK')
                
    def test2_removeDividers(self):
        print('\nCase 2: list is not sorted')
        expected=[9, 4, 4, 6, 3, 12, 2, 1]
        self.l2.removeDividers()
        self.assertEqual(str(self.l2), str(expected), 'Fail: Case 2')
        self.assertEqual(len(self.l2), len(expected), 'Fail: Case 2')
        self.assertEqual(self.l2._tail.elem, expected[-1], 'Fail: Case 2')


        print('Case 2: OK')

    def test3_removeDividers(self):
        print('\nCase 3: list with 1 node')
        expected=[11]
        self.l3.removeDividers()
        self.assertEqual(str(self.l3), str(expected), 'Fail: Case 3')
        self.assertEqual(len(self.l3), len(expected), 'Fail: Case 3')
        self.assertEqual(self.l3._tail.elem, expected[-1], 'Fail: Case 2')

        print('Case 3: OK')

    def test4_removeDividers(self):
        print('\nCase 4: list with zeros')
        expected=[0, 0, 0, 7, 11,12, 13, 15, 16]
        self.l4.removeDividers()
        self.assertEqual(str(self.l4), str(expected), 'Fail: Case 4')
        self.assertEqual(len(self.l4), len(expected), 'Fail: Case 4')
        self.assertEqual(self.l4._tail.elem, expected[-1], 'Fail: Case 2')

        print('Case 4: OK')

    def test5_removeDividers(self):
        print('\nCase 5: a complete list')
        expected=[8, 9, 10, 13, 14]
        self.l5.removeDividers()
        self.assertEqual(str(self.l5), str(expected), 'Fail: Case 5')
        self.assertEqual(len(self.l5), len(expected), 'Fail: Case 5')
        self.assertEqual(self.l5._tail.elem, expected[-1], 'Fail: Case 2')

        print('Case 5: OK')


#If you are using Spyder, please comment the following line: 
#unittest.main(argv=['first-arg-is-ignored'], exit=False)

#To use Spyder, remove the following comments:
if __name__ == '__main__':
    unittest.main()