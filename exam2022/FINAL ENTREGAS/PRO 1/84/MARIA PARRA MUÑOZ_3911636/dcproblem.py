def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    left = 0
    right = len(a) - 1

    if len(a) == 0:
        return -1, -1

    else:
        return _find_first_last(a, left, right, x)


def _find_first_last(a: list, left: int, right: int, x: int) -> (int, int):
    first = None
    last = None

    m = (left + right) // 2

    i = left
    j = right

    if len(a) > 3:
        while a[i] != x and i < m:
            i += 1

        if a[i] == x:
            first = i

        while a[j] != x and j > m:
            j -= 1

        if a[j] == x:
            last = j

        if first == None:
            if a[m] != x:
                i += 1
                first = _find_first_last(a[i:], i, right, x)[0]

            else:
                i += 1
                first = m

        if last == None:
            if a[m] != x:
                j -= 1
                last = _find_first_last(a[:j+1], 0, j, x)[1]
            else:
                j -= 1
                last = m

        return first, last


    if first == None:
        if last == None:
            return -1, -1
        else:
            return last, last
    if last == None:
        if first == None:
            return -1, -1
        else:
            return first, first



if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
