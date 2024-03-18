from slistHT import SList

class SList2(SList):
    def move_duplicates_to_end(self):
        if self.is_empty():
            return

        current = self._head
        last_node = self._tail
        count = 0
        while count < self.__len__() and (current is not last_node):
            if current.next and (current.elem == current.next.elem):
                duplicate = current.next
                successive = duplicate.next
                if successive is not None:
                    current.next = successive
                    self._tail.next = duplicate
                    self._tail = duplicate
                    self._tail.next = None
                    count=count+1
                else:
                    current = current.next
                    count = count + 1
            else:
                current = current.next
                count = count + 1


    def move_duplicates_to_end_2(self):
        if len(self) > 1:
            prev = self._head
            current = prev.next
            final = self._tail
            while current and prev != final:
                if prev.elem == current.elem and current.next!=None:
                    prev.next = current.next
                    self._tail.next = current
                    self._tail = current
                    self._tail.next = None
                    current = prev.next
                else:
                    prev = current
                    current = current.next
if __name__ == '__main__':
    slist = SList2()
    slist.add_last(1)
    #slist.add_last(1)
    slist.add_last(2)
    #slist.add_last(3)
    slist.add_last(3)
    slist.add_last(3)
    #slist.add_last(4)
    #slist.add_last(5)

    print("Lista original:", slist)
    slist.move_duplicates_to_end()
    print("Lista después de mover duplicados al final:", slist)
