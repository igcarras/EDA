# -*- coding: utf-8 -*-
"""P1-p2-Lega.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ic76_Egk1-sBcS5CRLTQVXAD0_ucKr6s
"""

from metodo_completar import SList2

import unittest
class Test(SList2):
  def move_duplicates_to_end(self):
        if self.is_empty():
            return

        current = self._head
        last_node = self._tail

        while current is not last_node.next:
            if current.next and current.elem == current.next.elem:
                duplicate = current.next
                successive = duplicate.next
                current.next = successive
                self._tail.next = duplicate
                self._tail = duplicate
                self._tail.next = None
            else:
                current = current.next

class Test(unittest.TestCase):
  def setUp(self):
    self.S1=SList2()
    self.S2s=SList2()
    self.S2e=SList2()
    self.S3s=SList2()
    self.S3e=SList2()
    self.S4s=SList2()
    self.S4e=SList2()
    self.S5s=SList2()
    self.S5e=SList2()

    L2s=[1,1,3,4,5]
    L2e=[1,3,4,5,1]
    for i in L2s:
        self.S2s.add_last(i)
    for i in L2e:
        self.S2e.add_last(i)

    L3s=[1,2,2,2,5]
    L3e=[1,2,5,2,2]
    for i in L3s:
        self.S3s.add_last(i)
    for i in L3e:
        self.S3e.add_last(i)

    L4s=[1,2]
    L4e=[1,2]
    for i in L4s:
        self.S4s.add_last(i)
    for i in L4e:
        self.S4e.add_last(i)

    L5s=[1,2,2,3,3]
    L5e=[1,2,3,2,3]
    for i in L5s:
        self.S5s.add_last(i)
    for i in L5e:
        self.S5e.add_last(i)

  def test1(self):
    OL=self.S1 #Original empty list
    self.S1.move_duplicates_to_end()
    print('Test 1: Empty list')
    print('\tOriginal list: ',OL)
    print('\tRemaining list: ',self.S1)
    self.assertEqual(OL._size,self.S1._size,'Size before and after in empty list is not the same')
    self.assertIsNone(self.S1._head,'Head in empty list is not None')
    self.assertIsNone(self.S1._tail,'Tail in empty list is not None')
    current1=OL._head
    current2=self.S1._head
    while current1:
      self.assertEqual(current1.elem,current2.elem,'Any elements in list before and after are not the same')
      current1=current1.next
      current2=current2.next

  def test2(self):
    print('Test 2:')
    print('\tOriginal list:', self.S2s)
    self.S2s.move_duplicates_to_end()
    print('\tExpected remaining list.',self.S2e)
    print('\tActual remaining list:',self.S2s)
    self.assertEqual(self.S2s._size,self.S2e._size,'Size before and after in empty list is not the same')
    self.assertEqual(self.S2s._head.elem,self.S2e._head.elem,'Head before and after in empty list is not the same')
    self.assertEqual(self.S2s._tail.elem,self.S2e._tail.elem,'Tail before and after in empty list is not the same')
    current1=self.S2s._head
    current2=self.S2e._head
    while current1:
      self.assertEqual(current1.elem,current2.elem,'Any elements in list before and after are not the same')
      current1=current1.next
      current2=current2.next

  def test3(self):
    print('Test 3:')
    print('\tOriginal list:', self.S3s)
    self.S3s.move_duplicates_to_end()
    print('\tExpected remaining list.',self.S3e)
    print('\tActual remaining list:',self.S3s)
    self.assertEqual(self.S3s._size,self.S3e._size,'Size before and after in empty list is not the same')
    self.assertEqual(self.S3s._head.elem,self.S3e._head.elem,'Head before and after in empty list is not the same')
    self.assertEqual(self.S3s._tail.elem,self.S3e._tail.elem,'Tail before and after in empty list is not the same')
    current1=self.S3s._head
    current2=self.S3e._head
    while current1:
      self.assertEqual(current1.elem,current2.elem,'Any elements in list before and after are not the same')
      current1=current1.next
      current2=current2.next

  def test4(self):
    print('Test 4:')
    print('\tOriginal list:', self.S4s)
    self.S4s.move_duplicates_to_end()
    print('\tExpected remaining list.',self.S4e)
    print('\tActual remaining list:',self.S4s)
    self.assertEqual(self.S4s._size,self.S4e._size,'Size before and after in empty list is not the same')
    self.assertEqual(self.S4s._head.elem,self.S4e._head.elem,'Head before and after in empty list is not the same')
    self.assertEqual(self.S4s._tail.elem,self.S4e._tail.elem,'Tail before and after in empty list is not the same')
    current1=self.S4s._head
    current2=self.S4e._head
    while current1:
      self.assertEqual(current1.elem,current2.elem,'Any elements in list before and after are not the same')
      current1=current1.next
      current2=current2.next

  def test5(self):
    print('Test 5:')
    print('\tOriginal list:', self.S5s)
    self.S5s.move_duplicates_to_end()
    print('\tExpected remaining list.',self.S5e)
    print('\tActual remaining list:',self.S5s)
    self.assertEqual(self.S5s._size,self.S5e._size,'Size before and after in empty list is not the same')
    self.assertEqual(self.S5s._head.elem,self.S5e._head.elem,'Head before and after in empty list is not the same')
    self.assertEqual(self.S5s._tail.elem,self.S5e._tail.elem,'Tail before and after in empty list is not the same')
    current1=self.S5s._head
    current2=self.S5e._head
    while current1:
      self.assertEqual(current1.elem,current2.elem,'Any elements in list before and after are not the same')
      current1=current1.next
      current2=current2.next


unittest.main(argv=['first-arg-is-ignored'], exit=False)