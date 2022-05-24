#Ignacio Puy Escario
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    stack = []
    stack.insert(0, -1)
    stack.insert(0, -1)
    if a is None or len(a) == 0:
        return (-1, -1)
    return _find_first_last(a, x, 0, len(a)-1, stack)
def _find_first_last(a, x, start, end, stack):
    if start <= end:
        m = (start + end) // 2
        _find_first_last(a, x, start, m - 1, stack)
        if a[m] == x:
            stack.insert(0, m)
        _find_first_last(a, x, m + 1, end, stack)
    if len(stack) < 4:
        tuple = (stack[0], stack[0])
    else:
        tuple = (stack[-3], stack[0])
    return tuple
