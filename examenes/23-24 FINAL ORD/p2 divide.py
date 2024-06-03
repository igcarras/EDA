def count_ideal_couples_slicing(a: list, b: list) -> int:
    """recibe dos listas de personas del mismo tamaño
    y devuelve una lista con las parejas ideales, y el número total de parejas ideales"""
    if len(a) != len(b):
        print("a y b deben tener el mismo tamaño")
        return 0

    if len(a) == 0:
        return 0

    num_couples = 0

    m = len(a) // 2
    if (a[m] % 2 == 0 and b[m] % 2 != 0) or (a[m] % 2 != 0 and b[m] % 2 == 0):
        num_couples += 1

    num_par1 = count_ideal_couples_slicing(a[0:m], b[0:m])
    num_par2 = count_ideal_couples_slicing(a[m + 1:], b[m + 1:])

    return num_couples + num_par1 + num_par2
def count_ideal_couples_slicing2(a: list, b: list) -> int:
    """recibe dos listas de personas del mismo tamaño
    y devuelve una lista con las parejas ideales, y el número total de parejas ideales"""
    if len(a) != len(b):
        print("a y b deben tener el mismo tamaño")
        return 0

    if len(a) == 0:
        return 0


    if len(a) == 1:

        #resA= a[0] % 2
        #resB= b[0] % 2

        #if resA != resB:
        if  (a[0]+ b[0])%2==1:
            return 1
        else:
            return 0

        """if (a[0] % 2 == 0 and b[0] % 2 != 0) or (a[0] % 2 != 0 and b[0] % 2 == 0):
            return 1
        else:
            return 0"""

    m = len(a) // 2

    num_par1 = count_ideal_couples_slicing2(a[0:m], b[0:m])
    num_par2 = count_ideal_couples_slicing2(a[m:], b[m:])

    return num_par1 + num_par2

def count_ideal_couples(a: list, b: list)-> int:
    if len(a) != len(b):
        print("a y b deben tener el mismo tamaño")
        return 0
    return _count_ideal_couples(a,b,0,len(a)-1)


def _count_ideal_couples(a: list, b: list, start:int, end:int) -> int:
    if start == end:
        if (a[start] % 2 == 0 and b[start] % 2 != 0) or (a[start] % 2 != 0 and b[end] % 2 == 0):
            return 1
        return 0

    m = (start+end)//2

    num_par1 = _count_ideal_couples(a,b, start,m)
    num_par2 = _count_ideal_couples(a,b, m+1,end)

    return  num_par1 + num_par2



import random as rand

if __name__ == '__main__':
    n = 15
    input_a=[]
    input_b=[]
    for i in range(n):
        input_a.append(rand.randint(0,100))
        input_b.append(rand.randint(0,100))

    print("lista a:" , input_a)
    print("lista b:", input_b)

    print(count_ideal_couples_slicing(input_a, input_b))
    print(count_ideal_couples_slicing2(input_a, input_b))
    print(count_ideal_couples(input_a, input_b))



