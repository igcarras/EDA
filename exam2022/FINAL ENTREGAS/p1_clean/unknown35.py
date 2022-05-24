# MIKEL UGARTE PLAZAOLA
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if len(a)==0 or a is None:
        return -1,-1
    return _find_first_last(a,x,0,len(a)-1)
def _find_first_last(a:list,x:int,start:int,end:int):
    if start==end:
        if a[start]==x:
            return start,end
        else:
            return -1
    if start<end:
        mid=(start+end)//2
        index=_find_first_last(a,x,0,mid)
        if index==-1:
            return _find_first_last(a,x,mid+1,end,)
        return index
