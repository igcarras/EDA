# Daniel Sánchez de la Cruz NIA: 100475344
# Simón Benzaquen Aserraf   NIA: 100475237

from slist import SList, SNode
import sys


class SList2(SList):
    # O(n)
    def sumLastN(self, n):
        # Check for a valid n value
        if n < 0:
            return None
        elif n == 0:
            return 0
        else:
            # Calculate the index at which the sum starts (e.g. if list _size is 5 and n is 2, starting index is 3 (sum 3 and 4))
            sum = 0
            sum_start_index = len(self) - n

            # Iterate through list
            aux = self._head
            i = 0
            while aux:
                # Sum only the last n terms
                if i >= sum_start_index:
                    sum += aux.elem

                aux = aux.next
                i += 1
            
            return sum

    # O(n)
    def insertMiddle(self, elem):
        # Add elem if list is empty
        if len(self) == 0:
            self.addFirst(elem)
            return
        else:
            # Check if list is odd or even
            if len(self) % 2 == 0:
                index = len(self) // 2
            else:
                index = (len(self) + 1) // 2
            
            # Iterate through list and stop at the node previous to the new node
            previous = self._head
            for i in range(index - 1):
                previous = previous.next
            
            # Add new node and increase list _size
            newNode = SNode(elem)
            newNode.next = previous.next
            previous.next = newNode
            self._size += 1
    
    # O(n)
    def insertList(self, inputList, start, end):
        # Check for valid start and end values
        if not ((start >= 0) and (start <= end) and (end < len(self))):
            return
        else:
            # Store inputList _tail reference
            aux = inputList._head
            while aux.next:
                aux = aux.next
            input_list_tail = aux
            
            # Store main list start and end nodes references
            aux = self._head
            start_node = self._head
            i = 0
            while i < end:
                if i == start - 1:
                    start_node = aux
                aux = aux.next
                i += 1
            end_node = aux.next

            # Move _head reference if inputList is inserted at the beginning of the main list,
            # else connect start node to inputList _head
            if start == 0:
                self._head = inputList._head
            else:
                start_node.next = inputList._head

            # Link inputList _tail to end node of main list and update list _size
            input_list_tail.next = end_node
            self._size = len(self) + inputList._size - (end - start + 1)

    # O(n)
    def reverseK(self, k):
        # Check for a valid k value
        if k <= 1 or len(self) == 0:
            # No changes
            return
        elif k >= len(self):
            # Reverse entire list
            auxlist = SList()
            aux = self._head
            while aux:
                auxlist.addFirst(aux.elem)
                aux = aux.next

            self._head = auxlist._head
            return
        else:
            # Call recursive auxiliary function
            aux = self._head
            self._head = self._reversegroup(aux, k)
    
    # Recursive aux function for reverseK
    def _reversegroup(self, aux, k):
        # Return if we reach the end of the main list
        if not aux:
            return None
        else:
            group = SList()

            # Do-while loop that saves the group _tail as we need it later
            group.addFirst(aux.elem)
            tail = group._head
            aux = aux.next
            for i in range(k - 1):
                group.addFirst(aux.elem)
                aux = aux.next

                # Return if last group _size is less than k
                if not aux:
                    return group._head
            
            # Connect group _tail to the next group _head
            tail.next = self._reversegroup(aux, k)
            return group._head

    # O(n)
    def maximumPair(self):
        # Return None if list is empty, or first element if list has only one node
        if len(self) == 0:
            return None
        elif len(self) == 1:
            return self._head.elem
        else:
            # Store in an auxiliary list the reversed second half of the main list
            auxlist = SList()
            aux1 = self._head
            i = 0
            while aux1:
                if i >= len(self) // 2 + len(self) % 2:
                    auxlist.addFirst(aux1.elem)
                
                aux1 = aux1.next
                i += 1
            
            # Iterate through both lists and check equidistant nodes sum
            aux1 = self._head
            aux2 = auxlist._head
            max_sum = -99
            while aux2:
                sum = aux1.elem + aux2.elem
                if sum > max_sum:
                    max_sum = sum
                
                aux1 = aux1.next
                aux2 = aux2.next

            # If main list is odd, check middle node element (one more node after comparing both lists)
            if len(self) % 2 != 0 and aux1.elem > max_sum:
                max_sum = aux1.elem

            return max_sum
                
