def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if a == None or len(a)==0:
        return (-1,-1)
    return _find_first_last(a,x,0,len(a)-1)
def _find_first_last(a,x,start,end):
    if start == end:
        if a[start] == x:
            return (start,start)
        else:
            return (-1,-1)
    if start < end:
        m = (start + end) // 2
        index1 = _find_first_last(a, x, start, m)
        index2 = _find_first_last(a, x, m + 1, end)
        return max(index1, index2)
    return (-1,-1)


if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
