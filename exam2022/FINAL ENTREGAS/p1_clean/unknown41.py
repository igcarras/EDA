# Alvarp SAntos
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    encontrado = False
    num = None
    left = 0
    right = len(a) - 1
    first = _find_first(a, x, left, right, encontrado, num)
    encontrado = False
    num2 = None
    left = 0
    right = len(a) - 1
    last = _find_last(a, x, left, right, encontrado, num2)
    if first == None:
        first = -1
    if last == None:
        last = -1
    return (first, last)
def _find_first(a: list, x: int, left: int, right: int, encontrado: bool, num):
    if len(a) == 0 or a == None:
        return
    mid = (left + right) // 2
    if a[mid] == x and encontrado == False:
        print("Hola", mid)
        encontrado = True
        return mid
    if right > left:
        z = _find_first(a, x, left, mid - 1, encontrado, num)
        if z != None:
            return z
        y = _find_first(a, x, mid + 1, right, encontrado, num)
        return y
def _find_last(a: list, x: int, left: int, right: int, encontrado: bool, num):
    if len(a) == 0 or a == None:
        return
    mid = (left + right) // 2
    if a[mid] == x and encontrado == False:
        print("Hola", mid)
        encontrado = True
        return mid
    if right > left:
        y = _find_first(a, x, mid + 1, right, encontrado, num)
        if y != None:
            return y
        z = _find_first(a, x, left, mid - 1, encontrado, num)
        z
