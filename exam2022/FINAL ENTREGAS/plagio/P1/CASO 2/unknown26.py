def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if len(a) == 0 or x not in a:
        return(-1, -1)
    if len(a) == 1 and a[0] == x:
        return(0, 0)
    primero = -1
    for i in range(len(a)):
        if a[i] == x:
            primero = i
            break
    if primero == -1:
        return(-1, -1)
    ultimo = i
    lista2 = a[i :]
    if len(lista2) == 1:
        return(i, i)
    for j in range(len(lista2)):
        if lista2[j] == x:
            ultimo = j + i
    return(primero, ultimo)
