def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    return _find_first_last(a,x,0,len(a)-1)
def _find_first_last(a:list, x:int, izq:int, der:int):
    #Casos base
    if a == None or len(a) == 0:
        return (-1,-1)
    if x not in a :
        return(-1,-1)
    if len(a) == 1:
        if a[izq] == 0:
            return (izq,izq)
        else:
            return(-1,-1)
    #Empezamos a comprobar el resto de casos
    if a[izq] == x and a[der] == x:
        return(izq, der)
    if a[izq] == x:
        if der - izq > 2:
            return (izq, _find_first_last(a, x, (der-izq)//2, der)[1])
        else:
            return (izq, izq)
    if a[der] == x:
        if der - izq > 2:
            return (_find_first_last(a, x, izq, ((der-izq)//2)-1)[0], der)
        else:
            return (der,der)
    #Al hacer este return me peta el terminal pero no se porque , entonces lo dejo comentado
    #return (
       # _find_first_last(a, x, izq, ((der-izq)//2)-1)[0],
       # _find_first_last(a, x, (der-izq)//2, der)[1]
    #)
