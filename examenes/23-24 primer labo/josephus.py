from queue_slist import Queue,SNode
from random import randrange

def josephus_two_groups(n1, n2, k1, k2)->[]:
    queue1 = Queue()
    queue2 = Queue()
    for i in range(0, n1):
        queue1.enqueue('q1-' + str(i))
    for i in range(0, n2):
        queue2.enqueue('q2-' + str(i))

    eliminated_persons = []

    while len(queue1) > 1:
        for _ in range(k1 - 1):
            queue1.enqueue(queue1.dequeue())
        eliminated_persons.append(queue1.dequeue())
    while len(queue2) > 1:
        for _ in range(k2 - 1):
            queue2.enqueue(queue2.dequeue())
        eliminated_persons.append(queue2.dequeue())



    print("sobrevive en q1", queue1.front(),"sobrevive en q2", queue2.front())

    return eliminated_persons

def contest(n, k):
    queue1 = Queue()
    queue2 = Queue()
    for i in range(0, n):
        queue1.enqueue(i+randrange(10))
    for i in range(0, n):
        queue2.enqueue(i+randrange(10))


    count=1
    while len(queue1) > 1:
        while count < k:
            queue1.enqueue(queue1.dequeue())
            count = count + 1
        queue1.dequeue()

    count=1
    while len(queue2) > 1:
        while count < k:
            queue2.enqueue(queue2.dequeue())
            count = count + 1
        queue2.dequeue()

    print("queda en q1", queue1.front(),"queda en q2", queue2.front())


    return max(queue1.front(), queue2.front())

if __name__ == '__main__':
    # Ejemplo de uso
    n1 = 5  # Número total de personas en el primer grupo
    n2 = 7  # Número total de personas en el segundo grupo
    k1 = 2  # El paso de eliminación para el primer grupo
    k2 = 3  # El paso de eliminación para el segundo grupo
    #personas_eliminadas = josephus_two_groups(n1, n2, k1, k2)
    #print("Personas eliminadas en orden:", personas_eliminadas)

    print("premio ganador: ", contest(8,3))
