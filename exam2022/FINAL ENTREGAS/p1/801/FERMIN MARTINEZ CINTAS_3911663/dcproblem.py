from turtle import left, right


def find_first_last(a: list, x: int):
    """returns the first and last indices of x in the list"""
    if a == None or len(a) == 0:
        return (-1, -1)
    return _find_first_last(a,x,0,len(a) - 1)
def _find_first_last(a, x, left, right):
    min = -1
    max = -1
    if left >= right:
        m = len(a)//2
        _find_first_last(a, x, left, m -1)
        if a[m] == x:
            if min == -1:
                min = m
            if m > max:
                max = m
        _find_first_last(a, x, m + 1, right)
    return (min, max)





if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
