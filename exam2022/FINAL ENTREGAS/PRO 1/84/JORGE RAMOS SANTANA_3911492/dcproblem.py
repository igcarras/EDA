
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    return _ffl(a,x)

    

    


def _ffl(a: list, x: int)->(int, int):
    test=1
    #print("A",a)
    mid=len(a)//2
    if len(a)<=1:
        if x==a[0]:
            #print(x)
            print("Found")
            return (x,test) #no entiendo como es que el metodo siempre devuelve NONE aun habiendo encontrado el elemento. Si lo imprimo, lo imprime correctamente, pero devuelve NONE
    else:
        _ffl(a[mid:],x)
        _ffl(a[:mid],x)


if __name__ == "__main__":

    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    


    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
    

    find_first_last(b, 5)

