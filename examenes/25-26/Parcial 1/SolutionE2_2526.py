class DNode:
    def __init__(self, e, n=None, p=None):
        self.elem = e
        self.next = n
        self.prev = p


class DList:
    def __init__(self):
        """creates an empty list"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        """Checks if the list is empty"""
        # return self.head == None
        return len(self) == 0

    def addLast(self, e):
        """Add a new elem, e, at the end of the list"""
        # create the new node
        newNode = DNode(e)

        if self.isEmpty():
            self._head = newNode
        else:
            newNode.prev = self._tail
            self._tail.next = newNode

        # update the reference of _head to point the new node
        self._tail = newNode
        # increase the _size of the list
        self._size = self._size + 1

    def removeFirst(self):
        """Returns and remove the first elem of the list"""
        if self.isEmpty():
            print("Error: list is empty")
            return None

        result = self._head.elem
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        else:
            self._head.prev = None

        self._size = self._size - 1
        return result

    def ringList(self, s):
        other = DList()
        if s > 0 and s <= self._size:
            for i in range(0, s):
                """order of complexity O(n)"""
                other.addLast(self.removeFirst())
            other._tail.next = other._head
            other._head.prev = other._tail
            return other
        else:
            print("error: wrong size")
            return None

    def ringList2(self, s):

        if self._size > 0:
            other = DList()
            if s >= self._size:
                other._head = self._head
                other._tail = self._tail

                self._head = None
                self._tail = None

                other._tail.next = other._head
                other._head.prev = other._tail

                other._size = self._size
                self._size = 0

                return other
            else:
                current = self._head
                i = 0
                while i < s:
                    current = current.next
                    i += 1
                other._head = self._head
                other._tail = current
                self._head = current.next
                self._head.prev = None
                other._tail.next = other._head
                other._head.prev = other._tail

                other._size = s
                self._size = self._size - s

            return other
        return None

    def ringList3(self, s):
        if self._size > 0:
            other = DList()

            if s >= self._size:
                other._head = self._head
                other._tail = self._tail
                other._size = self._size

                other._tail.next = other._head
                other._head.prev = other._tail

                self._head = None
                self._tail = None
                self._size = 0

                return other

            elif s > 0:
                current = self._head
                i = 1
                while i < s:
                    current = current.next
                    i += 1

                other._head = self._head
                other._tail = current

                self._head = current.next
                self._head.prev = None

                other._tail.next = other._head
                other._head.prev = other._tail

                other._size = s
                self._size = self._size - s

                return other

            return other

        return
