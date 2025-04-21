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
        while current and current.next:
            if current.elem + 1 < current.next.elem:
                new_node = SNode(current.elem + 1)
                new_node.next = current.next
                current.next = new_node
                self._size += 1  # Actualizar tamaño de la lista
            else:
                current = current.next  # Avanzar al siguiente nodo
        # Si el número de nodos es impar, añadir un nodo extra al final
        if self._size % 2 == 1:
            extra_node = SNode(self._tail.elem + 1)
            self._tail.next = extra_node
            self._tail = extra_node
            self._size += 1  # Actualizar tamaño

class DList2(DList):

    def rotar(self, p):
        if self._size <= 1 or p <= 0 or p >= self._size:
            return  # No es necesario girar

            # Encontrar el nuevo head después de girar
        current = self._head
        for _ in range(p - 1):
            current = current.next

        new_head = current.next
        new_tail = current

        # Actualizar la nueva cabeza y cola
        new_head.prev = None
        new_tail.next = None

        self._tail.next = self._head
        self._head.prev = self._tail

        self._head = new_head
        self._tail = new_tail
            
 
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
