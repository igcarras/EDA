





def find_first_last(a: list, x: int) -> (int, int):

    p = 0
    u = 0
    i = 0

    m = len(a)//2
    tupla = (p, u)

    if len(a) == 0 or a == None:
        tupla = (-1,-1)

    for y in a:
        if a[y] == x:
            i += 1
    if i == 0:
        tupla = (-1,-1)

    else:
        # tengo que separar la lista en dos
        parte1 = a[0:m]
        parte2 = a[m+1:]
        parte1 = _find_first_last(parte1,x)
        parte2 = _find_first_last(parte2,x)

        tupla = max(parte1,parte2)
    return tupla


def _find_first_last(a:list, x: int) -> (int,int):

    primer_indice = int
    segundo_indice = int
    m = len(a)//2

    if a[m] == x:
        primer_indice = m
        return primer_indice,primer_indice

    elif:
        _find_first_last(a[0:m])



"""def find_first_last(a,x):
    if len(a) == 0 or a == None:
        return -1,-1
    _find_first_last(a,x)

def _find_first_last(a,x):

    m = len(a)//2
    temp = a[m]
    pos1 = int
    pos2 = int
    if x == a[m]:
        pos1,pos2 = a[m]
    parte1 = _find_first_last(a[:m],x)
    parte2 = _find_first_last(a[m:,x])

    return pos1,pos2"""






if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)








