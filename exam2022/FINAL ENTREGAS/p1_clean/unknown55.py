#RUBEN ZORRILLA GARCIA
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if a is None or len(a) == 0:
        return (-1,-1)
    return _find_first_last(a, x, 0, len(a)-1)
def _find_first_last(a: list, x: int, start, end) -> (int, int):
    """returns the first and last indices of x in the list"""
    minim = 99999999
    maxim = -1
    if start == end:
        return (-1,-1)
    mid = (start + end) // 2
    if len(a) > 1:
        if x in a[0, mid+1]:
            return _find_first_last(a, x, 0, mid+1)
        elif x in a[mid + 1, len(a)]:
            return _find_first_last(a, x,mid+1,end)
    else:
        if x == a[mid]:
            if mid < minim:
                minim = mid
            if mid > maxim:
                maxim = mid
    return [minim, maxim]
