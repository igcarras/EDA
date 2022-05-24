#Luis González Pérez, Grupo 801, NIA 100475299




def find_first_last(a: list, x: int):
    """returns the first and last indices of x in the list"""
    return (find(a, x, 0, True), find(a, x, 0, False))


def find(a: list, x: int, indice : int, principio : bool):
    #Si la lista es de un elemento, se comprueba y se devuelve el indice si es x
    if len(a) == 1:
        if a[0] == x:
            return indice
    #Se divide la lista en mitades
    elif len(a) > 0:
        mitad = len(a) // 2
        #En función de principio, se busca la primera o última instancia
        if principio:
            i = find(a[:mitad], x, indice, principio)
            if i != -1:
                return i
            f = find(a[mitad:], x, indice+mitad, principio)
            return f
        else:
            f = find(a[mitad:], x, indice+mitad, principio)
            if f != -1:
                return f
            i = find(a[:mitad], x, indice, principio)
            return i
    #Si no se encuentra
    return -1

if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 6   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
