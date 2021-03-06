# -*- coding: utf-8 -*-
"""quicksort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N0qsiGgkVUlFLhmYy3dkNxR2RVDcvow8

<a href="https://colab.research.google.com/github/isegura/EDA/blob/master/quicksort.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Divide y Vencerás. Quicksort
En este notebook, codificaremos distintas implementaciones del algoritmo quicksort.

El algoritmo quicksort recibe una lista y ordena dicha lista de menor a mayor. 

Quicksort se basa en la elección de un elemento pivote, y la creación de dos particiones, los elementos que son menores que el pivote, y los elementos mayores al pivote. Después de crear las dos particiones, el pivote estará colocado en la posición que le corresponde en la lista ordenada.

## Quicksort (listas auxiliares y primer elemento como pivote)
"""

def partitions(a: list) -> (list, int, list):
    """ recibe una lista y selecciona un elemento como pivote el primer elemento 
    de la lista. La función devuelve los siguientes datos:
    - una lista con los elementos menores que el pivote
    - el pivote (primer elemento)
    - una lista formada con los elementos de la lista mayores que el pivote"""
    
    # seleccionamos el pivote
    p = a[0]
    smaller = []
    bigger = []
    for i in range(1, len(a)):
        if a[i] <= p:
            smaller.append(a[i])
        else:
            bigger.append(a[i])
    
    return (smaller, p, bigger)

def quicksort(a: list) -> list:
    if a is None or len(a) <= 1:
        return a

    list_smaller, pivote, list_bigger = partitions(a)
    return quicksort(list_smaller) + [pivote] + quicksort(list_bigger)

"""El siguiente código te ayudará a probar la función. Puedes ejecutarlo varias veces para probar con tamaños distintos y valores distintos en la lista de entrada:"""

import random
import copy
a = []
n = random.randint(1, 10)
for _ in range(n):
    x = random.randint(-5,10)
    a.append(x)
# creamos una copia por valor de a (no se almacena en la misma dirección)

print("before: ", a, end = ' ')

print(", after sorting: ", quicksort(a))
# it should be True. If it is False, this means that there is a bug in our code
assert quicksort(a) == sorted(a)

"""## Quicksoft (listas auxiliares y último elemento como pivote)

Implementa el algoritmo quicksort basado en la elección el **último elemento** de la lista como pivote. 

La siguiente implementación es muy parecida a la anterior, simplemente el pivote ahora es el último elemento de la lista. 
"""

def partitions(a: list) -> (list, int, list):
    """ recibe una lista y selecciona un elemento como pivote
    (en este caso, se elige el último elemento como pivote. La función devuelve los 
    siguientes datos:
    - una lista con los elementos menores que el pivote
    - el pivote (último elemento)
    - una lista formada con los elementos de la lista mayores que el pivote"""
    
    # seleccionamos el pivote
    p = a[-1]
    smaller = []
    bigger = []
    for i in range(len(a)-1):
        if a[i] <= p:
            smaller.append(a[i])
        else:
            bigger.append(a[i])
    
    return (smaller, p, bigger)

def quicksort(a: list) -> list:
    if a is None or len(a) <= 1:
        return a

    list_smaller, pivote, list_bigger = partitions(a)
    return quicksort(list_smaller) + [pivote] + quicksort(list_bigger)

"""El siguiente código crea un array de forma aleatoria. Ejecutálo varias veces para probarlo con distintas listas de distinto tamaño:"""

a = []
n = random.randint(1, 10)
for _ in range(n):
    x = random.randint(-5,10)
    a.append(x)

print("before: ", a, end = ' ')

print(", after sorting: ", quicksort(a))
# it should be True. If it is False, this means that there is a bug in our code
assert quicksort(a) == sorted(a)

"""## Quicksoft (listas auxiliares y pivote aleatorio)
Sería posible implementar otras versiones donde el pivote se eliga al azar, y una vez elegido se mueva a la primera o última posición, para proceder como en las versiones anteriores:

"""

