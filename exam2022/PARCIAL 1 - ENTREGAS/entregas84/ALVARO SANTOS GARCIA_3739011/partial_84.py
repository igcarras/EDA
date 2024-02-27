class SNode:
    def __init__(self, e, next=None):
        self.elem = e
        self.next = next


class MySList():

    def __init__(self):
        self._head = None
        self._tail = None

    def __str__(self):
        """Returns a string with the elements of the list"""
        ###This functions returns the same format used
        ###by the Python lists, i.e, [], ['i'], ['a', 'b', 'c', 'd']
        ###[1], [3, 4, 5]
        nodeIt = self._head
        result = '['
        while nodeIt:
            result += str(nodeIt.elem) + ", "
            nodeIt = nodeIt.next

        if len(result) > 1:
            result = result[:-2]

        result += ']'
        return result

    def append(self, e):
        """Adds a new element, e, at the end of the list"""
        # create the new node
        newNode = SNode(e)
        # the last node must point to the new node
        # now, we must update the _tail reference
        if self._head == None:
            self._head = newNode
        else:
            self._tail.next = newNode

        self._tail = newNode

    def isSorted(self):
        "returns True if self is sorted"
        if self._head == None:
            return True
        else:
            node1 = self._head
            node2 = node1.next
            while node2:
                if node1.elem > node2.elem:
                    return False
                node1 = node2
                node2 = node2.next

        return True

    def merge(self, other):
        "Merge of two ordered lists. No duplicates allowed."
        result = 0
        if other.isSorted() == False:
            result = None
        elif self.isSorted() == False:
            result = None
        elif self._head == None or other._head == None:
            if self._head == None:
                aux = other._head
            else:
                aux = self._head
            newlist = MySList()

            introducido = 0
            while aux != None:
                if newlist._head == None:
                    introducido = aux.elem
                    newlist.append(aux.elem)
                elif introducido < aux.elem:
                    introducido = aux.elem
                    newlist.append(aux.elem)
                aux = aux.next
            result = newlist.__str__()
        else:
            newlist = MySList()
            aux1 = self._head
            aux2 = other._head
            introducido = -1
            while (aux1 != None and aux2 != None):
                if newlist._head == None:
                    if aux1.elem < aux2.elem:
                        newlist.append(aux1.elem)
                        aux1 = aux1.next
                        introducido = aux1.elem
                    else:
                        newlist.append(aux2.elem)
                        aux2 = aux2.next
                        introducido = aux2.elem
                else:
                    if aux1.elem < aux2.elem:
                        introducido = aux1.elem
                        newlist.append(aux1.elem)
                        aux1 = aux1.next
                    elif aux1.elem > aux2.elem:
                        introducido = aux2.elem
                        newlist.append(aux2.elem)
                        aux2 = aux2.next
                    elif aux1.elem == aux2.elem:
                        if aux1.elem > introducido:
                            newlist.append(aux1.elem)
                        aux1 = aux1.next
                        aux2 = aux2.next
            newlist2 = MySList()
            aux = newlist._head
            introducido = 0
            while aux != None:
                if newlist2._head == None:
                    introducido = aux.elem
                    newlist2.append(aux.elem)
                elif introducido < aux.elem:
                    introducido = aux.elem
                    newlist2.append(aux.elem)
                aux = aux.next
            result = newlist2.__str__()

        return  result






import random

if __name__ == '__main__':
    # Please, uncomment the code for test each function
    l2 = MySList()

    for i in range(10):
        l2.append(random.randint(0, 20))
    print(l2)

    l3 = MySList()
    for i in range(10):
        l3.append(i)

    print('l2:', str(l2))
    print('l3:', str(l3))

    print("List merged:", str(l2.merge(l3)))
    print("List merged:", str(l3.merge(l2)))

    data = []
    for i in range(5):
        x = random.randint(0, 10)
        if x not in data:
            data.append(x)

    data.sort()
    l2 = MySList()
    for x in data:
        l2.append(x)

    data = []
    for i in range(7):
        x = random.randint(0, 10)
        if x not in data:
            data.append(x)

    data.sort()
    l3 = MySList()
    for x in data:
        l3.append(x)

    print('l2:', str(l2))
    print('l3:', str(l3))
    print("List merged:", str(l2.merge(l3)))
    print("List merged:", str(l3.merge(l2)))

