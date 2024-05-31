def count_ideal_couples(a: list, b: list) -> int:
    """recibe dos listas de personas del mismo tamaño
    y devuelve una lista con las parejas ideales, y el número total de parejas ideales"""
    if len(a) != len(b):
        print("a y b deben tener el mismo tamaño")
        return -1

    if len(a) == 0:
        return 0

    num_couples = 0

    m = len(a) // 2
    if (a[m] % 2 == 0 and b[m] % 2 != 0) or (a[m] % 2 != 0 and b[m] % 2 == 0):
        num_couples += 1

    num_par1 = count_ideal_couples(a[0:m], b[0:m])
    num_par2 = count_ideal_couples(a[m + 1:], b[m + 1:])

    return num_couples + num_par1 + num_par2

import random as rand

if __name__ == '__main__':
    n = 5
    input_a=[]
    input_b=[]
    for i in range(n):
        input_a.append(rand.randint(0,100))
        input_b.append(rand.randint(0,100))

    print("lista a:" , input_a)
    print("lista b:", input_b)

    print(count_ideal_couples(input_a, input_b))



