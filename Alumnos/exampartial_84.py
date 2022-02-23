from slistHT import SList

class SList2(SList):
        """: función que modifica la lista invocante para que todos los
        elementos pares aparezcan antes que los elementos impares. La función debe
        respetar el orden de los elementos pares y el orden de los elementos impares."""
        def segregateOddEven(self):
            if len(self) > 1:

                evens = SList2()
                odds = SList2()
                node = self._head
                while node:
                    e = node.elem
                    if e % 2 == 0:
                        evens.addLast(e)
                    else:
                        odds.addLast(e)

                    node = node.next

                if evens.isEmpty():
                    self._head = odds._head
                    self._tail = odds._tail
                elif odds.isEmpty():
                    self._head = evens._head
                    self._tail = evens._tail
                else:
                    self._head = evens._head
                    evens._tail.next = odds._head
                    self._tail = odds._tail


if __name__=='__main__':
       #Please, uncomment the code for test each function

        l2=SList2()
        for i in [7, 0, 8, 7, 6, 1, 7, 10, 2, 0, 9]:
            l2.addLast(i)
        print(l2)

        print("before segregateOddEven:",l2)
        l2.segregateOddEven()
        print("after segregateOddEven:",l2)