def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if a == None or len(a) == 0:
        return (-1, -1)
    first = _find_first(a, x, 0, len(a) - 1)
    last = _find_last(a, x, 0, len(a) - 1)
    return (first, last)
def _find_first(a, x, first, last):
    if first == last:
        if a[first] == x:
            return first
        else:
            return -1
    if first <= last:
        medio = (first + last) // 2
        index = _find_first(a, x, first, medio)
        if index == -1:
            index = _find_first(a, x, medio + 1, last)
        return index
    return -1
def _find_last(a, x, first, last):
    if first == last:
        if a[first] == x:
            return first
        else:
            return -1
    if first <= last:
        m = (first + last) // 2
        indice1 = _find_last(a, x, first, m)
        indice2 = _find_last(a, x, m + 1, last)
        return max(indice1, indice2)
    return -1
