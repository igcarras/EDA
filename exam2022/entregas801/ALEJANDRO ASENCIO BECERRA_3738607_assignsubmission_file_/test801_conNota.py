#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from partial_801 import MySList

import unittest
import random

"""
    - test1: Dos listas ordenadas sin duplicados de diferente longitud
    - test2: Dos listas ordenadas sin duplicados de diferente longitud
    - test3: Dos listas vacias
    - test4: Primera lista vacia
    - test5: Segunda lista vacia
    - test6: Dos listas sin ordenar
    - test7: Primera lista sin ordenar
    - test8: Segunda lista sin ordenar
    - test9: Dos listas ordenadas iguales sin duplicados
    - test10: Dos listas ordenadas iguales con duplicados
    - test11: Dos listas ordenadas, primera con duplicados y menos longitud
    - test12: Dos listas ordenadas, segunda con duplicados y menos longitud
 """

class Test(unittest.TestCase):
    notaprovisional = 0

    def setUp(self):
        #empty lists
        self.listE1 = MySList()
        self.listE2 = MySList()

        data1 = []
        for i in range(5):
            x = random.randint(0, 10)
            if x not in data1:
                data1.append(x)

        #lista l1 está ordenada
        data1.sort()
        self.l1 = MySList()
        for x in data1:
            self.l1.append(x)

        data2 = []
        for i in range(7):
            x = random.randint(0, 10)
            if x not in data2:
                data2.append(x)
        data2.sort()

        self.datasubs = []
        self.datasubs2 = []

        # lista l2 está ordenada
        self.l2 = MySList()
        for x in data2:
            self.l2.append(x)
            self.datasubs2.append(0)

        contador=min(len(data1), len(data2))
        for i in range(0, contador):
            if data1[i]<=data2[i]:
                self.datasubs.append(data2[i]-data1[i])
            else:
                self.datasubs.append(data1[i]-data2[i])

        if len(data1) <= len(data2):
            for i in range(len(data1),len(data2)):
               self.datasubs.append(data2[i])
        else:
            for i in range(len(data2), len(data1)):
               self.datasubs.append(data1[i])

        self.l3 = MySList()
        #lista l3 NO está ordenada y puede tener duplicados
        for i in range(10):
            self.l3.append(random.randint(0, 20))

        self.l4 = MySList()
        # lista l4 NO está ordenada y puede tener duplicados
        for i in range(6):
            self.l4.append(random.randint(0, 20))

        self.datasubs3 = []
        self.l5 = MySList()
        #lista l5 está ordenada y tiene duplicados
        for i in range(3):
            self.l5.append(i)
            self.l5.append(i)
            self.datasubs3.append(0)
            self.datasubs3.append(0)

        self.l6 = MySList()
        self.datasubs4 = [10,11,11,12,12,13,16]
        # lista l6 está ordenada y no tiene duplicados
        for i in range(10,17):
            self.l6.append(i)

    def test_subtraction1(self):
        print('Caso 1. Dos listas ordenadas sin duplicados, primera menos longitud')
        expected = self.datasubs
        result = self.l1.subtraction(self.l2)
        #print("List subtraction1:", str(result))
        self.assertEqual(str(result), str(expected), "Fail: test1")
        Test.notaprovisional += 1.5

    def test_subtraction2(self):
        print('Caso 2. Dos listas ordenadas sin duplicados, segunda menos longitud')
        expected = self.datasubs
        result = self.l2.subtraction(self.l1)
        #print("List subtraction2:", str(result))
        self.assertEqual(str(result), str(expected), "Fail: test2")
        Test.notaprovisional += 1.5

    def test_subtraction3(self):
        print('Caso 3. Dos listas vacias')
        expected = []
        result = self.listE1.subtraction(self.listE2)
        #print("List subtraction3:", str(result))
        self.assertEqual(str(result), str(expected), "Fail: test3")
        Test.notaprovisional += 0.5

    def test_subtraction4(self):
        print('Caso 4. Primera lista vacia')
        expected = self.l2
        result = self.listE1.subtraction(self.l2)
        print(self.l2)
        print("List subtraction4:", str(result))
        self.assertEqual(str(result), str(expected), "Fail: test4")
        Test.notaprovisional += 1.25

    def test_subtraction5(self):
        print('Caso 5. Segunda lista vacia')
        expected = self.l1
        result = self.l1.subtraction(self.listE1)
        #print("List subtraction5:", str(result))
        self.assertEqual(str(result), str(expected), "Fail: test5")
        Test.notaprovisional += 1.25

    def test_subtraction6(self):
        print('Caso 6. Dos listas sin ordenar')
        result = self.l3.subtraction(self.l4)
        #print("List subtraction6:", str(result))
        self.assertIsNone(result, "Fail: test6")
        Test.notaprovisional += 0.75

    def test_subtraction7(self):
        print('Caso 7. Primera lista sin ordenar')
        result = self.l3.subtraction(self.l1)
        #print("List subtraction7:", str(result))
        self.assertIsNone(result, "Fail: test7")
        Test.notaprovisional += 1.25

    def test_subtraction8(self):
        print('Caso 8. Segunda lista sin ordenar')
        result = self.l1.subtraction(self.l4)
        #print("List subtraction8:", str(result))
        self.assertIsNone(result, "Fail: test8")
        Test.notaprovisional += 1.25

    def test_subtraction9(self):
        print('Caso 9. Dos listas ordenadas iguales sin duplicados')
        expected = self.datasubs2
        result = self.l2.subtraction(self.l2)
        #print("List subtraction9:", str(result))
        self.assertEqual(str(result), str(expected), "Fail: test9")
        Test.notaprovisional += 1.25

    def test_subtraction10(self):
        print('Caso 10. Dos listas ordenadas iguales con duplicados')
        expected = self.datasubs3
        result = self.l5.subtraction(self.l5)
        #print("List subtraction10:", str(result))
        self.assertEqual(str(result), str(expected), "Fail: test10")
        Test.notaprovisional += 1.5

    def test_subtraction11(self):
        print('Caso 11. Dos listas ordenadas, primera con duplicados y menos longitud')
        expected = self.datasubs4
        result = self.l6.subtraction(self.l5)
        #print("List subtraction10:", str(result))
        self.assertEqual(str(result), str(expected), "Fail: test11")
        Test.notaprovisional += 1.5

    def test_subtraction12(self):
        print('Caso 12. Dos listas ordenadas, segunda con duplicados y menos longitud')
        expected = self.datasubs4
        result = self.l5.subtraction(self.l6)
        # print("List subtraction10:", str(result))
        self.assertEqual(str(result), str(expected), "Fail: test12")
        Test.notaprovisional += 1.5

    def test_zprintNota(self):
        print("Nota provisional: ", Test.notaprovisional)

# Descomentar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()


