#Raúl Sanz Belmar
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if a == None or len(a) == 0:
        return (-1, -1)
    indexmin, indexmax = _find_first_last(a, x, 0, len(a)-1)
    return (indexmin, indexmax)
def _find_first_last(a:list, x:int, start:int, end:int)->int:
    if start == end:
        if x == a[start]:
            return start
        else:
            return -1
    elif start < end:
        indexmin = find_first(a, x, start, end)
        indexmax = find_last(a, x, start, end)
        return indexmin, indexmax
    return -1
def find_first(a:list, x:int, start:int, end:int)->int:
    if start == end:
        if x == a[start]:
            return start
        else:
            return -1
    elif start < end:
        mid = (start + end)//2
        indexmin = find_first(a, x, start, mid)
        if indexmin == -1:
            indexmin = find_first(a, x, mid+1, end)
        return indexmin
    return -1
def find_last(a:list, x:int, start:int, end:int)->int:
    if start == end:
        if x == a[start]:
            return start
        else:
            return -1
    elif start < end:
        mid = (start + end)//2
        indexmax1 = find_last(a, x, mid+1, end)
        indexmax2 = find_last(a, x, start, mid)
        return max(indexmax1, indexmax2)
    return -1
