def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if len(a) == 0 or a is None:
        return (-1,-1)

    return _find_first_last(a, x, 0, len(a) - 1)


def _find_first_last(a, x, i, j):
    m = (i + j) // 2
    if i == j:
        if a[i]==x:
            return i,i
        else:
            return (-1,-1)
    if i < j:
        num1 = _find_first_last(a, x, i, m)
        if x == a[m]:
            return m,m
        num2 = _find_first_last(a, x, m+1, j)
        if num1 is None and num2 is None:
            return (-1, -1)
        elif num2:
            return num2
        elif num1:
            return num1
        else:
            return num1, num2









if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
