def find_first_last(a: list, x: int):
    """returns the first and last indices of x in the list"""
    if a is None or len(a) == 0:
        return (-1, -1)

    return _find_first_last(a, x, 0, len(a) - 1)

def _find_first_last(a: list, x: int, start: int, end: int):
    result = ()
    if start <= end:
        mid = (start + end)//2
        _find_first_last(a, x, start, mid - 1)

        if len(a) == 0:
            if a[start] == x:
                result = result + (start,)
        
        if len(a) == 1:
            if a[mid] == x:
                result = result + (mid,)

        _find_first_last(a, x, mid + 1, end)

        if result == ():
            result = result + (-1, -1,)
        

    return result




if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
