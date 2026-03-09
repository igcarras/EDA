from Ejercicio1 import DList2

import unittest

class Test(unittest.TestCase):

    def setUp(self):

        self.lEmpty = DList2()

        self.l1 = DList2()
        self.l1.addFirst(2)

        self.l2 = DList2()
        self.l2.addLast(1)
        self.l2.addLast(2)
        self.l2.addLast(3)
        self.l2.addLast(4)
        self.l2.addLast(5)

        self.l3 = DList2()
        self.l3.addLast(2)
        self.l3.addLast(2)
        self.l3.addLast(2)
        self.l3.addLast(2)

        self.l4 = DList2()
        self.l4.addLast(6)
        self.l4.addLast(4)
        self.l4.addLast(2)

        self.l5 = DList2()
        self.l5.addLast(1)
        self.l5.addLast(1)

    def test1(self):
        print('Case 1: longitud de la lista es ==0')
        expected = []
        result = self.lEmpty.copy_node_next(5)
        self.assertEqual(str(self.lEmpty),str(expected), "Fail: La lista no está vacía")
        self.assertEqual(len(self.lEmpty), len(expected), "Fail: La longitud de la lista es==0")

    def test2(self):
        print('Case 2: se duplican los primeros elementos de la lista')
        expected = [1,1,2,2,3,4,5]
        result = self.l2.copy_node_next(3)
        self.assertEqual(str(self.l2),str(expected), "Fail: La lista no es la esperada")
        self.assertEqual(len(self.l2), len(expected), "Fail: La longitud de la lista no es la esperada")
        self.assertEqual(result, 2, "Fail: Número de elementos duplicados no correcto")

    def test3(self):
        print('Case 3: No se duplican los elementos de la lista')
        expected = [1,2,3,4,5]
        result = self.l2.copy_node_next(1)
        self.assertEqual(str(self.l2),str(expected), "Fail: La lista no es la esperada")
        self.assertEqual(len(self.l2), len(expected), "Fail: La longitud de la lista no es la esperada")
        self.assertEqual(result, 0, "Fail: Número de elementos duplicados no correcto")

    def test4(self):
        print('Case 4: Se duplican todos los elementos de la lista')
        expected = [1,1,2,2,3,3,4,4,5,5]
        result = self.l2.copy_node_next(8)
        self.assertEqual(str(self.l2),str(expected), "Fail: La lista no es la esperada")
        self.assertEqual(len(self.l2), len(expected), "Fail: La longitud de la lista no es la esperada")
        self.assertEqual(result, 5, "Fail: Número de elementos duplicados no correcto")


    def test5(self):
        print('Case 5: Todos los elementos de la lista se duplican')
        expected = [2]*8
        result = self.l3.copy_node_next(3)
        self.assertEqual(str(self.l3), str(expected), "Fail: La lista no es la esperada")
        self.assertEqual(len(self.l3), len(expected), "Fail: La longitud de la lista no es la esperada")
        self.assertEqual(result, 4, "Fail: Número de elementos duplicados no correcto")

    def test6(self):
        print('Case 6: Ninguno de los elementos de la lista se duplican')
        expected = [2]*4
        result = self.l3.copy_node_next(1)
        self.assertEqual(str(self.l3), str(expected), "Fail: La lista no es la esperada")
        self.assertEqual(len(self.l3), len(expected), "Fail: La longitud de la lista no es la esperada")
        self.assertEqual(result, 0, "Fail: Número de elementos duplicados no correcto")

    def test7(self):
        print('Case 7: Ninguno de los elementos de la lista se duplican')
        expected = [6,4,2]
        result = self.l4.copy_node_next(1)
        self.assertEqual(str(self.l4), str(expected), "Fail: La lista no es la esperada")
        self.assertEqual(len(self.l4), len(expected), "Fail: La longitud de la lista no es la esperada")
        self.assertEqual(result, 0, "Fail: Número de elementos duplicados no correcto")

    def test8(self):
        print('Case 8: Se duplica el elemento final')
        expected = [6,4,2,2]
        result = self.l4.copy_node_next(3)
        self.assertEqual(str(self.l4), str(expected), "Fail: La lista no es la esperada")
        self.assertEqual(len(self.l4), len(expected), "Fail: La longitud de la lista no es la esperada")
        self.assertEqual(result, 1, "Fail: Número de elementos duplicados no correcto")

    def test9(self):
        print('Case 9: Se duplica el elemento central y el último')
        expected = [6,4,4,2,2]
        result = self.l4.copy_node_next(5)
        self.assertEqual(str(self.l4), str(expected), "Fail: La lista no es la esperada")
        self.assertEqual(len(self.l4), len(expected), "Fail: La longitud de la lista no es la esperada")
        self.assertEqual(result, 2, "Fail: Número de elementos duplicados no correcto")

    def test10(self):
        print('Case 10: Se duplica todos')
        expected = [6,6,4,4,2,2]
        result  =self.l4.copy_node_next(7)
        self.assertEqual(str(self.l4), str(expected), "Fail: La lista no es la esperada")
        self.assertEqual(len(self.l4), len(expected), "Fail: La longitud de la lista no es la esperada")
        self.assertEqual(result, 3, "Fail: Número de elementos duplicados no correcto")
    def test11(self):
        print('Case 11: Se duplica todos')
        expected = [1,1,1,1]
        result  =self.l5.copy_node_next(7)
        self.assertEqual(str(self.l5), str(expected), "Fail: La lista no es la esperada")
        self.assertEqual(len(self.l5), len(expected), "Fail: La longitud de la lista no es la esperada")
        self.assertEqual(result, 2, "Fail: Número de elementos duplicados no correcto")

if __name__=="__main__":
    unittest.main()
