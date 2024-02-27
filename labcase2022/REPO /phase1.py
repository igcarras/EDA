from slist import SList
from slist import SNode
#Download stackLL.py and queueLLHT.py from aula global and copy them
#to the same directory
from stackLL import Stack
from queueLLHT import Queue

import sys

class SList2(SList):

    def sumLastN(self, n):
        """returns the addition of the last n elements of the list.
        O(n)"""
        if n<0:
            return None
        else:
            result=0
            node=self._head
            n=len(self)-n
            i=0
            while node:
                if i>=n:
                    result+=node.elem
                i+=1
                node=node.next

            return result

    #method for inserting a new node in the middle
    def insertMiddle(self, elem):
        """inserts the element elem at the middle of the list. O(n)"""
        if len(self)%2==0:
            self.insertAt(len(self)//2,elem)
        else:
            self.insertAt(len(self)//2+1,elem)


    def insertList(self,inputList,start,end):
        """removes the nodes from start and end positions, and insert the inputList
        between these positions. O(n)"""
        if start>=0 and start<=end and end<len(self):
            prev=None
            node=self._head
            i=0
            while i<start:
                prev=node
                node=node.next
                i+=1
            #node is the node at position start, prev is its previous node
            while i<=end:
                node=node.next
                i+=1
            #node is the node at position end+1

            if inputList.isEmpty():
                if prev==None:
                    self._head=node
                else:
                    prev.next=node
            else:
                lastInput=inputList._head
                while lastInput.next!=None:
                    lastInput=lastInput.next
                #lastInput is the last node of the input list
                lastInput.next=node

                if prev==None:
                    self._head=inputList._head
                else:
                    prev.next=inputList._head

            self._size=len(self)-(end-start)+len(inputList)



    def reverseK1(self,k):
        #O(n2)
        if k>1:
            q=Queue()
            node=self._head
            while node:
                i=1
                stack=Stack()
                while node and i<=k:
                    stack.push(node.elem)
                    i+=1
                    node=node.next

                while not stack.isEmpty():
                    q.enqueue(stack.pop())
            self._head=q._head


    def reverseK2(self,k):
        """reverse the list in groups of k elements. O(n2)"""
        if k>1:
            #first and last nodes of a new list to save the reverse list
            firstNode, lastNode = None, None

            node=self._head
            while node:
                i=0
                nodeStack=None
                while node and i<k:
                    newNode=SNode(node.elem)
                    if nodeStack!=None:
                        newNode.next=nodeStack
                    nodeStack=newNode
                    i+=1
                    node=node.next
                    #remove the firs node
                    self._head=node

                #node is at k+1 positions
                #we add nodes from nodeStack to the end of the list
                while nodeStack!=None:
                    newNode=SNode(nodeStack.elem)
                    if firstNode==None:
                        firstNode=newNode
                    else:
                        lastNode.next=newNode
                    lastNode=newNode

                    nodeStack=nodeStack.next
                # print(self)
w
            self._head=firstNode

    def reverseK(self,k):
        self._head=self._reverseK(self._head,k)

    def _reverseK(self, inputNode, k):
        """O(n)"""
        if inputNode==None:
            return None

        i=0
        node=inputNode
        nextNode=None
        prevNode=None
        while node and i<k:
            nextNode=node.next
            node.next=prevNode
            prevNode=node
            node=nextNode
            i+=1

        if nextNode is not None:
            inputNode.next = self._reverseK(nextNode, k)

        # prev is new _head of the input list
        return prevNode

    def maximumPair(self):
        """return the maximum sum of equidistant nodes.
        O(n)"""
        result=None
        if self.isEmpty():
            return result

        left=SList2()
        right=Queue()

        node=self._head
        for i in range(len(self)//2):
            left.addFirst(node.elem)
            node=node.next


        if len(self)%2!=0:
            middleElem=node.elem
            node=node.next

        for i in range(len(self)//2):
            right.enqueue(node.elem)
            node=node.next

        nodeL=left._head
        nodeR=right._head
        result=-sys.maxsize
        while nodeL and nodeR:
            sumPair=nodeL.elem+nodeR.elem
            if result<sumPair:
                result=sumPair
            nodeL=nodeL.next
            nodeR=nodeR.next

        if len(self)%2!=0:
            result=max(result,middleElem)

        return result


