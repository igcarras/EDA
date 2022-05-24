from turtle import left, right
def find_first_last(a: list, x: int):
    """returns the first and last indices of x in the list"""
    if a == None or len(a) == 0:
        return (-1, -1)
    return _find_first_last(a,x,0,len(a) - 1)
def _find_first_last(a, x, left, right):
    min = -1
    max = -1
    if left >= right:
        m = len(a)//2
        _find_first_last(a, x, left, m -1)
        if a[m] == x:
            if min == -1:
                min = m
            if m > max:
                max = m
        _find_first_last(a, x, m + 1, right)
    return (min, max)
