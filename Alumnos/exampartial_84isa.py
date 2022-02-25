
class SNode:
  def __init__(self, e, next=None):
    self.elem = e
    self.next = next
    
    
class SList2():
    
    def __init__(self):
        self._head=None
        self._tail=None
        
    def __str__(self):
        """Returns a string with the elements of the list"""
        nodeIt=self._head
        result='['
        while nodeIt:
            result+= str(nodeIt.elem)+ ", "
            nodeIt=nodeIt.next
        
        if len(result)>1:
            result=result[:-2]

        result+=']'
        return result
    
    def append(self,e):
        """Adds a new element, e, at the end of the list"""
        #create the new node
        newNode=SNode(e)
        #the last node must point to the new node
        #now, we must update the tail reference
        if self._head==None:
            self._head=newNode
        else:
            self._tail.next= newNode
        
        self._tail=newNode

    
        
    def isSorted(self):
        "returns True if self is sorted and does not have any duplicate"
        if self._head==None:
            return True
        else:
            node1=self._head
            node2=node1.next
            while node2:
                if node1.elem>=node2.elem:
                    return False
                node1=node2
                node2=node2.next
                
        return True
    
        
    """ funcion que modifica la lista invocante para que todos los elementos pares aparezcan antes que los elementos
    impares. La funcion debe respetar el orden de los elementos pares y el orden de los elementos impares
     pero no puede contener valores duplicados."""
    def segregateOddEven(self):

        #evens = SList2()
        #odds = SList2()
        node = self._head
        
        '''Isa: el problema que le veo a este problema es que ya está en la hoja de problemas.
        Si no admitimos duplicados la complejidad de la función aumenta a O(n2). 
        Quizá una variación del problema
        es decir que no pueden usar addLast (de hecho puedes darle una clase sin esos métodos y decir que no puedes incluir 
                                             otros métodos)
        E indicarles que sí pueden hacer es usar variables para 
        '''
        '''while node:
            e = node.elem
            if e % 2 == 0:
                if evens.index(e)==-1:
                    evens.addLast(e)
            else:
                if odds.index(e)==-1:
                    odds.addLast(e)

            node = node.next
        '''
        
        headEven=None #This node will save the first node of the  nodes containing an elem even
        headOdd= None #This node will save the first node of the  nodes containing an  elem odd
        
        prevEven=None
        prevOdd=None
        
        while node:
            e = node.elem
            if e % 2 == 0:
                if headEven==None:
                    headEven=node
                else:
                    prevEven.next=node
                prevEven=node
            else:
                if headOdd==None:
                    headOdd=node
                else:
                    prevOdd.next=node
                prevOdd=node

            node = node.next
        
        tailEven=prevEven
        if tailEven!=None:
            tailEven.next=None
        tailOdd=prevOdd
        if tailOdd!=None:
            tailOdd.next=None

        if headEven==None:
            self._head = headOdd
            self._tail = tailOdd
        elif headOdd==None:
            self._head = headEven
            self._tail = tailEven
        else:
            # print(headEven.elem,headOdd.elem)
            # print(tailEven.elem,tailOdd.elem)

            self._head = headEven
            prevEven.next=headOdd
            self._tail = tailOdd

    """ funcion merge que a la lista invocante otra lista que recibe por parametro.
    La lista resultante tiene que estar ordenada de menor a mayor y no admite duplicados
    Isa: La solución propuesta está bien. Si pides que ambas listas estén ordenadas como precondición, 
    entonces la complejidad de mezclarlas de forma ordenada puede bajar a lineal. De esta forma puedes distinguir e

    """
    def merge(self, other):
        
        if self.isSorted()==False or other.isSorted()==False:
            print('Error: both list must be sorted')
            return None
        
       
        
        listMerged = SList2()

        node1 = self._head
        node2 = other._head

        while node1 and node2:
            if node1.elem < node2.elem:
                listMerged.append(node1.elem)
                node1 = node1.next
            elif node2.elem < node1.elem:
                listMerged.append(node2.elem)
                node2 = node2.next
            else:
                # no duplicates allowed
                listMerged.append(node1.elem)
                node1 = node1.next
                node2 = node2.next

        # if the there are still elements in self (list)
        while node1:
            #no duplicates allowed
            listMerged.append(node1.elem)
            node1 = node1.next

            # if the there are still elements in other (list)
        while node2:
            # no duplicates allowed
            listMerged.append(node2.elem)
            node2 = node2.next

        return listMerged

import random
if __name__=='__main__':
       #Please, uncomment the code for test each function

        l2=SList2()
        print(l2)
        for i in range(10):
            l2.append(random.randint(0,20))
        print(l2)

        

        #print("before segregateOddEven:",l2.__str__())
        ##Isa: Las funciones __x__ son funciones mágicasque sobre escriben operadores: str, len, +, etc.
        ##puedes llamarlas como un oeprador. En el caso de str, incluso la puedes obviar, porque
        #al hacer un print, por defecto se llama al str del objeto
        print("before segregateOddEven:",str(l2))
        l2.segregateOddEven()
        #Isa: Por ejemplo, aquí no pongo str
        print("after segregateOddEven:",l2)
        print()
        
        #Isa: Test with a list of even elements 
        l2=SList2()
        for i in range(10):
            l2.append(i*2)
        print(l2)
        
        print("before segregateOddEven:",l2)
        l2.segregateOddEven()
        print("after segregateOddEven:",l2)
        print()
        
        #Isa: Test with a list of odd elements 
        l2=SList2()
        for i in range(1,10,2):
            l2.append(i)
        print(l2)
        
        print("before segregateOddEven:",l2)
        l2.segregateOddEven()
        print("after segregateOddEven:",l2)
        print()



        l3 = SList2()
        for i in range(10):
            l3.append(i)

        
        print('l2:', l2)
        print('l3:', l3)
        
        print("List merged:" , l2.merge(l3))
        print("List merged:" , l3.merge(l2))
        print()
        
        data=[]
        for i in range(5):
            x=random.randint(0,10)
            if x not in data:
                data.append(x)
            
        data.sort()
        l2=SList2()
        for x in data:
            l2.append(x)
            
        data=[]
        for i in range(7):
            x=random.randint(0,10)
            if x not in data:
                data.append(x)
            
        data.sort()
        l3=SList2()
        for x in data:
            l3.append(x)
            
            
            
        print('l2:', l2)
        print('l3:', l3)    
        print("List merged:" , l2.merge(l3))
        print("List merged:" , l3.merge(l2))
        
