# Daniel Sánchez de la Cruz. NIA: 100475344
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    ocurrencia = (-1, -1)
    if len(a) == 0:
        return ocurrencia
    first = _find_first(a, x, start=0, end=len(a))
    last = _find_last(a, x, start=0, end=len(a))
    if last == -1:
        last = first
    if first == -1:
        first = last
    return (first, last)
def _find_first(a, x, start, end):
    if len(a) == 0:
        return -1
    if len(a) == 1:
        if a[0] == x:
            return start
        else:
            return -1
    m = len(a) // 2
    first = _find_first(a[0:m], x, start=start, end=m)
    if first != -1:
        return first
    first = _find_first(a[m:], x, start=m, end=end)
    return first
def _find_last(a, x, start, end):
    if len(a) == 0:
        return -1
    if len(a) == 1:
        if a[0] == x:
            return start
        else:
            return -1
    m = len(a) // 2
    last = _find_last(a[m:], x, start=m, end=end)
    if last != -1:
        return last
    last = _find_last(a[0:m], x, start=start, end=m)
    return last
