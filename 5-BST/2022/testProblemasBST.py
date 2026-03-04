import unittest

from problemasBST import BST2

class Test(unittest.TestCase):

    def setUp(self):
        self.tree = BST2()
        self.data = [18, 11, 23, 5, 20, 24, 9, 15, 22, 21, 6, 8, 7]
        for x in self.data:
            self.tree.insert(x)
        # self.tree.draw()

    def test1_minimum(self):
        print("\n\ttest1_minimum")
        expected = min(self.data)
        result = self.tree.minimum()
        self.assertEqual(result, expected)
        print('\ttest1_minimum was OK!!!')

    def test2_maximum(self):
        print("\n\ttest2_maximum")
        expected = max(self.data)
        result = self.tree.maximum()
        self.assertEqual(result, expected)
        print('\ttest2_maximum was OK!!!')


    def test4_sum_elems(self):
        print("\n\ttest4_sum_Elems")
        expected = sum(self.data)
        result = self.tree.sum_elems()
        self.assertEqual(result, expected)
        print('\ttest4_sum_Elems was OK!!!')



#Descomenar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()
