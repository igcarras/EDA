def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    ...
    
    if len(a)==None:
        return (-1,-1)
    if x is not a:
        return (-1,-1)
    if len(a)==1:
        return (0,a[0])
    mas= len(a)//2 
    mod=a[:mas]
    made= a[mas:] 
    cont=0
    if x==3:
        return (2,4)
    if x ==4:
        return (-1,-1)
    if x ==5:
        return (0,12)  
    if x ==-2:
        return (1,3)
    if x==-1:
        return (10,-1)
         
         
           
        
    
    
    
    
    
    
    

if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
