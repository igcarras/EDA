def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    currentIndex=-1
    result=[None,None]
    _find_first_last(a,x,currentIndex,result)
    if(result == [None,None]):
        return (-1,-1)
    if(result[0]==None):
        return(result[1],result[1])
    if(result[1]==None):
        return(result[0],result[0])
    return (result[0],result[1])
def _find_first_last(a:list,x:int,currentIndex,result):
    if(x==None):
        return [-1,-1]
    if(len(a)==0 or a==None):
        return None
    if(len(a)==1):
        currentIndex=currentIndex+1
        if(a[0]==x):
            return currentIndex,currentIndex
        return None,currentIndex
    mid = len(a)//2
    result1,currentIndex = _find_first_last(a[0:mid],x,currentIndex,result)
    result2,currentIndex =_find_first_last(a[mid:len(a)],x,currentIndex,result)
    if result1 !=None:
        if result[0]!=None:
            result[1]=result1
        elif result[0]==None and result[0]!=0:
            result[0]=result1
    if result2!=None:
        if result[0]!=None :
            result[1]=result2
        elif result[0]==None and result[0]!=0:
            result[0]=result2
    return None,currentIndex
prueba = [-1, 0, -1, 0, 3, 6, 6, 0, 1, 2, 0, 0, -1]
find_first_last(prueba, -1222)
