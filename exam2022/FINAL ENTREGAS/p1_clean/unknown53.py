#Marina Pérez Barbero
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    aux=  tuple(a)
    tupl = (-1,-1)
    if a == None or len(a) == 0:
        return tupl
    elif aux.index(x) == None:
        return _find_first_last(a,x,0,len(a)-1,tupl,aux)
    else:
        return (aux.index(x), aux.index(x))
def _find_first_last(a,x,right,left,tupl,aux) -> (int,int):
    if len(a) == 1:
        if a[0] == x:
            print("a")
            tupl = (aux.index(x),aux.index(x))
            return tupl
    while left <= right:
        m = (right + left)//2
        _find_first_last(a,x,left,m-1,tupl)
        _find_first_last(a, x, m + 1, right, tupl)
        if a[m] == x:
            if aux.index(x) == 1:
                tupl = (aux.index(x),aux.index(x))
                return tupl
    return tupl
