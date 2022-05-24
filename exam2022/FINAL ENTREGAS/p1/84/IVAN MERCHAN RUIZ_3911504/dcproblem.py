"""
Nombre: Iván Merchán Ruiz
NIA: 100451135
"""

def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if len(a) == 0 or x not in a:
        resultado = (-1,-1)
        return resultado
    return _find_first_last(a, x, 0, len(a) - 1, [-1,-1])

def _find_first_last(a, x, left, right, indices):
    if left <= right:
        mid = (left + right) // 2
        _find_first_last(a, x, left, mid - 1, indices)
        if a[mid] == x and indices[0] == -1:
            indices[0] = mid
        if a[mid] == x:
            indices[1] = mid
        _find_first_last(a, x, mid + 1, right, indices)
    if indices[1] == -1:
        indices[1] = indices[0]
    resultado = (indices[0],indices[1])
    return resultado


if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
