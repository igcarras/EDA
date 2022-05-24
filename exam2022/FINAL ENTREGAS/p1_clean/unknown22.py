def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if a == None or len(a) == 0:
        return (-1, -1)
    first = _find_first(a, x, 0, len(a) - 1)
    last = _last(a, x, 0, len(a) - 1)
    return (first, last)
def _find_first(a, x, start, end):
    if start == end:
        if a[start] == x:
            return start
        else:
            return -1
    if start <= end:
        m = (start + end) // 2
        index = _find_first(a, x, start, m)
        if index == -1:
            index = _find_first(a, x, m + 1, end)
        return index
    return -1
def _last(a, x, start, end):
    if start == end:
        if a[start] == x:
            return start
        else:
            return -1
    if start <= end:
        m = (start + end) // 2
        index1 = _last(a, x, start, m)
        index2 = _last(a, x, m + 1, end)
        return max(index1, index2)
    return -1
'''
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if a is None or len(a)== 0:
        return -1, -1
    if x not in a:
        return -1, -1
    return _find_first_last(a, x, 0, len(a)-1)
def _find_first_last(a: list, x: int, start: int, end: int) -> (int, int):
    if start == end:
        if a[start] == x:
            return start, start
        else:
            return -1, -1
    if start < end:
        m = (start + end) // 2
        index = _find_first_last(a, x, start, m)
        if index == (-1, -1):
            index = _find_first_last(a, x, m + 1, end)
        if index == (start, start):
            index = _find_first_last(a, x, m + 1, end)
        return index
    return -1, -1
'''
