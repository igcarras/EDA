#Mario Rodríguez Román Grupo 84
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    indices=[-1,-1]
    if len(a)>0:
        _find_first_last(a,x,0,len(a)-1,indices)
    return (indices[0],indices[1])


def _find_first_last(a:list,x:int,izq,drch,indices:list):
    if izq<=drch:
        mid=(izq+drch)//2
        _find_first_last(a,x,izq,mid-1,indices)
        if a[mid]==x:
            if indices[0]==indices[1]==-1:
                indices[0]=indices[1]=mid
            elif indices[0]>mid:
                indices[0]=mid
            elif indices[1]<mid:
                indices[1]=mid
        _find_first_last(a,x,mid+1,drch,indices)

if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
