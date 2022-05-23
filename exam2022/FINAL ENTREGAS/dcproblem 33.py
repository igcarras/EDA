#Álvaro Moreno Martín

def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if x not in a:
        return (-1,-1)
    if a == []:
        return (-1,-1)
    ocurrencias = 0
    pos1 = 0
    pos2 = 0
    for numero in a:
        if numero != x:
            pos1 += 1
            pos2 += 1
        if numero == x:
            ocurrencias += 1
            break
    if ocurrencias == 1:
        return (pos1,pos1)













if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
