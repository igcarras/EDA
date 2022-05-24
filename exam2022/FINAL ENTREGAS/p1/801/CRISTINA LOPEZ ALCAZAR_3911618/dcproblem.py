#Cristina López Alcázar
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if len(a) == 0 or not a or not x in a:
        return -1, -1
    return _find_first_last(a, x, 0, len(a)-1)


def _find_first_last(a: list, x: int, start: int, end: int) -> (int, int):
    m = (start + end) // 2
    if start == end:
        if a[m] == x:
            return m, m
        else:
            return None, None
    else:
        min1, max1 = _find_first_last(a, x, start, m)
        min2, max2 = _find_first_last(a, x, m+1, end)

    if min1 and min2:
        mini = min(min1, min2)
    elif min1 and not min2:
        mini = min1
    elif min2 and not min1:
        mini = min2
    else:
        mini = None

    if max1 and max2:
        maxi = max(max1, max2)
    elif max1 and not max2:
        maxi = min1
    elif max2 and not max1:
        maxi = max2
    else:
        maxi = None

    if not mini and not maxi:
        return 0, 0
    else:
        return mini, maxi






if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
