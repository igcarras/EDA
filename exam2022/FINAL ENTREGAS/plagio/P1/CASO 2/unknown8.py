#Mario Salvador Camacho
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if x not in a or len(a) == 0:
        return(-1,-1)
    if len(a) == 1 and a[0] == x:
        return(0,0)
    principio = -1
    for i in range(len(a)):
        if a[i] == x:
            principio = i
            break
    if principio ==-1:
        return(-1,1)
    final = i
    list_aux = a[i: ]
    if len(list_aux) == 1:
        return(i,i)
    for k in range(len(list_aux)):
        if list_aux[k] == x:
            final = k
            final = i + k
    return(principio,final)
