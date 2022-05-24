# David Serrano Sangrador
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if a == None or len(a) == 0:
        return (-1, -1)
    # metemos una lista con unos valores máximos y mínimos básicos que a medida que vayamos viendo elementos
    # iremos cambiandolos por el que más se adecue
    lista = _find_first_last(a, x, 0, len(a)-1, [9999,-9999])
    # si la lista que sacamos es la misma que introducimos, es que no existe el elemento en la lista
    if lista == [9999,-9999]:
        return (-1, -1)
    # volvemos a comprobar el mínimo (si no se hace esto, el test 6 no lo pasa)
    min = lista[0]
    for elem in lista:
        if elem <= min:
            min = elem
    max = lista[0]
    for elem in lista:
        if elem >= max:
            max = elem
    return (min, max)
    # ahora cogemos el elemento más pequeño de la lista
'''
# este método para todos los unitest, pero tiene el append
def _find_first_last(a, x, left, right, lista):
    # nos damos cuenta de que el índice es m
    if left <= right:
        m = (left+right) // 2
        _find_first_last(a, x, left, m - 1, lista)
        _find_first_last(a, x, m + 1, right, lista)
        if a[m] == x:
            lista.append(m)
    return lista
'''
def _find_first_last(a, x, left, right, lista):
    # nos damos cuenta de que el índice es m
    # si está dentro del rango
    if left <= right:
        m = (left+right) // 2
        # dividimos
        _find_first_last(a, x, left, m - 1, lista)
        _find_first_last(a, x, m + 1, right, lista)
        # vencemos, vamos contando las posiciones de la lista
        # si encontramos una posicion menor, la sustituimos por la menor e igual con el maximo
        if a[m] == x:
            if a[m] <= lista[0]:
                lista[0] = m
            if a[m] >= lista[1]:
                lista[1] = m
    return lista
