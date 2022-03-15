#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from partial_84_solution import MySList

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
      #empty lists
      self.listE1 = MySList()
      self.listE2 = MySList()

      # data1 will be a sorted array without duplicates
      data1 = []
      for i in range(5):
        x = random.randint(0, 10)
        data1.append(x)
        if i%2==0:  #we create some duplicates
          data1.append(x)
          data1.append(x)

      data1.sort()
      #print("data1:", data1)
      # create a SList sorted and with duplicates
      self.l1Dupli = MySList()
      for x in data1:
        self.l1Dupli.append(x)
      # print("l1 with duplicates:", str(self.l1Dupli))

      # remove duplicates from data
      data1=list(set(data1))
      #we have to sort again
      data1.sort()
      #print("data1 after removing duplicates:", data1)

      # create a SList sorted and without duplicates
      self.l1 = MySList()
      for x in data1:
        self.l1.append(x)
      # print("l1 no duplicates:", str(self.l1))

      # data2 will be a sorted array without duplicates
      data2 = []
      for i in range(10):
        x = random.randint(0, 10)
        data2.append(x)
        if i%2!=0:  #we create some duplicates
          data2.append(x)
          data2.append(x)
      data2=sorted(data2)
      #print("data2:", data2)

      # now we create a SList sorted and with duplicates
      self.l2Dupli = MySList()
      for x in data2:
        self.l2Dupli.append(x)
      # print("l2 with duplicates:", str(self.l2Dupli))

      #remove duplicates from data2
      data2=list(set(data2))
      data2.sort()

      # print("data2 after removing duplicates:", data2)
      self.l2 = MySList()
      for x in data2:
        self.l2.append(x)
      #print("l2 no duplicates:", str(self.l2))

      self.datamerge = list(set(data1 + data2))
      self.datamerge.sort()
      # print("merge list:", self.datamerge)

      self.l3 = MySList()
      for i in range(10):
        self.l3.append(random.randint(0, 20))
      # print("l3 no sorted: ", str(self.l3))
      self.l4 = MySList()
      for i in range(10):
        self.l4.append(i)
      # print("l4:", self.l4)
      # print()

    def test_printNota(self):
      print("Nota provisional: ", Test.notaprovisional)


    def test1(self):
      print('Caso 1. Dos listas vacías')
      expected=[]
      result=self.listE1.merge(self.listE2)

      # print('first list: ', str(self.listE1))
      # print('second list: ', str(self.listE2))
      # print("List merged:" , str(result))
      # print("expected:" , str(expected))
      # print()
      self.assertEqual(str(result),str(expected),"Fail: test1")
      Test.notaprovisional+=0.5


    def test2(self):
      print('Caso 2. Primera lista no está ordenada')
      result=self.l3.merge(self.l1)

      # print('first list: ', str(self.l3))
      # print('second list: ', str(self.l1))
      # print("List merged:" , str(result))
      # print("expected:" , None)
      # print()
      self.assertIsNone(result,"Fail: test2")
      Test.notaprovisional+=0.5


    def test3(self):
      print('Caso 3. Segunda lista no está ordenada')
      result=self.l1.merge(self.l3)

      # print('first list: ', str(self.l1))
      # print('second list: ', str(self.l3))
      # print("List merged:" , str(result))
      # print("expected:" , None)

      self.assertIsNone(result,"Fail: test3")
      Test.notaprovisional+=0.5

    def test4(self):
      print('Caso 4. Primera lista vacia, segunda lista no vacía sin duplicados')
      expected=self.l2
      result=self.listE1.merge(self.l2)

      # print('first list: ', str(self.listE1))
      # print('second list: ', str(self.l2))
      # print("List merged:" , str(result))
      # print("expected:" , str(expected))
      # print()

      self.assertEqual(str(result),str(expected),"Fail: test4")
      Test.notaprovisional+=0.5

    def test5(self):
      print('Caso 5. Primera lista vacia, segunda lista no vacía con duplicados')
      expected=self.l2
      result=self.listE1.merge(self.l2Dupli)

      # print('first list: ', str(self.listE1))
      # print('second list: ', str(self.l2Dupli))
      # print("List merged:" , str(result))
      # print("expected:" , str(expected))

      self.assertEqual(str(result),str(expected),"Fail: test5")
      Test.notaprovisional+=1.5

    def test6(self):
      print('Caso 6. Primera lista no vacía sin duplicados, segunda lista  vacía ')
      expected=self.l1
      result=self.l1.merge(self.listE2)

      # print('first list: ', str(self.l1))
      # print('second list: ', str(self.listE2))
      # print("List merged:" , str(result))
      # print("expected:" , str(expected))

      self.assertEqual(str(result),str(expected),"Fail: test6")
      Test.notaprovisional+=0.5

    def test7(self):
      print('Caso 7. Primera lista no vacía con duplicados, segunda lista  vacía ')
      expected=self.l1
      result=self.l1Dupli.merge(self.listE2)

      # print('first list: ', str(self.l1Dupli))
      # print('second list: ', str(self.listE2))
      # print("List merged:" , str(result))
      # print("expected:" , str(expected))

      self.assertEqual(str(result),str(expected),"Fail: test7")
      Test.notaprovisional+=1.5

    def test8(self):
      print('Caso 8. Dos listas ordenadas sin duplicados. Primera menos longitud')
      expected=self.datamerge
      result=self.l1.merge(self.l2)

      # print('first list: ', str(self.l1))
      # print('second list: ', str(self.l2))
      # print("List merged:" , str(result))
      # print("expected:" , str(expected))

      self.assertEqual(str(result),str(expected),"Fail: test8")
      Test.notaprovisional+=1.25

    def test9(self):
      print('Caso 9. Dos listas ordenadas sin duplicados. Segunda menos longitud')
      expected=self.datamerge
      result=self.l2.merge(self.l1)

      # print('first list: ', str(self.l2))
      # print('second list: ', str(self.l1))
      # print("List merged:" , str(result))
      # print("expected:" , str(expected))

      self.assertEqual(str(result),str(expected),"Fail: test9")
      Test.notaprovisional+=1.25

    def test10(self):
      print('Caso 10. Dos listas ordenadas con duplicados. Primera menos longitud')
      expected=self.datamerge
      result=self.l1Dupli.merge(self.l2Dupli)

      #print('first list: ', str(self.l1Dupli))
      #print('second list: ', str(self.l2Dupli))
      #print("List merged:" , str(result))
      #print("expected:" , str(expected))

      self.assertEqual(str(result),str(expected),"Fail: test10")
      Test.notaprovisional+=1.5


    def test11(self):
      print('Caso 11. Dos listas ordenadas con duplicados. Segunda menos longitud')
      expected=self.datamerge
      result=self.l2Dupli.merge(self.l1Dupli)

      # print('first list: ', str(self.l2Dupli))
      # print('second list: ', str(self.l1Dupli))
      # print("List merged:" , str(result))
      # print("expected:" , str(expected))

      self.assertEqual(str(result),str(expected),"Fail: test11")
      Test.notaprovisional+=1.5


    def test12(self):
      print('Caso 12. la misma lista con duplicados')
      expected=self.l1
      result=self.l1Dupli.merge(self.l1Dupli)

      #print('first list: ', str(self.l1Dupli))
      #print('second list: ', str(self.l1Dupli))
      #print("List merged:" , str(result))
      #print("expected:" , str(expected))

      self.assertEqual(str(result),str(expected),"Fail: test12")
      Test.notaprovisional+=1



    def test13(self):
      print('Caso 13. Primera con duplicados, segunda sin duplicados')
      expected=self.datamerge
      result=self.l1Dupli.merge(self.l2)

      # print('first list: ', str(self.l1Dupli))
      # print('second list: ', str(self.l2))
      # print("List merged:" , str(result))
      # print("expected:" , str(expected))

      self.assertEqual(str(result),str(expected),"Fail: test13")
      Test.notaprovisional+=1.5



    def test14(self):
      print('Caso 14. Primera sin duplicados, segunda con duplicados')
      expected=self.datamerge
      result=self.l1.merge(self.l2Dupli)

      # print('first list: ', str(self.l1))
      # print('second list: ', str(self.l2Dupli))
      # print("List merged:" , str(result))
      # print("expected:" , str(expected))

      self.assertEqual(str(result),str(expected),"Fail: test14")
      Test.notaprovisional+=1.5




#Descomentar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()

