
import unittest
from phase1 import SList2


class Test(unittest.TestCase):

    #setUp is a method which is ran before a test method is executed.
    #This is useful if you need some data (for example) to be present before running a test.
    def setUp(self):

        self.lEmpty = SList2()

        self.list2 = SList2()
        self.list2.addFirst(10)

        self.list3 = SList2()
        self.list3.addFirst(5)
        self.list3.addFirst(4)
        self.list3.addFirst(3)
        self.list3.addFirst(2)
        self.list3.addFirst(1)




    def test1_delLargestSeq(self):

        self.lEmpty.delLargestSeq()
        expected = str(self.lEmpty)
        self.assertEqual(str(self.lEmpty), str(expected))


    def test2_delLargestSeq(self):

        self.list2.delLargestSeq()
        expected = str(self.list2)
        self.assertEqual(str(self.lEmpty), str(expected))


    def test3_delLargestSeq(self):

        self.list3.delLargestSeq()
        expected = [1, 2, 3, 4]
        self.assertEqual(str(self.list3), str(expected))
























        
if __name__ == "__main__":
    unittest.main()