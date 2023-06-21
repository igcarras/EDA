import random


def quicksort(arr):
    if len(arr) > 1:
        if len(arr) % 2 != 0:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            quicksort(L)
            quicksort(R)
            print("First pivot: ", arr[mid])
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] > R[j]:  # esta es la única diferencia con el  sort original que ordena de menor a mayor
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        else:
            mid = (len(arr) // 2) - 1
            L = arr[:mid + 1]
            R = arr[mid + 1:]
            quicksort(L)
            quicksort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] > R[j]:  # esta es la única diferencia con el  sort original que ordena de menor a mayor
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1


if __name__ == '__main__':
    a = []
    n = random.randint(1,7)
    for _ in range(n):
        a.append(random.randint(0,10))
    print("Before: ", a, end = "\n")
    #quicksort(a, 0, len(a)-1)
    quicksort(a)
    print("After: ", a)