import random

def partitions(a: list) -> (list, int, list):
    """ recibe una lista y selecciona de forma aleatoria el pivote.
    La función devuelve los siguientes datos:
    - una lista con los elementos menores que el pivote
    - el pivote (último elemento)
    - una lista formada con los elementos de la lista mayores que el pivote"""
    
    # seleccionamos el pivote
    index_p = random.randint(0,len(a)-1)
    p = a[index_p]
    # intercambiamos el pivote con el último elemento
    a[index_p], a[-1] = a[-1], a[index_p]
    # ahora el pivote es el último elemento
    smaller = []
    bigger = []
    for i in range(len(a)-1):
        if a[i] <= p:
            smaller.append(a[i])
        else:
            bigger.append(a[i])
    
    return (smaller, p, bigger)

def quicksort(a: list) -> list:
    if a is None or len(a) <= 1:
        return a

    list_smaller, pivote, list_bigger = partitions(a)
    return quicksort(list_smaller) + [pivote] + quicksort(list_bigger)

"""Probamos esta implementación basada en listas auxiliares y pivote aleatorio:"""

a = []
n = random.randint(1, 10)
for _ in range(n):
    x = random.randint(-5,10)
    a.append(x)

print("before: ", a, end = ' ')

print(", after sorting: ", quicksort(a))
# it should be True. If it is False, this means that there is a bug in our code
assert quicksort(a) == sorted(a)

"""## Quicksort con menor complejidad espacial (sin usar listas auxiliares)

Las dos implementaciones anteriores utilizan listas auxiliares para almacenar las particiones (los elementos menores y mayores del pivote). Es posible proponer implementaciones con una menor complejidad espacial (es decir, sin la necesidad de usar listas auxiliares para almacenar las particiones). En su lugar, usaremos índices que indique el inicio y final de la partición a ordenar. 

A continuación, veremos una implementación (sin listas auxiliares) que selecciona el último elemento como pivote:

### Quicksort (último elemento pivote)
"""

def quicksort(a: list) -> None:
    """la función ordena los elementos de la lista a de menor a mayor.
    No devuelve una nueva lista, simplemente ordena a."""
    if a is None or len(a)<=1:
        # a is already sorted!!!        
        return

    _quicksort(a, 0, len(a)-1)

def _quicksort(a: list, start: int, end: int) -> None:
    """La función ordena la sublista de a comprendida entre los indices start y end, ambos inclusives"""
   
    # primer paso, elegir el último elemento como pivote
    piv = a[end]
    # creamos dos índices
    # el índice i va a recorrer la lista (partición) desde start, y su objetivo
    # es avanzar mientras que los elementos sean menores que el pivote
    # el índice j va a recorrer la partición desde end hacia la izquierda, y su 
    # objetivo es avanzar (hacia start) mientras que los elementos sean mayores que 
    # el pivote
    i, j = start, end - 1

    while i <= j:
        # paramos de avanzar i, cuando encontramos un elemento a[i]>=p 
        while a[i] < piv:
            i += 1
        # paramos de disminuir j, cuando encontramos un elemento a[j]<=p 
        while a[j] > piv:
            j -= 1

        if i < j:
            # intercambiamos a[i], a[j]
            a[i], a[j] = a[j], a[i]
        if i <= j:    
            # avanzamos índices
            i += 1
            j -= 1

    # Cuando termina el bucle, los elementos más pequeños al pivote estarán situados
    # en la izquierda de la partición, mientras los elementos mayores al pivote
    # estarán situados a la derecha. Debemos colocar el pivote, en la posición i, que es la 
    # posición que separá ambas partes. El elemento en i será mayor que el pivote, y por tanto
    # podemos moverlo a la parte derecha de la partición
    a[end], a[i] = a[i], a[end]

    # Aplicamos recursión sobre cada partición (si al menos tienen un elemento)
    if i-1 > start: 
        _quicksort(a, start, i-1)
    if i+1 < end:
        _quicksort(a, i+1, end)

