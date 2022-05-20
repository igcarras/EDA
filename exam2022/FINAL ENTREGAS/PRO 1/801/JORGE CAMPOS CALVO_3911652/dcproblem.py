def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    result = (first_occurrence(a, x), last_occurrence(a, x))
    return result


def first_occurrence(a: list, x: int) -> int:
    if a is None or len(a) == 0:
        return -1
    return _first_occurrence(a, x, 0)


def _first_occurrence(a: list, x: int, i) -> int:
    encontrado = False
    while i != len(a) and encontrado == False:
        if a[i] == x:
            encontrado = True
            return i
        i += 1
    return -1


def last_occurrence(a: list, x: int) -> int:
    if a is None or len(a) == 0:
        return -1
    return _first_occurrence(a, x, -1)


def _last_occurrence(a: list, x: int, i) -> int:
    encontrado = False
    while i != -len(a) and encontrado == False:
        if a[i] == x:
            encontrado = True
            return len(a)-i
        i -= 1
    return -1



if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
