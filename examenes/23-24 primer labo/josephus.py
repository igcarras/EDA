from random import randrange
from prize  import Award,Prizes
import unittest

def contest(prize1, prize2, k):

    while prize1 != None and len(prize1) > 1:
        count = 1
        while count < k:
            prize1.add(prize1.remove())
            count = count + 1
        prize1.remove()


    while prize2 != None and len(prize2) > 1:
        count = 1
        while count < k:
            prize2.add(prize2.remove())
            count = count + 1
        prize2.remove()

    if prize1 != None and len(prize1) > 0:
        winner1 = prize1.remove()
    else:
        winner1 = 0
    if prize2 != None and len(prize2) > 0:
        winner2 = prize2.remove()
    else:
        winner2 = 0
    return max(winner1, winner2)


import unittest

class Test(unittest.TestCase):
  def setUp(self):
    self.S1a=Prizes()
    self.S1b=Prizes()

    self.S2a=Prizes()
    self.S2a.add(25)
    self.S2a.add(31)
    self.S2a.add(4)
    self.S2b=Prizes()

    self.S3a=Prizes()
    self.S3a.add(72)
    self.S3a.add(90)
    self.S3a.add(18)
    self.S3b=Prizes()
    self.S3b.add(31)
    self.S3b.add(64)
    self.S3b.add(75)
    self.S3b.add(64)
    self.S3b.add(34)
    self.S3b.add(50)
    self.S3b.add(64)
    self.S3b.add(70)
    self.S3b.add(93)

    self.S4a=Prizes()
    self.S4a.add(97)
    self.S4a.add(96)
    self.S4a.add(38)
    self.S4a.add(101)
    self.S4a.add(30)
    self.S4a.add(85)
    self.S4b=Prizes()
    self.S4b.add(60)
    self.S4b.add(3)
    self.S4b.add(93)
    self.S4b.add(6)
    self.S4b.add(24)
    self.S4b.add(19)
    self.S4b.add(61)
    self.S4b.add(14)
    self.S4b.add(51)
    self.S4b.add(86)

  def test0(self):
    print('Test 0: None lists')
    S0a = None
    S0b = None
    print("L1: ", S0a)
    print("L2: ", S0b)
    k=1
    print("k: ", k)
    self.assertEqual(contest(S0a, S0b, k), 0)

  def test1(self):
    print('Test 1: Empty list')
    print("L1: ", self.S1a)
    print("L2: ", self.S1b)
    k=4
    print("k: ", k)
    winner = contest(self.S1a, self.S1b, k)
    print("premio ganador: ", winner)
    self.assertEqual(winner, 0)

  def test2(self):
    print('Test 2: one empty list')
    print("L1: ", self.S2a)
    print("L2: ", self.S2b)
    k=4
    print("k: ", k)
    winner = contest(self.S2a, self.S2b, k)
    print("premio ganador: ", winner)
    self.assertEqual(winner, 31)

  def test3(self):
    print('Test 3: long and short list')
    print("L1: ", self.S3a)
    print("L2: ", self.S3b)
    k=3
    print("k: ", k)
    self.assertEqual(contest(self.S3a, self.S3b, k), 90)

  def test4(self):
    print('Test 4: long lists')
    print("L1: ", self.S4a)
    print("L2: ", self.S4b)
    k=2
    print("k: ", k)
    self.assertEqual(contest(self.S4a, self.S4b, k), 30)

unittest.main(argv=['first-arg-is-ignored'], exit=False)

