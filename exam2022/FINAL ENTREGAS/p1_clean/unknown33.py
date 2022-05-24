def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if a is None or len(a) <= 1:
        return -1, -1
    if x not in a:
        return -1, -1
    return _find_first_last(a, x, 0, len(a)-1)
def _find_first_last(a, x, left, right):
    if left == right:
        if a[left] == x:
            return left
    if left < right:
        mid = (left + right) // 2
        parte1 = _find_first_last(a, x, left, mid)
        parte2 = _find_first_last(a, x, mid + 1, right)
        if parte1 != None and parte2 != None:
            return min(parte1, parte2), max(parte1, parte2)
        elif parte1 != None:
            return parte1
        elif parte2 != None:
            return parte2