"""Ejecuta el siguiente código varias veces para comprobar que el algoritmo funciona correctamente para distintos tamaños y valores en la lista:"""

import copy
# a = [0, -7, -10, -7]
# a = [-3, 4, -5, -2, -2]

a = []
n = random.randint(1, 10)
for _ in range(n):
    x = random.randint(-5,10)
    a.append(x)

# aux es una copia de a, pero no tienen la misma dirección de memoria
aux = copy.deepcopy(a)

print("before: ", a, end = " ")
quicksort(a)
print(", after: ", a)

# Siempre deben ser iguales. Si no son iguales, significa que nuestra
# implementación tiene algún error
assert a == sorted(aux)

"""### Quicksort (elemento central pivote)"""

def quicksort(a: list) -> None:
    """la función ordena los elementos de la lista a de menor a mayor.
    No devuelve una nueva lista, simplemente ordena a."""
    if a is None or len(a)<=1:
        # a is already sorted!!!        
        return

    _quicksort(a, 0, len(a)-1)

def _quicksort(a: list, start: int, end: int) -> None:
    """La función ordena la sublista de a comprendida entre los indices start y end, ambos inclusives"""
    # primer paso, elegir el elemento central como pivote
    m = (start + end) // 2
    piv = a[m]
    # creamos dos índices
    i, j = start, end

    while i <= j:
        while a[i] < piv:
            i += 1
        while a[j] > piv:
            j -= 1

        if i < j:
            # intercambiamos a[i], a[j]
            a[i], a[j] = a[j], a[i]
        if i <= j:
            # avanzamos índices
            i = i + 1
            j = j - 1
    
    # Aplicamos recursión sobre cada partición
    if start < j:
        _quicksort(a, start, j)
    if end > i:
        _quicksort(a, i, end)

"""Vamos a probar esta nueva implementación (recuerda ejecutar varias veces)"""

# 
# a = [-3, 4, -5, -2, -2]
# a = [0, -7, -10, -7]

a = []
n = random.randint(1, 10)
for _ in range(n):
    x = random.randint(-5,10)
    a.append(x)

# aux es una copia de a, pero no tienen la misma dirección de memoria
aux = copy.deepcopy(a)
print("before: ", a, end = " ")
quicksort(a)
print(", after: ", a)
# Siempre debe ser True. En otro caso, tenemos algún fallo. 
assert a == sorted(aux)

"""## Quicksort (random pivote)
Esta implementación es muy similar a la anterior, pero la principal diferencia es que vamos a seleccionar el pivote de forma aleatoria
"""

import random

def quicksort(a: list) -> None:
    if a is None or len(a)==0:
        return
    _quicksort(a, 0, len(a)-1)

def _quicksort(a: list, start: int, end: int) -> None:
    """La función ordena la sublista de a comprendida entre los indices start y end, ambos inclusives"""
    # elegimos un índice de start and end, de forma aleatoria
    index_pivote = random.randint(start, end) # start and end, both included
    piv = a[index_pivote]
    # print('pivote seleccionado ', index_pivote, piv)

    # movemos el pivote a la posición end del array 
    a[index_pivote], a[end] = a[end], a[index_pivote]
    # ahora el pivote está al final de la partición

    i, j = start, end - 1

    while i <= j:
        while a[i] < piv:
            i += 1
        while a[j] > piv:
            j -= 1

        if i < j:
            # intercambiamos a[i], a[j]
            a[i], a[j] = a[j], a[i]
        if i <= j:
            # avanzamos índices
            i += 1
            j -= 1

    # finalmente, intercambiamos el pivote a la posición i,
    # que es la que separa los elementos menores a la izquierda
    # y los elementos mayores a la derecha
    a[end], a[i] = a[i], a[end]

    # Aplicamos recursión sobre las particiones (cuando no estén vacías)
    if start < i-1:
        _quicksort(a, start, i-1)
    if i+1 < end:
        _quicksort(a, i+1, end)

