def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    visitados={}
    for i in range(len(a)):
        visitados[i]=False
    if a == None or len(a)==0:
        return (-1,-1)
    if _find_first(a,x,0,len(a)-1,visitados)==-1 and _find_last(a,x,0,len(a)-1,visitados)!=-1:
        return _find_last(a,x,0,len(a)-1,visitados),_find_last(a,x,0,len(a)-1,visitados)
    elif _find_first(a,x,0,len(a)-1,visitados)!=-1 and _find_last(a,x,0,len(a)-1,visitados)==-1:
        return _find_first(a,x,0,len(a)-1,visitados),_find_first(a,x,0,len(a)-1,visitados)
    return _find_first(a,x,0,len(a)-1,visitados),_find_last(a,x,0,len(a)-1,visitados)
def _find_first(a,x,start,end,visitados)->int:
    indice=-1
    if x not in a:
        return -1
    m= (start+end)//2
    if x==a[m] and visitados[m]==False:
        indice=m
        visitados[m]=True
        m=m-1
        if x==a[m] and x==a[0]:
            return 0
    if x<a[m] and visitados[m]==False:
        return _find_first(a,x,start,m,visitados)
    if visitados[m]==True:
        return indice
def _find_last(a,x,start,end,visitados):
    indice = -1
    if x not in a:
        return -1
    m = (start + end) // 2
    if x == a[m] and visitados[m] == False:
        indice = m
        visitados[m] = True
        m = m + 1
    if x==a[m] and x==[len(a)-1]:
        return
    if x > a[m]:
        return _find_first(a, x, start, m, visitados)
    if visitados[m] == True:
        return indice
