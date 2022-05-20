def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    # Si la lista está vacía devolvemos (-1, -1)
    if len(a) == 0 or x not in a:
        return (-1, -1)

    else:
        _find_first_last(a, x, 0, len(a)-1)

def _find_first_last(a, x, start, end):
    aux1 = len(a)
    aux2 = 0
    mid = len(a)//2
    i = start
    j = end
    pivot = mid

    while i <= j:
        while i < pivot:
            i += 1
        while j > pivot:
            j -= 1
        if i <= j:
            if i == x or j == x:
                if aux1 != len(a):
                    aux2 = i
                else:
                    aux1 = i
            i += 1
            j -= 1

    while j > start:
        _find_first_last(a, x, start, j)
    while i < end:
        _find_first_last(a, x, i, end)

    return (aux1, aux2)


if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
