#  Daniel Parente Contreras


def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if len(a) == 0:
        return (-1, -1) #  Comprobacion inicial para descartar listas vacias
    resultado = [float('inf'), -float('inf')] #  Valores iniciales que serán sustitudios cuando encontremos x
    return _find_first_last(a, x, resultado, 0)

def _find_first_last(a: list, x: int, resultado: list, posicion):
    if posicion >= len(a): #  Cuando se llega al final de la lista se devuelve el resultado con el formato correcto
        if resultado[0] == float('inf'): #  Se cambian los valores por defecto por "-1" en caso de que sea necesario
            resultado[0] = -1
        if resultado[1] == -float('inf'):
            resultado[1] = -1
        return tuple(resultado)
    if a[posicion] == x: # Comprobacion de que estamos en el valor que buscamos
        if posicion <= resultado[0]: # Se comprueba si la posicion actual es valida como primera o ultima ocurrencia
            resultado[0] = posicion
        if posicion >= resultado[1]:
            resultado[1] = posicion            
    return _find_first_last(a, x, resultado, posicion + 1) # Se vuelve a llamar a la funcion, esta vez con 
if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