"""Ejecutamos varias veces para probar con distintos tamaños y valores:"""

a = []
n = random.randint(1,7)
for _ in range(n):
    a.append( random.randint(-10,10))

# aux es una copia de a, pero no tienen la misma dirección de memoria
aux = copy.deepcopy(a)

print("before: ", a, end = " ")
quicksort(a)
print(", after: ", a)

assert a == sorted(aux)

"""Esta última implementación muestra otra posible forma de codificar quicksort con pivote aleatorio:"""

def quicksortRand(A):
    _quicksortRand(A,0,len(A)-1)
    
def _quicksortRand(A, left, right):
    
    i,j=left,right
    p = A[random.randint(left,right)] # pivot is random element
    
    while i <= j:
        while A[i] < p: 
          i += 1
        while A[j] > p: 
          j -= 1
        if i < j: # swap 
            A[i], A[j] = A[j], A[i]
        if i <= j:
            i += 1
            j -= 1

    if left < j: # sort left list
        _quicksortRand(A, left, j)
    if i < right: # sort right list
        _quicksortRand(A, i, right)

a = []
n = random.randint(1,7)
for _ in range(n):
    a.append( random.randint(-10,10))

# aux es una copia de a, pero no tienen la misma dirección de memoria
aux = copy.deepcopy(a)

print("before: ", a, end = " ")
quicksortRand(a)
print(", after: ", a)

assert a == sorted(aux)

"""Y otra posible implementación más:"""

# Python implementation QuickSort using  
# Lomuto's partition Scheme. 
import random 
  
''' 
The function which implements QuickSort. 
arr :- array to be sorted. 
start :- starting index of the array. 
stop :- ending index of the array. 
'''
def quicksort(arr, start , stop): 
    if(start < stop): 
          
        # pivotindex is the index where  
        # the pivot lies in the array 
        pivotindex = partitionrand(arr, start, stop) 
          
        # At this stage the array is partially sorted  
        # around the pivot. Separately sorting the  
        # left half of the array and the right half of the array. 
        quicksort(arr , start , pivotindex - 1) 
        quicksort(arr, pivotindex + 1, stop) 
  
# This function generates random pivot, swaps the first 
# element with the pivot and calls the partition fucntion. 
def partitionrand(arr , start, stop): 
  
    # Generating a random number between the  
    # starting index of the array and the 
    # ending index of the array. 
    randpivot = random.randrange(start, stop) 
  
    # Swapping the starting element of the array and the pivot 
    arr[start], arr[randpivot] = arr[randpivot], arr[start] 
    return partition(arr, start, stop) 
  
''' 
This function takes the first element as pivot,  
places the pivot element at the correct position  
in the sorted array. All the elements are re-arranged  
according to the pivot, the elements smaller than the 
pivot is places on the left and the elements 
greater than the pivot is placed to the right of pivot. 
'''
def partition(arr,start,stop): 
    pivot = start # pivot 
    i = start + 1 # a variable to memorize where the  
                  # partition in the array starts from. 
    for j in range(start + 1, stop + 1): 
          
        # if the current element is smaller or equal to pivot, 
        # shift it to the left side of the partition. 
        if arr[j] <= arr[pivot]: 
            arr[i] , arr[j] = arr[j] , arr[i] 
            i = i + 1
    arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot] 
    pivot = i - 1
    return (pivot) 
  
# Driver Code 
if __name__ == "__main__": 
    array = [10, 7, 8, 9, 1, 5] 
    quicksort(array, 0, len(array) - 1) 
    print(array)

a = []
n = random.randint(1,7)
for _ in range(n):
    a.append( random.randint(-10,10))

# aux es una copia de a, pero no tienen la misma dirección de memoria
aux = copy.deepcopy(a)

print("before: ", a, end = " ")
quicksort(a, 0, len(a)-1)
print(", after: ", a)

assert a == sorted(aux)