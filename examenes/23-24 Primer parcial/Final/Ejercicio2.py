from slistHT import SList

class SList2(SList):
    def move_duplicates_to_end(self):
        if self.is_empty():
            return

        current = self._head
        last_node = self._tail

        while current is not last_node.next:
            if current.next and (current.elem == current.next.elem):
                print("estoy en ", current.elem)

                duplicate = current.next
                print("siguiente es:", duplicate.elem)
                successive = duplicate.next
                if successive is not None:
                    current.next = successive
                    self._tail.next = duplicate
                    self._tail = duplicate
                    self._tail.next = None
                else:
                    print("entro aqui")
                    current = current.next

            else:
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
