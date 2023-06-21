from bst import BinarySearchTree

class MyBST(BinarySearchTree):

    def mac(self,a,b):
        """returns the lowest common ancestor of a and b"""
        nodeA=self.search(a)
        if nodeA is None:
            return None
        
        nodeB=self.search(b)
        if nodeB is None:
            return None

        if nodeB is self._root or nodeA is self._root:
            return None

        return self._mac(self._root,nodeA,nodeB)

    def _mac(self,node,nodeA,nodeB):
        if node is None:
            return None

        if nodeA.elem<node.elem and nodeB.elem<node.elem:
            if node.left is not nodeA and node.left is not nodeB:
                return self._mac(node.left,nodeA,nodeB)

        if nodeA.elem>node.elem and nodeB.elem>node.elem:
            if node.right is not nodeA and node.right is not nodeB:
                return self._mac(node.right,nodeA,nodeB)


        return node.elem

import random

if __name__ == '__main__':
    tree=MyBST()
    values=[50,48,70,30,65,90,20,32,67,98,15,25,31,35,66,69,94,99]

    tree=MyBST()
    for x in values:
        tree.insert(x)

    tree.draw()

    print(tree.mac(48,70),50)
    print(tree.mac(30,70),50)
    print(tree.mac(30,65),50)
    print(tree.mac(20,32),30)
    print(tree.mac(67,90),70)
    print(tree.mac(69,99),70)
    print(tree.mac(31,94),50)
    print(tree.mac(15,25),20)
    print(tree.mac(15,35),30)
    print(tree.mac(67,70),50)
    print(tree.mac(30,35),48)
    print(tree.mac(90,94),70)
    print(tree.mac(20,30),48)
    print(tree.mac(67,70),50)
    print(tree.mac(48,50),"None")

# import unittest
#
# class Test(unittest.TestCase):
#
#     #provisional mark
#     mark=0
#
#     def setUp(self):
#         values=[50,48,70,30,65,90,20,32,67,98,15,25,31,35,66,69,94,99]
#         self.bst=MyBST()
#         for x in values:
#             self.bst.insert(x)
#
#
#     def testz_printNota(self):
#         print('\n\n*************************')
#         print("\t Provisional mark:",Test.mark)
#         print('*************************')
#
#     def test1_lwc(self):
#         print('Case 1: a does not exist')
#         self.assertEqual(self.bst.mac(21,50),None)
#         print('\t\t mark += 1')
#         Test.mark+=1
#
#     def test2_lwc(self):
#         print('Case 2: b does not exist')
#         self.assertEqual(self.bst.mac(50,100),None)
#         print('\t\t mark += 1')
#         Test.mark+=1
#
#     def test3_lwc(self):
#         print('Case 3: tree is empty')
#         empty=MyBST()
#         self.assertEqual(empty.mac(58,70),None)
#         print('\t\t mark += 1')
#         Test.mark+=1
#
#     def test4_lwc(self):
#         print('Case 4: a=30,b=90')
#         self.assertEqual(self.bst.mac(30,90),50)
#         print('\t\t mark += 2')
#         Test.mark+=2
#
#     def test5_lwc(self):
#         print('Case 5: a=67,b=98, same depth')
#         self.assertEqual(self.bst.mac(67,98),70)
#         print('\t\t mark += 2.5')
#         Test.mark+=2.5
#
#     def test6_lwc(self):
#         print('Case 6: a=15,b=32, different depth')
#         self.assertEqual(self.bst.mac(15,32),30)
#         print('\t\t mark += 2.5')
#         Test.mark+=2.5
#
#
#     def test7_lwc(self):
#         print('Case 7: a=15, b=35')
#         self.assertEqual(self.bst.mac(15,35),30)
#         print('\t\t mark += 2.5')
#         Test.mark+=2.5
#
#     def test8_lwc(self):
#         print('Case 8: a=67, b=99')
#         self.assertEqual(self.bst.mac(67,99),70)
#         print('\t\t mark += 2.5')
#         Test.mark+=2.5
#
#     def test9_lwc(self):
#         print('Case 9: a is the lowest common ancestor')
#         self.assertEqual(self.bst.mac(90,94),90)
#         print('\t\t mark += 2.5')
#         Test.mark+=2.5
#
#     def test10_lwc(self):
#         print('Case 10: b is the lowest common ancestor')
#         self.assertEqual(self.bst.mac(20,30),30)
#         print('\t\t mark += 2.5')
#         Test.mark+=2.5
#
#
# #Comentar para usarlo en google colab
# #unittest.main(argv=['first-arg-is-ignored'], exit=False)
#
# #Descomenar para usarlo en Spyder
# if __name__ == '__main__':
#     unittest.main()