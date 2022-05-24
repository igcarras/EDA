def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if a == None or len(a)== 0:
        return (-1,-1)
    primero = _buscar_primero(a,x,0,len(a)-1)
    ultimo = _buscar_ultimo(a,x,0,len(a)-1)
    return (primero,ultimo)
def _buscar_primero(a,x,start,end):
   if start == end:
        if a[start] == x:
            return start
        else:
            return -1
   if start <= end:
        mid= (start + end) // 2
        i = _buscar_primero(a, x, start, mid)
        if i == -1:
            i = _buscar_primero(a, x, mid+ 1, end)
        return i
   return -1
def _buscar_ultimo(a,x,start,end):
    if start == end:
        if a[start] == x:
            return start
        else:
            return -1
    if start <= end:
        mid= (start + end) // 2
        i1 =  _buscar_ultimo(a, x, start,mid)
        i2 = _buscar_ultimo(a, x, mid+ 1, end)
        return max(i1, i2)
    return -1
