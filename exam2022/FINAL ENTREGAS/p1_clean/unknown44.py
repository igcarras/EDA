# Miguel Salas Heras
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if x not in a:
        return (-1,-1)
    first, last = _find_first_last(a,x,0, len(a)-1)
    return (first, last)
def _find_first_last(a,x,first,last):
    if first > last or (a[first] == x and a[last] == x):
        return first , last
    if a[first] != x:
        first += 1
    if a[last] != x:
        last -= 1
    return _find_first_last(a,x,first,last)
