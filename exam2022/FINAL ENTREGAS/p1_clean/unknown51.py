#Paula Subías Serrano
def find_first_last(a: list, x: int) -> (int, int):
    """returns the first and last indices of x in the list"""
    if len(a) == 0:
        return -1, -1
    if x not in a:
        return -1, -1
