def quicksort(a: list) -> list:
    if a is None or len(a) <= 1:
        return a
    print("Primera llamada")
    _quicksort(a, 0, len(a)-1)
def _quicksort(a,start,end):
    p=a[start]
    print("el pivote es", p)
    i,j=start+1,end
    while i<=j:
        while i <= end and a[i] <= p:
            i += 1
        while j >= start+1 and a[j] >= p:
            j -= 1
        if i <= j:
            a[i],a[j]=a[j],a[i]
        if start<j:
            a[i],a[j]=a[j],a[i]
    a[start],a[j]=a[j],a[start]

    if j-1 > start:
        _quicksort(a, start, j-1)
    if j+1 < end:
        _quicksort(a, j+1, end)

#main
import copy,random

a = []
n = random.randint(1, 10)
for _ in range(n):
    x = random.randint(-5,10)
    a.append(x)

# crea una copia de a
aux = copy.deepcopy(a)

print("before: ", a, end = " ")
# ordena la copia aux
quicksort(aux)
print(", after: ", aux)

# ambas listas deben ser iguales después de ordenar
assert a == sorted(aux)