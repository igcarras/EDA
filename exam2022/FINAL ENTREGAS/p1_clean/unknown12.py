def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if x not in a:
        return -1,-1
    else:
        currentIndex = -1
        result = [None, None]
        _find_first_last(a, x, currentIndex, result)
        return (result[0], result[1])
def _find_first_last(a: list, x: int, currentIndex, result):
    if len(a) == 0 or a == None:
        return -1,-1
    if len(a) == 1:
        currentIndex = currentIndex + 1
        if (a[0] == x):
            return currentIndex, currentIndex
        return None, currentIndex
    mid = len(a) // 2
    result1, currentIndex = _find_first_last(a[0:mid], x, currentIndex, result)
    result2, currentIndex = _find_first_last(a[mid:len(a)], x, currentIndex, result)
    if result1 != None:
        if result[0] != None:
            result[1] = result1
        elif result[0] == None and result[0] != 0:
            result[0] = result1
    if result2 != None:
        if result[0] != None:
            result[1] = result2
        elif result[0] == None and result[0] != 0:
            result[0] = result2
    return None, currentIndex
