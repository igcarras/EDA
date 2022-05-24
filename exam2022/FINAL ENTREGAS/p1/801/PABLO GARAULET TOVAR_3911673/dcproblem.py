def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
#Implementa una función, find_first_last, que reciba una
#lista de enteros, a, y un número entero, x. La función debe devolver una tupla (first,
#last), donde first es el índice de la primera ocurrencia de x en a, y last es el índice de
#la última ocurrencia de x en a. Si la lista está vacía o x no existe en a, la función
#devolverá la tupla (-1, -1).


def _find_first_last(a, x, posicion, tupla):
    #casos base
    if len(a) == 0:
        return None
    elif len(a) == 1:
        posicion = posicion + 1
        if a[0] == x:
            return posicion, posicion
        else:
            return None, posicion

    #divide
    mitad = len(a) // 2
    posicion1, posicion = _find_first_last(a[0:mitad], x, posicion, tupla)
    posicion2, posicion = _find_first_last(a[mitad:len(a)], x, posicion, tupla)


    if posicion1 is not None:
        if tupla[0] is not None:
            tupla[1] = posicion1
        elif tupla[0] is None and tupla[0] is not 0:
            tupla[0] = posicion1
    if posicion2 is not None:
        if tupla[0] is not None:
            tupla[1] = posicion2
        elif tupla[0] is None and tupla[0] is not 0:
            tupla[0] = posicion2
    return None, posicion

def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    posicion = -1
    tupla = [None, None]
    _find_first_last(a, x, posicion, tupla)
    return (tupla[0], tupla[1])




if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
