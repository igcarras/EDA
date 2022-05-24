# ALUMNO: JAVIER PRATS MUÑOZ
# GRUPO: 84
def find_first_last(a: list, x: int) -> (int, int):
    # returns the first and last indices of x in the list
    if len(a) == 0:
        return -1, -1
    first_last = _find_first_last(a, x, 0, len(a) - 1)
    if first_last[0] == None and first_last[1] == None:
        return -1, -1
    elif first_last[0] == None:
        return first_last[1], first_last[1]
    elif first_last[1] == None:
        return first_last[0], first_last[0]
    return first_last[0], first_last[1]
def _find_first_last(a: list, x: int, start: int, end: int) -> (int, int):
    mid = (start + end) // 2
    if start < end:
        variable1, variable2 = _find_first_last(a, x, start, mid)
        if a[mid] == x:
            if (not variable1) and (not variable2):
                return mid, mid
            if not variable1:
                return mid, variable2
            else:
                return variable1, mid
        variable1, variable2 = _find_first_last(a, x, mid + 1, end)
        return variable1, variable2
    return None, None
