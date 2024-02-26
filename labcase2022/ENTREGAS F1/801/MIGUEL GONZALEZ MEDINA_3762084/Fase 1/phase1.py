    from slist import SList,SNode
import sys
import math

class SList2(SList,SNode):

    def sumLastN(self, n):
        suma=0
        current =0
        aux = self._head
        if (self.__len__()==0):
            print("list is empty")
            return 0
        if n<=0:
            print("Index is not big enough")
            return None
        if n > self.__len__():
           while aux != None:
               suma+=aux.elem
               aux = aux.next 
           print(suma)     
           return suma
        while aux !=None:
            # print(self.__len__(), current,n)
            current+=1
            if self.__len__()-current<n:
                suma+=aux.elem
            aux=aux.next
        print(suma)
        return suma
        

    #method for inserting a new node in the middle
    def insertMiddle(self, elem):

        newNode = SNode(elem)

        if self.isEmpty():
            self._head = newNode
        elif self._size == 1:
            self._head.next = newNode
        else:
            aux = self._head.next
            prev = self._head
            contador = 0
            if self._size % 2 == 0:
                while contador != (self._size // 2) - 1:
                    aux = aux.next
                    prev = prev.next
                    contador += 1
                prev.next = newNode
                newNode.next = aux
            else:
                while contador != (self._size // 2):
                    aux = aux.next
                    prev = prev.next
                    contador += 1
                prev.next = newNode
                newNode.next = aux


    def insertList(self,inputList,start,end):
        if(self.isEmpty()==True):   
            print("self list is empty")
            return 
        if(inputList.isEmpty()==True):
            print("Input list is empty")
            return
        startNode =None
        endNode = None
        aux = self._head
        counter = 0
        #First: we get the nodes start and end (for this we need to loop)
        while aux != None:
            if (counter+1== start):
                startNode = aux
            if(counter-1 ==end):
                endNode=aux
            aux = aux.next
            counter+=1
              
        #We get first and last node from the list to introduce
        inputListFirst = inputList._head
        inputListLast = None
        aux2=inputList._head
        while aux2.next!=None:
            aux2 = aux2.next
        inputListLast= aux2
        #We change the pointers
        #if start=0
        if start==0:
            self._head=inputListFirst
            if end != self.__len__()-1:
                inputListLast.next = endNode
        #when it is in the middle
        else:
            startNode.next = inputListFirst
            if end != self.__len__()-1:
                inputListLast.next = endNode
        #Updating sizes
       
        self._size = self._size - (end -start +1) + inputList.__len__()

        print(self._size)
        print(self)


    def reverseK(self,k):
        #We have done this without additional data structures. In order to archive the objective, we loop the list in splits base on the number
        #of elements per split. In each iteration we reverse each split joining it with the last split reversed (if exists). We also take into #account the case in which the last split has a different lenght than "k".
        #-----------

        #Reasining k in case it is to big
        if(k>self.__len__()):
            k=self.__len__()
        #Checking splitting is possible
        if(k<0):
            print("the split range is not valid")
            return
        #Cheking if no need to reverse
        if(k==1 or k==0):
            print(self)
            return
        lastSplit=False
        #In case the splits are not exact, we calculate the length of last split
        reminder=int(self._size-(math.floor(self._size/k)*k))
        #calculate the number of splits
        splits = int(math.ceil((self._size/k)-1))
        currentSplit = 0
        #Save _head keeps track of the initial node of the reversed list
        saveHead = None
        #LastNodeProv keeps track of the last node of the last split
        lastNodeProv=None
        #Waiting keeps track of the first node of the next split
        waiting=None
        #We do one loop one for each split
        while splits >= currentSplit:
    #setting inital values
            aux = self._head
            #find provHead
            counter = 1
            #In case reminder equals one and we are on the last split
            if(reminder==1 and lastSplit==True):
                lastNodeProv.next=aux
                self._head=saveHead
                print(self)
                return
            #we will use [1,2,3,4,5,6,7,8] for ilustrating with k=4
            #Here we get the node before the end of the split Ex: [3]
            #provSize is a variable that keeps track of the split lenght
            if lastSplit==True and reminder!=0:
                provSize = reminder
                while counter+1!=reminder:
                    aux=aux.next
                    counter+=1
            else:
                provSize = k
                while counter+1 !=k:
                    aux=aux.next
                    counter+=1
            #Newhead contains the node that starts the reversing EX: [1,2,3,4] newhead will be 4
            newHead= aux.next
            
            #If we are in the first split, we save the _head for the end:
            if(currentSplit==0):
                saveHead = newHead
            #This contains the node that starts the next split
            #We check that we are not in the last split
            if(newHead.next!=None):
                #If we are not in the last split we save waiting (explained above) Ex: [5]
                waiting = newHead.next
            
            #Now we can cut and isolate the reminding nodes for the current split from newHead (we are isolating newHead) [1,2,3], [4]
            aux.next=None
            #As we do this we need to substract one from the provisional _size
            provSize=provSize-1
            #comming back to starting point because we need to start iterating.  [1,2,3] --> aux will be 1
            aux=self._head
            #We use a prev variable to keep track of the last node
            prev =self._head
            #Provisional _head is used in order to keep the last number that has been splitted Ex: provHead will be 4
            provHead = newHead
            while aux!=None:     
                #Once we reach the end of the split
                if(aux.next == None):
                    #we detach the node
                    prev.next=None
                    aux.next=None
                    #we attach the node to the provHead and move provHead Ex: after first iteration provHead will be 3
                    provHead.next=aux
                    provHead=provHead.next
                    #In case we are in the last node of the current split Ex:[1]
                    if(provSize==1):
                        #If we have already completed one split
                        if(lastNodeProv!=None):
                            #We join the last split with the _head of the new split
                            lastNodeProv.next =newHead
                        #If there are more splits comming
                        if(waiting!=None):
                            #We set the _head to the begenning of the next split  Ex: remember waiting was [5]
                            self._head=waiting
                        #We keep track of the last node of the current split for the next iteration Ex: [1]
                        lastNodeProv = aux
                        #Set aux to None to scape the loop
                        aux=None
                    else: 
                        #go back to the beggining of the split to keep iterating
                        prev=self._head
                        aux=self._head
                    provSize=provSize-1
                    continue
                #keep looping until reaching the end of the split
                prev=aux
                aux=aux.next
            #checks if we are in the last split
            currentSplit+=1     
            if(currentSplit==splits):
                lastSplit=True

        self._head = saveHead
        print(self)
        
    def maximumPair(self):
        if (self.isEmpty() == True):
            print("List is empty")
            return
        if(self.__len__()==1):
            print(self._head.elem)
            return (self._head.elem)
        #keep track of the left value index we need to add
        initialIndex = 0
        #keep track of the right value index we need to add
        endIndex = self.__len__()-1
        #Biggest sum made (this is the one that will be returned)
        currentSum = 0
        aux = self._head
        #Keeps track of the element in which we are in
        currentIndex = 0
        leftValue=None
        rightValue=None
        while endIndex>=initialIndex:
            #If the indexes are the same, we save the value
            if (currentIndex==initialIndex):
                leftValue = aux.elem
            if(currentIndex== endIndex):
                rightValue = aux.elem
            #Once both values are fill, we enter this if
            if(leftValue!=None and rightValue!=None):
                #This is in case the array has an odd number of elements
                if(initialIndex==endIndex):
                    provCurrentSum=rightValue
                else:
                    provCurrentSum =leftValue + rightValue
                #We only increase the value if the new sum is bigger than the last one
                if provCurrentSum>currentSum:
                    currentSum = provCurrentSum   
                #Change the index of the  next values we need to add up     
                initialIndex +=1
                endIndex -=1
                #We go back to _head
                aux = self._head
                #restoringValues
                leftValue=None
                rightValue=None
                currentIndex=0
                continue
            currentIndex +=1
            aux=aux.next
        print(currentSum)
        return currentSum