#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from second84 import MyBinarySearchTree

import unittest
import random

class Test(unittest.TestCase):
    """
      - test1: input dos listas vacías, output: lista vacía
      - test2: primera lista no ordenada, output: None
      - test3: segunda lista no ordenada, output: None
      - test4: primera lista vacia, segunda lista no vacía sin duplicados
      - test5: primera lista vacia, segunda lista no vacía con duplicados
      - test6: primera no vacia sin duplicados, segunda lista  vacía
      - test7: primera no vacía con duplicados, segunda lista no vacía
      - test8: Dos listas ordenadas sin duplicados. Primera menos longitud
      - test9: Dos listas ordenadas sin duplicados. Segunda menos longitud
      - test10: Dos listas ordenadas con duplicados. Primera menos longitud
      - test11: Dos listas ordenadas con duplicados. Segunda menos longitud
      - test12: la misma lista con duplicados
      - test13: Primera con duplicados, segunda sin duplicados
      - test14: Primera sin duplicados, segunda con duplicados
   """
    notaprovisional=0

    def setUp(self):
      #empty trees
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

    def test_printNota(self):
      print("Nota provisional: ", Test.notaprovisional)

    def test1(self):
      print('Caso 1. Valores min y max fuera de rango de valores del arbol ')
      expected=[]
      result=self.tree.removeOutsideRange3(1,120)

      self.assertEqual(str(result),str(expected),"Fail: test1")
      Test.notaprovisional+=0.5

    def test2(self):
        print('Caso 2. Valores min y max dentro de rango de valores del arbol')
        expected = [5, 24, 54, 80]
        result = self.tree.removeOutsideRange3(15, 20)

        self.assertEqual(str(result), str(expected), "Fail: test2")
        Test.notaprovisional += 0.5

    def test3(self):
        print('Caso 3. Árbol vacío ')
        expected = []
        result = self.tree3.removeOutsideRange3(15, 20)

        self.assertEqual(str(result), str(expected), "Fail: test3")
        Test.notaprovisional += 0.5

    def test4(self):
        print('Caso 4. Valor min fuera de rango de valores del arbol')
        expected = [24, 54, 80]
        result = self.tree.removeOutsideRange3(0, 20)

        self.assertEqual(str(result), str(expected), "Fail: test4")
        Test.notaprovisional += 0.5

    def test5(self):
        print('Caso 5. Valor max fuera de rango de valores del arbol')
        expected = [5]
        result = self.tree.removeOutsideRange3(15, 200)

        self.assertEqual(str(result), str(expected), "Fail: test5")
        Test.notaprovisional += 0.5

#Descomentar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()

