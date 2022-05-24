def find_first_last(a: list, x: int):
    """returns the first and last indices of x in the list"""
    if a is None or len(a)==0 or x is None:
        return (-1,-1)
    t=len(a)
    return _find_first_last(a,x,0,t-1)
def _find_first_last(a:list,x:int,l,r):
    if l>r or l<0 or r>=len(a):
        return (-1,-1)
    if l==r:
        return(a[l],a[l])
    mid=(l+r)//2
    (l[0],l[-1])= _find_first_last(a,x,l,mid)
    (r[0], r[-1])= _find_first_last(a,x,mid+1,r)
    if l[0]>r[0] and r[-1]>l[-1]:
        return (l[0],r[-1])
    if l[0]>r[0] and r[-1]<l[-1]:
        return (r[0],l[-1])
    if l[0]<r[0] and r[-1]>l[-1]:
        return (l[0],r[-1])
    if l[0]<r[0] and r[-1]<l[-1]:
        return (l[0],l[-1])
    if l[0]==r[0] and r[-1]<l[-1]:
        return (l[0],l[-1])
    if l[0]==r[0] and r[-1]>a[-1]:
        return (l[0],r[-1])
    if a[0]<r[0] and r[-1]==l[-1]:
        return (l[0],l[-1])
    if l[0]>r[0] and r[-1]==l[-1]:
        return (r[0],l[-1])
