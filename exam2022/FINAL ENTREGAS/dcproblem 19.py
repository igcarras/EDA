def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    """returns the list of indices for x in data"""
    if a == None or len(a) == 0:
        return (-1,-1)

    return ((_getIndices(a, x, 0, len(a) - 1, []))[0], (_getIndices(a, x, 0, len(a) - 1, []))[-1])


def _find_first_last(data, x, left, right, indices):
    if left <= right:
        mid = (left + right) // 2

        _getIndices(data, x, left, mid - 1, indices)

        if data[mid] == x:
            indices.append(mid)

        _getIndices(data, x, mid + 1, right, indices)

    return indices



def getIndices(data, x):
    """returns the list of indices for x in data"""
    if data == None or len(data) == 0:
        return []

    return _getIndices(data, x, 0, len(data) - 1, [])


def _getIndices(data, x, left, right, indices):
    if left <= right:
        mid = (left + right) // 2

        _getIndices(data, x, left, mid - 1, indices)

        if data[mid] == x:
            indices.append(mid)

        _getIndices(data, x, mid + 1, right, indices)

    return indices

if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)

    print(find_first_last(b,5))
    """for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)"""
