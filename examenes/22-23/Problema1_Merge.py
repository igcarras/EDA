from slistHT import SList


class MySList(SList):
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
        if self.isSorted() == False or other.isSorted() == False:
            # print('Error: both list must be sorted')
            return None

        listMerged = MySList()

        node1 = self._head
        node2 = other._head

        # Aunque tengamos bucles anidados, la complejidad no aumenta porque los nodos que saltamos no se vuelven a visitar
        while node1 and node2:
            # we hop all repeated nodes
            while node1.next and node1.elem == node1.next.elem:
                node1 = node1.next

            while node2.next and node2.elem == node2.next.elem:
                node2 = node2.next

            # print(node1.elem, node2.elem)

            if node1.elem < node2.elem:
                listMerged.add_last(node1.elem)
                node1 = node1.next
            elif node2.elem < node1.elem:
                listMerged.add_last(node2.elem)
                node2 = node2.next
            else:
                # no duplicates allowed
                listMerged.add_last(node1.elem)
                node1 = node1.next
                node2 = node2.next

        # if the there are still elements in self (list)

        if node1:
            while node1.next:
                if node1.elem < node1.next.elem:
                    # no duplicates allowed
                    listMerged.add_last(node1.elem)
                node1 = node1.next
            if listMerged._tail.elem != node1.elem:
                listMerged.add_last(node1.elem)

            # if the there are still elements in other (list)
        if node2:
            while node2.next:
                if node2.elem < node2.next.elem:
                    # no duplicates allowed
                    listMerged.add_last(node2.elem)
                node2 = node2.next

            if listMerged._tail.elem < node2.elem:
                listMerged.add_last(node2.elem)

        return listMerged


import random

if __name__ == '__main__':
    # Please, uncomment the code for test each function
    l2 = MySList()

    for i in range(10):
        l2.add_last(random.randint(0, 20))
    print(l2)

    l3 = MySList()
    for i in range(10):
        l3.add_last(i)

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
        l2.add_last(x)

    data = []
    for i in range(7):
        x = random.randint(0, 10)
        if x not in data:
            data.append(x)

    data.sort()
    l3 = MySList()
    for x in data:
        l3.add_last(x)

    print('l2:', str(l2))
    print('l3:', str(l3))
    print("List merged:", str(l2.merge(l3)))
    print("List merged:", str(l3.merge(l2)))
