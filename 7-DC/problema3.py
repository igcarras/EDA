# -*- coding: utf-8 -*-
"""Problema3.ipynb


PROBLEMA 3 - Divide y Vencerás / Problem 1 - Divide and Conquer
Instrucciones / Instructions:

- Puntuación: 20 puntos.
- Duración: 20 minutos para desarrollar y subir tu solución a la actividad Problema 3.
- Lee antentamente el problema. Vuelve a leer el problema una segunda vez.
Después de haber leído el enunciado dos veces, si tienes alguna duda pregunta en chat de la sesión.
- Descarga el fichero problema3.py y completa tu solución.
- En ningún caso puedes modificar, la función Test de unittest.
 
- Cuando queden 5 minutos el profesor, te avisará para que vayas subiendo tu solución. Las soluciones enviadas más tarde de los 30 minutos no serán evaluadas.


Aplicando la **estrategia de divide y vencerás**, implementa una función **recursiva** que reciba una lista ordenada de enteros y sin repeticiones, **A**, y un número entero, **x**,  y devuelva su posición en la lista. Si el número no existe devuelve -1. 

Reglas:
- Recuerda que tu función debe ser recursiva y seguir el enfoque de divide y vencerás. Enfoques no recursivos y no basados en este enfoque no serán evaluados.
- Tu función no puede usar bucles ni listas auxiliares (de ningún tipo). 
- Tampoco puedes usar la funcion index de las listas de Python. 
- data no puede ser modificado (es decir, no puedes añadir o eliminar elementos de data)
"""

def indexRec(A,x):
  """returns the list of indices for x in data"""
  if A==None or len(A)==0:
    return -1

  return _indexRec(A,x,0,len(A)-1)

def _indexRec(A,x,left,right):
    if left<=right:
        mid =   (left + right) // 2
    

        if A[mid]==x:
            return mid

        if x<A[mid]:
            return _indexRec(A,x,left,mid-1)
        
        return _indexRec(A,x,mid+1,right)

    return -1

import unittest


class Test(unittest.TestCase):

    #variable estática para almacenar la nota
    nota=0
    
    def setUp(self):
        self.x=5
        self.y=34
        self.w=-4

        self.z=10
        self.t=15

        self.input=[-2, 0, 4, 5, 10, 13, 15, 25, 33]

    def test1_indexRec(self):
        print('Caso 1: data es [] (nota: 2)')
        print('input:',[],'value:',self.x)
        self.assertEqual(indexRec([],self.x), -1, 'FAIL: debería ser -1')
        print('\t\t nota += 2.5')
        Test.nota+=2.5


    def test2_indexRec(self):
      print('Caso 2: x no existe es [] (nota: 2)')
      print('input:',self.input,'value:',self.y)
      self.assertEqual(indexRec([],self.y), -1, 'FAIL: debería ser -1')
      print('\t\t nota += 2.5')
      Test.nota+=2.5

    def test3_indexRec(self):
      print('Caso 3: x no existe es [] (nota: 2)')
      print('input:',self.input,'value:',self.w)
      self.assertEqual(indexRec([],self.w), -1, 'FAIL: debería ser -1')
      print('\t\t nota += 5')
      Test.nota+=5

    def test4_indexRec(self):
      print('...Caso 4: x sí existe en data (nota: 2)')
      print('input:',self.input,'value:',self.z)
      self.assertEqual(indexRec(self.input,self.z), 4, 'FAIL: debería ser 4')
      print('\t\t nota += 5')
      Test.nota+=5

    def test5_indexRec(self):
      print('...Caso 4: x sí existe en data (nota: 2)')
      print('input:',self.input,'value:',self.t)
      self.assertEqual(indexRec(self.input,self.t), 6, 'FAIL: debería ser 6')
      print('\t\t nota += 5')
      Test.nota+=5

   
    def test_printNota(self):
      print('\n\n*************************')
      print("\nNota Final:",Test.nota)  
      print('*************************')


#Comentar para usarlo en spyder
unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Descomenar para usarlo en Spyder
#if __name__ == '__main__':
#    unittest.main()