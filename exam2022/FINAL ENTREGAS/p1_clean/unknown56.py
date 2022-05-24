# Irene Subías Serrano
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    resultado = (-1, -1)
    if not a:
        return resultado
    lista = a
    resultado = _find_first_last(a, x, 0, len(a)-1, resultado, lista)
    return resultado
def _find_first_last(a: list, x: int, i, j, resultado, lista):
    if len(a) > 1:
        resultado = _find_first_last(a[0: len(a)//2], x, i, j//2, resultado, lista)
        resultado = _find_first_last(a[len(a) // 2 + 1:], x, i // 2, j, resultado, lista)
    if lista[i] == x and i > resultado(0):
        resultado = (i, resultado(1))
    elif lista[j] == x and j > resultado(1):
        resultado = (resultado(0), j)
    return resultado
