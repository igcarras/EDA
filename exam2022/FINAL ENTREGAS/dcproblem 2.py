# Jaime Espada Santos
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if x == None or a == None or len(a) < 0: # Comprobamos si los parametros son correctos
        return (-1, -1)
    return _find_first_last(a, x, 0, len(a)-1) # LLamamos a la funcion recursiva

def _find_first_last(a: list, x: int, start: int, end: int) -> (int, int):
    if start == end: # Si unicamente hay un elemento en la lista
        if a[start] == x: # Comprobamos si es el que buscamos y lo devolvemos
            return (start, start)
        else: 
            return (-1, -1)
    if start < end: # Si hay mas elementos
        m = (start + end) // 2 # Dividimos la lista
        first1, last1 = _find_first_last(a, x, start, m) # Buscamos los respectivos indices
        first2, last2 = _find_first_last(a, x, m+1, end)
        
        if first1 != -1: # Si existe en la primera parte de la lista, es el que queremos
            first = first1
        elif first2 != None: # En caso contrario, cogemos en de la segunda parte
            first = first2     
        
        if last1 != None and last2 != None: # Si existe el indice que queremos
            if last1 >= last2: # Nos quedamos con el de mayor valor
                last = last1
            else:
                last = last2
            
        return (first, last) # Devuelve el primer y ultimo indice

    return (-1, -1)

if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
