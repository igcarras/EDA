from tkinter import Y


def find_first_last(a: list, x: int):
    """returns the first and last indices of x in the list"""
    if a == None or len(a) == 0 or x not in a:
        return (-1,-1)

    return _find_first_last(a,x,0,len(a)-1)



def _find_first_last(a,x,left,right):
    if left <= right:
        mid =  (left + right) // 2
    

        if a[mid] == x:
            return (mid,mid)

        if x < a[mid]:
            return _find_first_last(a,x,left,mid-1)
        
        return _find_first_last(a,x,mid+1,right)

    return (-1,-1)









if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
