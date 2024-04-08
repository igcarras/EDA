from slistHT import SList

class SList2(SList):

    def move_duplicates_to_end(self):
        if self.is_empty():
            return

        current = self._head
        count = 0
        while count < self.__len__():
            if current.next and (current.elem == current.next.elem):
                duplicate = current.next
                successive = duplicate.next
                if duplicate is not self._tail:
                    current.next = successive
                    self._tail.next = duplicate
                    self._tail = duplicate
                    self._tail.next = None
                else:
                    current = current.next
            else:
                current = current.next

            count = count + 1

    def move_duplicates_to_end1(self):
        if len(self) > 1:
            prev = self._head
            current = prev.next
            for i in range(1,len(self)):
                if prev.elem == current.elem and current.next!=None:
                    prev.next = current.next
                    self._tail.next = current
                    self._tail = current
                    self._tail.next = None
                    current = prev.next
                else:

                    prev = current
                    current = current.next

    def move_duplicates_to_end3(self):
        if len(self) > 0:
            prev=self._head
            aux=prev.next
            for i in range (len(self)-2):
                if prev.elem == aux.elem:
                    prev.next = aux.next
                    self._tail.next = aux
                    self._tail = aux
                    self._tail.next = None
                else:
                    prev=aux
                aux=aux.next
        else:
            return

    def move_duplicates_to_end2(self):
        if len(self)>2:
            nodeit=self._head
            aux = nodeit.next
            count = 0
            while count < self.__len__()-1:
                while nodeit.elem == aux.elem:
                    if aux.next:
                        nodeit.next=aux.next
                        aux.next=None
                        self._tail.next=aux
                        self._tail=aux
                        aux=nodeit.next
                        count+=1
                nodeit=aux
                aux=aux.next
                count+=1


if __name__ == '__main__':
    slist = SList2()
    slist.add_last(1)
    slist.add_last(2)
    slist.add_last(2)
    slist.add_last(2)
    slist.add_last(2)
    slist.add_last(2)
    slist.add_last(2)

    print("Lista original:", slist)
    slist.move_duplicates_to_end2()
    print("Lista después de mover duplicados al final:", slist)
