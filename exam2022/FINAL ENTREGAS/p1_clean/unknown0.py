def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if a == None or len(a)== 0:
        return (-1,-1)
    primera = _find_first(a,x,0,len(a)-1)
    ultima = _find_last(a,x,0,len(a)-1)
    return (primera,ultima)
def _find_first(a,x,start,end):
   if start == end:
        if a[start] == x:
            return start
        else:
            return -1
   if start <= end:
        medio= (start + end) // 2
        indice = _find_first(a, x, start, medio)
        if indice == -1:
            indice = _find_first(a, x, medio+ 1, end)
        return indice
   return -1
def _find_last(a,x,start,end):
    if start == end:
        if a[start] == x:
            return start
        else:
            return -1
    if start <= end:
        medio= (start + end) // 2
        indice1 =  _find_last(a, x, start,medio)
        indice2 = _find_last(a, x, medio+ 1, end)
        if indice1 > indice2:
            return indice1
        else:
            return indice2
    return -1
