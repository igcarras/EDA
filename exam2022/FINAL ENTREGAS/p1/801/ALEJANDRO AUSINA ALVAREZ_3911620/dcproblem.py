def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if a == None or len(a) == 0:
        return (-1, -1)
    lista = []
    resultado = tuple(_find_first_last(a, 0, len(a)-1, x))

    return resultado

def _find_first_last(a: list, start: int, end: int, x: int):
    m = (start+end) // 2
    if start ==  end:
        if a[start] == x:
            return (0, 0)
        else:
            return (-1, -1)

    mitad1 = _find_first_last(a, start, m, x)
    mitad2 = _find_first_last(a, m+1, end, x)

    pos1 = start
    pos2 = end
    while a[pos1] != x:
        pos1 += 1
    while a[pos2] != x:
        pos2 -= 1

    if pos1 == pos2:
        return (pos1, pos1)
    if pos2 == pos1:
        return (pos2, pos2)
    if pos2 == m and pos1 == m:
        if m != x:
            return (-1, -1)
        else:
            return (m, m)
    if pos1 == x and pos2 == x:
        return (pos1, pos2)
        pos1 += 1
        pos2 -= 1
        pos1 += 1















if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
