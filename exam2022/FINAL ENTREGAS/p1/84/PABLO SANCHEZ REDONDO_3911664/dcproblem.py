def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if len(a) == 0 or x not in a:
        return (-1, -1)

    i = 0
    j = len(a) - 1
    mid = len(a) // 2
    punt_i = len(a) - 1
    punt_j = 0

    if len(a) > 1:
        find_first_last(a[0:mid], x)
        find_first_last(a[mid:], x)

    if len(a) == 1:
        if a[0] != x:
            i += 1
            j -= 1
        else:
            punt_i = i
            punt_j = j
        return i, j, punt_i, punt_j

    first = min(punt_i, i)
    last = max(punt_j, j)

    return (first, last)

if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
