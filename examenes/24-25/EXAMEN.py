# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


class SNode:
  def __init__(self,elem,next=None,prev=None ):
    self.elem = elem
    self.next = next
    
    
class SList:
    def __init__(self):
        """creates an empty list"""
        self._head=None
        self._tail=None
        self._size=0
    
    def __len__(self):
        return self._size
  
    def __str__(self):
        """Returns a string with the elements of the list"""
        ###This functions returns the same format used 
        ###by the Python lists, i.e, [], ['i'], ['a', 'b', 'c', 'd']
        ###[1], [3, 4, 5]
        nodeIt=self._head
        result='['
        while nodeIt:
            if type(nodeIt.elem)==int:
                result+= str(nodeIt.elem)+ ", "
            else:
                result+= "'"+str(nodeIt.elem)+ "', "
            nodeIt=nodeIt.next
        
        if len(result)>1:
            result=result[:-2]

        result+=']'
        return result

    def addLast(self,e):
        """Add a new element, e, at the end of the list"""
        #create the new node
        newNode=SNode(e)
        
        if self._head is None:
            self._head=newNode
            self._tail=newNode
        else:
            self._tail.next = newNode
            self._tail = newNode
        
        #increase the size of the list  
        self._size+=1


class DNode:
  def __init__(self,elem,next=None,prev=None ):
    self.elem = elem
    self.next = next
    self.prev = prev
    
    
class DList:
    def __init__(self):
        """creates an empty list"""
        self._head=None
        self._tail=None
        self._size=0
    
    def __len__(self):
        return self._size
  
    def __str__(self):
        """Returns a string with the elements of the list"""
        ###This functions returns the same format used 
        ###by the Python lists, i.e, [], ['i'], ['a', 'b', 'c', 'd']
        ###[1], [3, 4, 5]
        nodeIt=self._head
        result='['
        while nodeIt:
            if type(nodeIt.elem)==int:
                result+= str(nodeIt.elem)+ ", "
            else:
                result+= "'"+str(nodeIt.elem)+ "', "
            nodeIt=nodeIt.next
        
        if len(result)>1:
            result=result[:-2]

        result+=']'
        return result

    def addLast(self,e):
        """Add a new element, e, at the end of the list"""
        #create the new node
        newNode=DNode(e)
        
        if self._head is None:
            self._head=newNode
        else:
            newNode.prev=self._tail
            self._tail.next=newNode
        
        #update the reference of head to point the new node
        self._tail=newNode
        #increase the size of the list  
        self._size+=1
        

class SList2(SList):
    def completar(self):
        current = self._head
        es_impar = True
        curr_num = current.elem
        my_next = current.next
        while my_next:
            if my_next.elem != curr_num + 1:
                curr_num = curr_num + 1
                nuevo_nodo = SNode(curr_num)
                nuevo_nodo.next = current.next
                current.next = nuevo_nodo
                current = nuevo_nodo
                my_next = current.next
                self._size += 1
            else:
                current = my_next
                my_next = current.next
            
            curr_num = current.elem
            es_impar = not es_impar
        if es_impar:
            curr_num = curr_num + 1
            nuevo_nodo = DNode(curr_num)
            nuevo_nodo.next = current.next
            current.next = nuevo_nodo
            self._tail = nuevo_nodo
            self._size += 1

class DList2(DList):
    
    def rotar(self, p):
        if self._size > 1:
            while p > 0:
                p -= 1
                newNode=self._head 
                
                self._head= self._head.next
                self._head.prev = None
                    
                newNode.next = None
                newNode.prev=self._tail
                self._tail.next=newNode
                
                self._tail=newNode
            
 
import unittest

class Test(unittest.TestCase):

    def test1ej1(self):
        l=SList2()
        l.addLast(1)
        l.addLast(3)
        l.addLast(4)
        l.completar()
        self.assertEqual(str(l), "[1, 2, 3, 4]")


    def test2ej1(self):
        l=SList2()
        l.addLast(1)
        l.addLast(5)
        l.completar()
        self.assertEqual(str(l), "[1, 2, 3, 4, 5, 6]")

    def test3ej1(self):
        l=SList2()
        l.addLast(7)
        l.addLast(8)
        l.addLast(9)
        l.completar()
        self.assertEqual(str(l), "[7, 8, 9, 10]")

    def test4ej1(self):        
        l=SList2()
        l.addLast(2)
        l.addLast(4)
        l.addLast(6)
        l.completar()
        self.assertEqual(str(l), "[2, 3, 4, 5, 6, 7]")
    
    def test1ej2(self):
        l=DList2()
        l.rotar(5)
        self.assertEqual(str(l), "[]")


    def test2ej2(self):
        l=DList2()
        l.addLast(2)
        self.assertEqual(str(l), "[2]")
        l.rotar(5)
        self.assertEqual(str(l), "[2]")

    def test3ej2(self):
        l=DList2()
        l.addLast(2)
        l.addLast(4)
        l.addLast(5)
        self.assertEqual(str(l), "[2, 4, 5]")
        l.rotar(2)
        self.assertEqual(str(l), "[5, 2, 4]")

    def test4ej2(self):        
        l=DList2()
        l.addLast(2)
        l.addLast(4)
        l.addLast(5)
        l.addLast(6)
        self.assertEqual(str(l), "[2, 4, 5, 6]")
        l.rotar(1)
        self.assertEqual(str(l), "[4, 5, 6, 2]")
    
    def test5ej2(self):        
        l=DList2()
        l.addLast(2)
        l.addLast(4)
        l.addLast(5)
        l.addLast(6)
        self.assertEqual(str(l), "[2, 4, 5, 6]")
        l.rotar(12)
        self.assertEqual(str(l), "[2, 4, 5, 6]")
    

unittest.main()
