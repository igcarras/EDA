#Alberto Casas Ramirez Grupo 84


def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    return _find_first_last(a, x, 0, len(a)-1)

def _find_first_last(a: list, x: int, left: int, right: int) -> (int, int):
    if right-left < 2:
        if len(a)!=0 and a[left] == x:
            return (left, left)
        return (-1, -1)
    if right-left == 2:
        if a[left] == x or a[right] == x:
            if a[left] == a[right]:
                return (left, right)
            if a[left] == x:
                return (left, left)
            return (right, right)
        return (-1, -1)


    if a[left] == x and a[right] == x:
        return (left, right)
    if a[left] == x:
        if (right - left) > 2:
            return (left, _find_first_last(a, x, (right-left)//2, right)[1])
        else:
            return (left, left)
    if a[right] == x:
        if (right - left) > 2:
            return (_find_first_last(a, x, left, ((right-left)//2)-1)[0], right)
        else:
            return (right, right)
    return (
        _find_first_last(a, x, left, ((right-left)//2)-1)[0],
        _find_first_last(a, x, (right-left)//2, right)[1]
    )

if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)