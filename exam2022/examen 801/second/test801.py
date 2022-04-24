#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from second801 import MyBinarySearchTree

import unittest
import random

class Test(unittest.TestCase):
    """
'Caso 1. Valores min y max fuera de rango de valores del arbol '
'Caso 2. Valores min y max dentro de rango de valores del arbol'
'Caso 3. Valores min y max fuera de rango de valores del arbol (test 2) '
'Caso 4. Valores min y max dentro de rango de valores del arbol (test 2)'
'Caso 5. Árbol vacío ')
'Caso 6. Valor min fuera de rango de valores del arbol'
'Caso 7. Valor max fuera de rango de valores del arbol'
'Caso 8. Arbol con un solo nodo y se elimina')
'Caso 9. Arbol con un solo nodo y no se elimina'
'Caso 10. Valores mínimo y maximo iguales y elimina'
'Caso 11. Valores mínimo y maximo en los limites de valores a borrar'

   """
    def setUp(self):
      #empty tree
      self.tree = MyBinarySearchTree()
      for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        self.tree.insert(x)

      self.tree2 = MyBinarySearchTree()
      for x in [18, 11, 23, 5, 15, 20, 24, 9, 22, 21, 6, 8, 7]:
        self.tree2.insert(x)

      self.tree3 = MyBinarySearchTree()

      self.tree4 = MyBinarySearchTree()
      for x in [5, 10, 15, 20]:
        self.tree4.insert(x)

      self.tree5 = MyBinarySearchTree()
      for x in [12]:
        self.tree5.insert(x)

    def test1(self):
        print('Caso 1. Valores min y max fuera de rango de valores del arbol ')
        expected = [80, 54, 24, 18, 5]
        result = self.tree.removeInsideRange(1, 120)

        self.assertEqual(str(result), str(expected), "Fail: test1")


    def test2(self):
        print('Caso 2. Valores min y max dentro de rango de valores del arbol')
        expected = []
        result = self.tree.removeInsideRange(33, 34)

        self.assertEqual(str(result), str(expected), "Fail: test2")


    def test3(self):
        print('Caso 3. Valores min y max fuera de rango de valores del arbol (test 2) ')
        expected = [24, 21, 15, 7]
        result = self.tree2.removeInsideRange(2, 220)

        self.assertEqual(str(result), str(expected), "Fail: test3")



    def test4(self):
        print('Caso 4. Valores min y max dentro de rango de valores del arbol (test 2)')
        expected = [21, 15, 7]
        result = self.tree2.removeInsideRange(7, 23)

        self.assertEqual(str(result), str(expected), "Fail: test4")



    def test5(self):
        print('Caso 5. Árbol vacío ')
        expected = []
        result = self.tree3.removeInsideRange(15, 20)

        self.assertEqual(str(result), str(expected), "Fail: test5")



    def test6(self):
        print('Caso 6. Valor min fuera de rango de valores del arbol')
        expected = [18, 5]
        result = self.tree.removeInsideRange(0, 20)

        self.assertEqual(str(result), str(expected), "Fail: test6")



    def test7(self):
        print('Caso 7. Valor max fuera de rango de valores del arbol')
        expected = [80, 54, 24, 18]
        result = self.tree.removeInsideRange(15, 200)

        self.assertEqual(str(result), str(expected), "Fail: test7")



    def test8(self):
        print('Caso 8. Arbol con un solo nodo y no se elimina')
        expected = []
        result = self.tree5.removeInsideRange(15, 200)

        self.assertEqual(str(result), str(expected), "Fail: test8")



    def test9(self):
        print('Caso 9. Arbol con un solo nodo y se elimina')
        expected = [12]
        result = self.tree5.removeInsideRange(10, 200)

        self.assertEqual(str(result), str(expected), "Fail: test9")



    def test10(self):
        print('Caso 10. Valores mínimo y maximo iguales y no elimina')
        expected = []
        result = self.tree2.removeInsideRange(0, 0)

        self.assertEqual(str(result), str(expected), "Fail: test10")



    def test11(self):
        print('Caso 11. Valores mínimo y maximo en los limites de valores a borrar')
        expected = [24, 21, 15, 7]
        result = self.tree2.removeInsideRange(7, 24)

        self.assertEqual(str(result), str(expected), "Fail: test11")



#Descomentar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()

