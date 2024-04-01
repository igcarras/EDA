from random import randrange
from prize  import Award,Prizes

def contest(prize1, prize2, k):

    while len(prize1) > 1:
        count = 1
        while count < k:
            prize1.add(prize1.remove())
            count = count + 1
        prize1.remove()


    while len(prize2) > 1:
        count = 1
        while count < k:
            prize2.add(prize2.remove())
            count = count + 1
        prize2.remove()

    winner1 = prize1.remove()
    winner2 = prize2.remove()
    return max(winner1, winner2)

if __name__ == '__main__':

    queue1 = Prizes()
    queue2 = Prizes()
    n=20
    for i in range(1, n+randrange(10)):
        queue1.add(i + randrange(100))
    for i in range(1, n+randrange(10)):
        queue2.add(i + randrange(100))

    print("premio ganador: ", contest(queue1, queue2, 3))
