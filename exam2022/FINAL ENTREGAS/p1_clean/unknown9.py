def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if len (a) == 0 or a == None:    #si la lista esta vacia o directamente no existe lista se devuelve lo predeterminado
        return (-1, -1)
    return _find_first_last(a, x, 0, len(a)-1)     #acudimos a la funcion auxiliar
def _find_first_last(a:list, x:int, start:int, end:int)->tuple:  #creamos una funcion auxiliar con un inicio y un final
    if start == end:                     #compartamos el inicio con el final porque si son los mismo y ademas coinciden con x pued devolvemos su posicionm
        if a[start] == x and a[end] == x:
            return (start, end)
        else:
            return (-1, -1)
    if start<=end:     #aplicamos el divide y venceras en la lista para dividirla en unidades mas pequeñas
        m = (start+end) // 2
        posi1 = _find_first_last(a, x, start, m)
        posi2 = _find_first_last(a, x, m+1, end)
        return max(posi1, posi2)
    return (-1, -1)
