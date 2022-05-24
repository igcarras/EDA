def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if x not in a or x == None:
        return (-1, -1)

    return _find_first_last(0, len(a)-1, a, x, tuple(), int(), int())


def _find_first_last(left, right, a, x, tupla, first, last):
    if left <= right:
        mid = (left + right)//2
        _find_first_last(left, mid-1, a,x, tupla, first, last)
        if a[mid] == x:
            first, last = a[mid], a[mid]

        _find_first_last(mid+1, right, a, x, tupla, first, last)
    return (first, last)






if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
