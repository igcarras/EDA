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
