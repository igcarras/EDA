# -*- coding: utf-8 -*-
"""parcia1-81-2021.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QMyehshSw1j9MN8GcfixSIA12agHCx0I

# Primer examen parcial grupo 81
Problema: En la clase MyList, completa la función remove, que toma como argumento un elemento, e, y elimina la última ocurrencia de este elemento en la lista. La función debe devolver el índice de esta última ocurrencia. Si el elemento no existe en la lista entonces, la función devuelve -1 y la lista no es modificada.
"""

class DNode:
    def __init__(self,e,next=None, prev=None):
        self.elem=e
        self.next=next
        self.prev=prev

class MyList:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0

    def append(self,e):
        newNode=DNode(e)
        if self._head==None:
            self._head=newNode
        else:
            self._tail.next=newNode
            newNode.prev=self._tail
        self._tail=newNode
        self._size+=1

   
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
        #O(n)



    def removeAt(self,index):
        ...

    def deleteLast(self,e):
        index=self._size -1 # es el índice del último nodo
        node=self._tail
        found=False

        while node!=None and found==False:
            if node.elem==e:
                found=True
            else:
                node=node.prev
                index-=1

        if node==None:
            print(e, ' no existe en la lista')
            index=-1
        else:
            index=self.removeAt(index)

        return index





    def deleteLast1(self,e):
        """delete the last occurrence of e in the list and returns its index.
        If e does not exist, it returns -1
        
        Complejidad de la función, O(n)
        Mejor caso: Lista vacía, O(1). Si la lista no está vacía, e está en el último nodo O(1) 
        Peor caso: e no está en la lista, lista no vacía. O(n)"""

        
        index=self._size -1 # es el índice del último nodo
        node=self._tail
        found=False

        while node!=None and found==False:
            if node.elem==e:
                found=True
            else:
                node=node.prev
                index-=1


        #node el nodo que contiene a e
        if node==None:
            print(e, ' no existe en la lista')
            index=-1
        else:
            #node es el nodo a borrar
            if node==self._tail:
                self._tail=self._tail.prev
                if self._tail==None:
                    self._head=None
                else:
                    self._tail.next=None

            elif node==self._head:
                self._head=self._head.next
                self._head.prev=None
            else:
                #estoy borrando un nodo que no es un extremo
                
                node.prev.next=node.next
                node.next.prev=node.prev

            
            self._size-=1
   
        return index














    def deleteLast2(self,e):
        """delete the last occurrence of e in the list and returns its index.
        If e does not exist, it returns -1"""

        
        #Mejor caso: la lista está vacía O(1). Si e está en el último nodo, se
        #puede considerar también mejor caso, O(1)
        #Peor caso: O(n), e no existe en la lista, es necesario 
        #recorrer toda la lista.
        #Complejidad de la función: O(n), la complejidad depende del tamaño de
        #la lista. En el peor de los casos es necesario recorrer toda la lista.
        
        found=False
        index=self._size
        
        node=self._tail
        #this loop looks for e starting by the end of the list
        while node and found==False:
            index-=1
            if node.elem==e:
                found=True
            else:
                node=node.prev
        
        if found==False:
            index=-1
        else:
            #index is the last position of e
            #node is the node to remove
            if node==self._tail:            #index=self._size-1
                self._tail=self._tail.prev
                if self._tail==None:  #the list only had a node
                    self._head=None
                else:
                    self._tail.next=None
            elif node==self._head:          #index==0
                self._head=self._head.next
                self._head.prev=None
            else:  
                previous=node.prev
                nextNode=node.next
                previous.next=nextNode
                nextNode.prev=previous
            
            self._size-=1

        return index

mylist=MyList()
for c in ['a','z','a','r']:
    mylist.append(c)
print("Lista=",mylist)
print() 

for x in ['p','a','a','z','r','a']:
    print("mylist: ", mylist)
    print("mylist.deleteLast('{}')={}  -->    mylist={}".format(x,mylist.deleteLast(x),mylist))
    print()

import unittest #package that contains the classes t

class Test(unittest.TestCase):

    def setUp(self):
        """This functions is executed for each of the test functions"""
        self.lEmpty=MyList()

        self.l1=MyList()
        self.l1.append('a')
        
        self.l4=MyList()
        for c in ['a','z','a','r']:
            self.l4.append(c)
        



    def test1_remove(self):
        print('Case 1: deleteLast an element that does not exist')
        index=self.l4.deleteLast('b')

        expected=['a','z','a','r']
        
        self.assertEqual(index, -1, "Fail: Case 1: deleteLast an element that does not exist, index should be -1")

        #str(expected)=['a','z','a','r']
        self.assertEqual(str(self.l4), str(expected), "Fail: Case 1: deleteLast an element that does not exist")

        print('test1_remove was OK!!\n')

    def test2_remove(self):
        print('Case 2: deleteLast an element from an empty list')
        index=self.lEmpty.deleteLast('a')

        expected=[]
        self.assertEqual(index, -1, "Case 2: deleteLast an element from an empty list")

        self.assertEqual(str(self.lEmpty), str(expected), "Case 2: deleteLast an element from an empty list")

    def test3_remove(self):
        print('Case 3: deleteLast an element that is not at the beginning')
        #l4 a<->z<->a<->r
        index=self.l4.deleteLast('a')
        #l4 a<->z<->r  -> str(l4)=['a', 'z', 'r']
        
        expected=['a','z','r']
        self.assertEqual(index, 2, "Case 3: remove an element that is the first element")

        self.assertEqual(str(self.l4), str(expected), "Case 3: deleteLast an element that is the first element")

  

    def test4_remove(self):
        print('Case 4: deleteLast an element that is the last element')
        index=self.l4.deleteLast('r')

        expected=['a','z','a']
        self.assertEqual(index, 3, "Case 4: deleteLast an element that is the last element")
        self.assertEqual(str(self.l4), str(expected), "Case 4: deleteLast an element that is the last element")

    def test5_remove(self):
        print('Case 5: deleteLast an element that is in the middle of the list')
        index=self.l4.deleteLast('z')

        expected=['a','a','r']
        self.assertEqual(index, 1, "Case 5: deleteLast an element that is in the middle of the list")
        self.assertEqual(str(self.l4), str(expected), "Case 5: deleteLast an element that is in the middle of the list")

    def test6_remove(self):
        print('Case 6: deleteLast the only element of the list')
        index=self.l1.deleteLast('a')

        expected=[]
        self.assertEqual(index, 0, "Case 6: deleteLast the only element of the list")
        self.assertEqual(str(self.l1), str(expected), "Case 6: deleteLast the only element of the list")

#If you are using Spyder, please comment the following line: 
unittest.main(argv=['first-arg-is-ignored'], exit=False)

#To use Spyder, remove the following comments:
#if __name__ == '__main__':
#    unittest.main()