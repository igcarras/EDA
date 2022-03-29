from slist import SList
from slist import SNode
import sys


class SList2(SList):

    def sumLastN(self, n):
        if self.isEmpty() == True:
            print("Error: list is empty!")
            return 0
        else:
            if n < 0:
                return None
            elif n >= self._size:
                total = 0
                for i in range(self._size):
                    ultimo = self.getAt(i)
                    total += ultimo
            elif 0 < n < self._size:
                total = 0
                for i in range(n):
                    ultimo = self.getAt(len(self) - 1 - i)
                    total += ultimo

            return total

    def insertMiddle(self, elem):
        node1 = self._head
        if self.isEmpty():
            self.addFirst(elem)
        else:
            if self._size % 2 == 0:
                m = self._size // 2 - 1
                for i in range(m):
                    node1 = node1.next
            else:
                m = self._size // 2
                for i in range(m):
                    node1 = node1.next

            node2 = SNode(elem)
            node2.next = node1.next
            node1.next = node2
            self._size += 1

    def insertList(self, inputList, start, end):
        node1 = self._head
        l = end - start
        if start >= 0 and start <= end and end + 1 <= self._size:
            if start == 0:
                for i in range(end + 1):
                    self.removeFirst()
                for j in range(inputList._size):
                    n = inputList.removeLast()
                    self.addFirst(n)
            else:
                for i in range(start):
                    node1 = node1.next
                for j in range(l + 1):
                    self.removeAt(self.index(node1.elem))
                    node1 = node1.next
                for k in range(inputList._size):
                    n = inputList.removeFirst()
                    self.insertAt(start + k, n)

    def reverseK(self, k):
        laux = SList2()
        if k > 1:
            for i in range(self._size//k):
                lsub = SList2()
                for j in range(k):
                    lsub.addFirst(self.getAt(j + k * i))
                for z in range(k):
                    laux.addLast(lsub.getAt(z))
            if self._size % k != 0:
                lsub = SList2()
                for a in range(self._size - k * (self._size//k)):
                    lsub.addFirst(self.getAt((self._size//k) * k + a))
                for b in range(self._size - k * (self._size//k)):
                    laux.addLast(lsub.getAt(b))
            self.insertList(laux, 0, self._size - 1)

    def maximumPair(self):
        laux = SList2()
        if self.isEmpty():
            return None
        elif self._size % 2 == 0:
            for a in range(self._size // 2):
                laux.addFirst(self.removeFirst() + self.removeLast())
        else:
            for a in range((self._size - 1) // 2):
                laux.addFirst(self.removeFirst() + self.removeLast())
            laux.addFirst(self.removeFirst())
        Node1 = laux._head
        x = 0
        for a in range(laux._size):
            if Node1.elem > x:
                x = Node1.elem
            Node1 = Node1.next
        return x