"""100451322 - Yago Brotón Gutiérrez"""
import sys


def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    primera_pos = _find_first(a, x)
    ultima_pos = _find_last(a, x)
    if primera_pos == sys.maxsize:
        primera_pos = -1
    if ultima_pos < -1:
        # No hacemos ultima_pos == -sys.maxsize, por que cuando el elemento no está en la lista
        # la función find_last devuelve -sys.maxsize + len(a) // 2, que es distinto a -sys.maxsize
        ultima_pos = -1
    result = (primera_pos, ultima_pos)
    return result


def _find_first(a: list, x: int):
    """Devuelve el índice de la primera aparición del elemento"""
    if len(a) == 0:
        return sys.maxsize
    if len(a) == 1:
        if a[0] == x:
            return 0
        return sys.maxsize

    mid = len(a) // 2
    return min(_find_first(a[:mid], x), mid + _find_first(a[mid:], x))


def _find_last(a: list, x: int):
    """Devuelve el índice de la última aparición del elemento"""
    if len(a) == 0:
        return -sys.maxsize
    if len(a) == 1:
        if a[0] == x:
            return 0
        return -sys.maxsize

    mid = len(a) // 2
    return max(_find_last(a[:mid], x), mid + _find_last(a[mid:], x))


if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for VALUE in sorted(set(b)):
        first, last = find_first_last(b, VALUE)
        print("x: ", VALUE, ", first index:", first, ", last index: ", last)

    VALUE = 4   # does not exist
    first, last = find_first_last(b, VALUE)
    print("x: ", VALUE, ", first index:", first, ", last index: ", last)
