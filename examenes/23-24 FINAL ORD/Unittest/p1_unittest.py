def count_ideal_couples(a: list, b: list) -> int:
   ...


import random as rand
import unittest


class TestCountIdealCouplesSlicing(unittest.TestCase):
    print("Test método count_ideal_couples_slicing()")

    def test_longitud_igual_par_impar(self):
        a = [2, 4, 6, 8]
        b = [1, 3, 5, 7]
        resultado = count_ideal_couples_slicing(a, b)
        self.assertEqual(resultado, 4)

    def test_longitud_igual_mezclado(self):
        a = [2, 4, 5, 8]
        b = [1, 3, 6, 7]
        resultado = count_ideal_couples_slicing(a, b)
        self.assertEqual(resultado, 4)

    def test_listas_vacias(self):
        a = []
        b = []
        resultado = count_ideal_couples_slicing(a, b)
        self.assertEqual(resultado, 0)

    def test_longitudes_diferentes(self):
        a = [2, 4, 6]
        b = [1, 3]
        resultado = count_ideal_couples_slicing(a, b)
        self.assertEqual(resultado, 0)

    def test_longitudes_diferentes_mezclado(self):
        a = [2, 4, 6]
        b = [1, 3, 1, 4]
        resultado = count_ideal_couples_slicing(a, b)
        self.assertEqual(resultado, 0)

    def test_sin_parejas_ideales_par(self):
        a = [2, 4, 6, 8]
        b = [2, 4, 6, 8]
        resultado = count_ideal_couples_slicing(a, b)
        self.assertEqual(resultado, 0)

    def test_sin_parejas_ideales_impar(self):
        a = [1, 3, 5, 7, 9]
        b = [1, 3, 5, 7, 9]
        resultado = count_ideal_couples_slicing(a, b)
        self.assertEqual(resultado, 0)

    def test_pareja_unica(self):
        a = [1]
        b = [2]
        resultado = count_ideal_couples_slicing(a, b)
        self.assertEqual(resultado, 1)

    def test_sin_pareja_unica(self):
        a = [2]
        b = [2]
        resultado = count_ideal_couples_slicing(a, b)
        self.assertEqual(resultado, 0)


class TestCountIdealCouplesSlicing_2(unittest.TestCase):
    print("Test método count_ideal_couples_slicing2()")

    def test_longitud_igual_par_impar(self):
        a = [2, 4, 6, 8]
        b = [1, 3, 5, 7]
        resultado = count_ideal_couples_slicing2(a, b)
        self.assertEqual(resultado, 4)

    def test_longitud_igual_mezclado(self):
        a = [2, 4, 5, 8]
        b = [1, 3, 6, 7]
        resultado = count_ideal_couples_slicing2(a, b)
        self.assertEqual(resultado, 4)

    def test_listas_vacias(self):
        a = []
        b = []
        resultado = count_ideal_couples_slicing2(a, b)
        self.assertEqual(resultado, 0)

    def test_longitudes_diferentes(self):
        a = [2, 4, 6]
        b = [1, 3]
        resultado = count_ideal_couples_slicing2(a, b)
        self.assertEqual(resultado, 0)

    def test_longitudes_diferentes_mezclado(self):
        a = [2, 4, 6]
        b = [1, 3, 1, 4]
        resultado = count_ideal_couples_slicing2(a, b)
        self.assertEqual(resultado, 0)

    def test_sin_parejas_ideales_par(self):
        a = [2, 4, 6, 8]
        b = [2, 4, 6, 8]
        resultado = count_ideal_couples_slicing2(a, b)
        self.assertEqual(resultado, 0)

    def test_sin_parejas_ideales_impar(self):
        a = [1, 3, 5, 7, 9]
        b = [1, 3, 5, 7, 9]
        resultado = count_ideal_couples_slicing2(a, b)
        self.assertEqual(resultado, 0)

    def test_pareja_unica(self):
        a = [1]
        b = [2]
        resultado = count_ideal_couples_slicing2(a, b)
        self.assertEqual(resultado, 1)

    def test_sin_pareja_unica(self):
        a = [2]
        b = [2]
        resultado = count_ideal_couples_slicing2(a, b)
        self.assertEqual(resultado, 0)


class TestCount_ideal_couples(unittest.TestCase):
    print("Test método count_ideal_couples()")

    def test_longitud_igual_par_impar(self):
        a = [2, 4, 6, 8]
        b = [1, 3, 5, 7]
        resultado = count_ideal_couples(a, b)
        self.assertEqual(resultado, 4)

    def test_longitud_igual_mezclado(self):
        a = [2, 4, 5, 8]
        b = [1, 3, 6, 7]
        resultado = count_ideal_couples(a, b)
        self.assertEqual(resultado, 4)

    def test_listas_vacias(self):
        a = []
        b = []
        resultado = count_ideal_couples(a, b)
        self.assertEqual(resultado, 0)

    def test_longitudes_diferentes(self):
        a = [2, 4, 6]
        b = [1, 3]
        resultado = count_ideal_couples(a, b)
        self.assertEqual(resultado, 0)

    def test_longitudes_diferentes_mezclado(self):
        a = [2, 4, 6]
        b = [1, 3, 1, 4]
        resultado = count_ideal_couples(a, b)
        self.assertEqual(resultado, 0)

    def test_sin_parejas_ideales_par(self):
        a = [2, 4, 6, 8]
        b = [2, 4, 6, 8]
        resultado = count_ideal_couples(a, b)
        self.assertEqual(resultado, 0)

    def test_sin_parejas_ideales_impar(self):
        a = [1, 3, 5, 7, 9]
        b = [1, 3, 5, 7, 9]
        resultado = count_ideal_couples(a, b)
        self.assertEqual(resultado, 0)

    def test_pareja_unica(self):
        a = [1]
        b = [2]
        resultado = count_ideal_couples(a, b)
        self.assertEqual(resultado, 1)

    def test_sin_pareja_unica(self):
        a = [2]
        b = [2]
        resultado = count_ideal_couples(a, b)
        self.assertEqual(resultado, 0)


if __name__ == '__main__':
    print("Inicio de los unittest")
    unittest.main()
    n = 15
    input_a = []
    input_b = []
    for i in range(n):
        input_a.append(rand.randint(0, 100))
        input_b.append(rand.randint(0, 100))

    print("lista a:", input_a)
    print("lista b:", input_b)

    print(count_ideal_couples_slicing(input_a, input_b))
    print(count_ideal_couples_slicing2(input_a, input_b))
    print(count_ideal_couples(input_a, input_b))
