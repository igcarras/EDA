#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from second84 import MyBinarySearchTree

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
    notaprovisional=0

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

    def test_printNota(self):
      print("Nota provisional: ", Test.notaprovisional)

    def test1(self):
      print('Caso 1. Valores min y max fuera de rango de valores del arbol ')
      expected=[]
      result=self.tree.removeOutsideRange(1,120)

      self.assertEqual(str(result),str(expected),"Fail: test1")
      Test.notaprovisional+=1

    def test2(self):
        print('Caso 2. Valores min y max dentro de rango de valores del arbol')
        expected = [5, 24, 54, 80]
        result = self.tree.removeOutsideRange(15, 20)

        self.assertEqual(str(result), str(expected), "Fail: test2")
        Test.notaprovisional += 1

    def test3(self):
        print('Caso 3. Valores min y max fuera de rango de valores del arbol (test 2) ')
        expected = []
        result = self.tree2.removeOutsideRange(2, 220)

        self.assertEqual(str(result), str(expected), "Fail: test3")
        Test.notaprovisional += 1

    def test4(self):
        print('Caso 4. Valores min y max dentro de rango de valores del arbol (test 2)')
        expected = [24]
        result = self.tree2.removeOutsideRange(7, 23)

        self.assertEqual(str(result), str(expected), "Fail: test4")
        Test.notaprovisional += 1

    def test5(self):
        print('Caso 5. Árbol vacío ')
        expected = []
        result = self.tree3.removeOutsideRange(15, 20)

        self.assertEqual(str(result), str(expected), "Fail: test5")
        Test.notaprovisional += 0.75

    def test6(self):
        print('Caso 6. Valor min fuera de rango de valores del arbol')
        expected = [24, 54, 80]
        result = self.tree.removeOutsideRange(0, 20)

        self.assertEqual(str(result), str(expected), "Fail: test6")
        Test.notaprovisional += 0.75

    def test7(self):
        print('Caso 7. Valor max fuera de rango de valores del arbol')
        expected = [5]
        result = self.tree.removeOutsideRange(15, 200)

        self.assertEqual(str(result), str(expected), "Fail: test7")
        Test.notaprovisional += 0.75


    def test8(self):
        print('Caso 8. Arbol con un solo nodo y se elimina')
        expected = [12]
        result = self.tree5.removeOutsideRange(15, 200)

        self.assertEqual(str(result), str(expected), "Fail: test8")
        Test.notaprovisional += 0.75


    def test9(self):
        print('Caso 9. Arbol con un solo nodo y no se elimina')
        expected = []
        result = self.tree5.removeOutsideRange(10, 200)

        self.assertEqual(str(result), str(expected), "Fail: test9")
        Test.notaprovisional += 0.75

    def test10(self):
        print('Caso 10. Valores mínimo y maximo iguales y elimina')
        expected = [7,15,21,24]
        result = self.tree2.removeOutsideRange(0, 0)

        self.assertEqual(str(result), str(expected), "Fail: test10")
        Test.notaprovisional += 0.75

    def test11(self):
        print('Caso 11. Valores mínimo y maximo en los limites de valores a borrar')
        expected = []
        result = self.tree2.removeOutsideRange(7, 24)

        self.assertEqual(str(result), str(expected), "Fail: test11")
        Test.notaprovisional += 1.5
#Descomentar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()

