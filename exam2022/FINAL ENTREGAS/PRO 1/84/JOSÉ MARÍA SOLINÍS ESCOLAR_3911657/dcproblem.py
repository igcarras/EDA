#Nombre y apellidos: José María Solinís Escolar


def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    first_index = -1
    last_index = -1
    if a is None or len(a) == 0:
        return -1, -1
    return _find_first_last(a, x, 0, len(a) - 1, first_index, last_index)


def _find_first_last(a: list, x: int, start: int, end: int, first_index, last_index):
    if a[start] == x:
        if first_index > -1:
            last_index = start
        else:
            first_index = start
    if start < end:
        m = (start + end) // 2
        _find_first_last(a, x, start, m, first_index, last_index)
        _find_first_last(a, x, m+1, end, first_index, last_index)
    return first_index, last_index


if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
