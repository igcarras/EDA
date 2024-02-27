#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from exampartial_84_2022 import MySList

import unittest
import random

class Test(unittest.TestCase):
    def setUp(self):
      self.listE1 = MySList()
      self.listE2 = MySList()

      data1 = []
      for i in range(5):
        x = random.randint(0, 10)
        if x not in data1:
          data1.append(x)

      self.datamerge = []

      data1.sort()
      self.l1 = MySList()
      for x in data1:
        self.l1.append(x)
        if x not in self.datamerge:
          self.datamerge.append(x)

      data2 = []
      for i in range(7):
        x = random.randint(0, 10)
        if x not in data2:
          data2.append(x)

      data2.sort()

      self.l2 = MySList()
      for x in data2:
        self.l2.append(x)
        if x not in self.datamerge:
          self.datamerge.append(x)

      self.datamerge.sort()

      self.l3 = MySList()
      for i in range(10):
        self.l3.append(random.randint(0, 20))
      self.l4 = MySList()
      for i in range(10):
        self.l4.append(i)

    def test_merge1(self):
      print('Caso 1. Dos listas ordenadas sin duplicados de diferente longitud')
      expected=self.datamerge
      result=self.l1.merge(self.l2)
      print("List merged 1:" , str(result))
      self.assertEqual(str(result),str(expected))

    def test_merge2(self):
      print('Caso 2. Dos listas ordenadas sin duplicados de diferente longitud')
      expected = self.datamerge
      result = self.l2.merge(self.l1)
      print("List merged 2:", str(result))
      self.assertEqual(str(result), str(expected))

    def test_merge3(self):
      print('Caso 3. Dos listas vacias')
      expected="]"
      result=self.listE1.merge(self.listE2)
      print("List merged 3:" , str(result))
      self.assertEqual(str(result),str(expected))

    def test_merge4(self):
      print('Caso 4. Primera lista vacia')
      expected=self.l2
      result=self.listE1.merge(self.l2)
      print("List merged 4:" , str(result))
      self.assertEqual(str(result),str(expected))

    def test_merge5(self):
      print('Caso 5. Segunda lista vacia')
      expected=self.l1
      result=self.l1.merge(self.listE1)
      print("List merged 5:" , str(result))
      self.assertEqual(str(result),str(expected))

    def test_merge6(self):
      print('Caso 6. Listas sin ordenar')
      expected=None
      result=self.l3.merge(self.l4)
      print("List merged 6:" , str(result))
      self.assertEqual(str(result),str(expected))

    def test_merge7(self):
      print('Caso 7. Dos listas ordenadas de igual longitud sin duplicados')
      expected=None
      result=self.l3.merge(self.l4)
      print("List merged 7:" , str(result))
      self.assertEqual(str(result),str(expected))

    def test_merge8(self):
      print('Caso 8. Dos listas iguales')
      expected=self.l1
      result=self.l1.merge(self.l1)
      print("List merged 8:" , str(result))
      self.assertEqual(str(result),str(expected))

#Descomenar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()
    
