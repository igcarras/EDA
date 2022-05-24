"""XIUTIAN WANG"""
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if a is None or len(a) == 0:
        return -1, -1
    return _find_first_last(a,x, 0, len(a)-1)
def _find_first_last(a, x, start, end):
    if start > end:
        return -1, -1
    m = (start + end) // 2
    if start == end:
        if a[start] == x:
            return start, start
        else:
            return -1, -1
    pos1 = _find_first_last(a, x, start, m-1)
    if x == a[m]:
        return m,m
    pos2 = _find_first_last(a, x, m+1, end)
    if pos1 is None and pos2 is None:
        return -1,-1
    elif pos2:
        return pos2
    elif pos1:
        return pos1
    else:
        return pos1, pos2
