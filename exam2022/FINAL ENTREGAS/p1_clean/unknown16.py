"Pablo Albendea Obispo"
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if not a or len(a)== 0:
        return (-1, -1)
    elif x not in a:
        return (-1,-1)
    else:
        return _find_first_last(a, x, -1, -1, 0)
def _find_first_last(a, x, primer, ultimo, indice):
    if not a or len(a) == 0:
        return (primer, ultimo)
    else:
        mid = len(a)//2
    if len(a)==1:
        if a[mid]== x:
            if primer == -1:
                primer = indice
            if ultimo < indice:
                ultimo = indice
        indice += 1
    elif len(a) > 1:
        mid = len(a)//2
        izquierda = a[0:mid]
        derecha = a[mid:]
        return _find_first_last(izquierda,x,primer,ultimo,indice) and _find_first_last(derecha,x,primer,ultimo,indice)
    return (primer, ultimo)
