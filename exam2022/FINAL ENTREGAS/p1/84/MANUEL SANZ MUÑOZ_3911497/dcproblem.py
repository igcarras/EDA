def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    first = last = -1
    if x in a:
        if len(a) == 1:
            return 0,0

        else:
            mid = len(a) // 2

            first_, last_ = _find_first_last(a[0:mid], x, 0)
            first, last = elegir(first, last, first_, last_)

            first_, last_ = _find_first_last(a[mid:], x, mid)
            first, last = elegir(first, last, first_, last_)

    return first, last


def _find_first_last(a:list, x:int, i:int) -> tuple:
    first = last = -1
    if x in a:
        if len(a) == 1:
            first, last = elegir(first, last, i, i)

        else:
            mid = len(a) // 2

            first_, last_ = _find_first_last(a[0:mid], x, i)
            first, last = elegir(first, last, first_, last_)

            first_, last_ = _find_first_last(a[mid:], x, mid+i)
            first, last = elegir(first, last, first_, last_)

    return first, last


def elegir(first, last, first_, last_) -> tuple:
    if first == -1 or first_ < first_:
        first = first_
    if last_ > last:
        last = last_
    return first, last


if __name__ == "__main__":
    b = [4, 1, 7, 4, 4, 8, 8, 3, 1, 2]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 0   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
    a = find_first_last(b, 0)
    print(a)

    b = [4]
    value = 4  # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)



"""
def find_first_last(a: list, x: int) -> (int, int):
    first = last = -1
    if x in a:
        if len(a) == 1:
            return [0,0]
        else:
            mid = len(a)//2
            first, last = _find_first_last(a[0:mid], x, 0, first, last)
            first, last = _find_first_last(a[mid:], x, mid, first, last)
    return first, last


def _find_first_last(a:list, x:int, i:int, first, last) -> tuple:
    if x in a:
        if len(a) == 1:
            if i > last:
                last = i
            if i < first or first == -1:
                first = i
        else:
            mid = len(a) // 2
            first, last = _find_first_last(a[0:mid], x, i, first, last)
            first, last = _find_first_last(a[mid:], x, mid+i, first, last)
    return first, last"""