def quicksort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)
        # Recursively sort the elements before and after partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def partition(arr, low, high):
    # Pivot is the first element
    pivot = arr[low]
    left = low + 1
    right = high

    done = False
    while not done:
        # Move the left pointer to the right until an element larger than the pivot is found
        while left <= right and arr[left] <= pivot:
            left += 1
        # Move the right pointer to the left until an element smaller than the pivot is found
        while arr[right] >= pivot and right >= left:
            right -= 1
        # If there is an element on the left that is greater than the pivot
        # and an element on the right that is smaller than the pivot, swap them
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # Swap the pivot with the right pointer
    arr[low], arr[right] = arr[right], arr[low]

    return right


# Example usage
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    print(arr)
    quicksort(arr, 0, n - 1)
    print("Array ordenado:", arr)

# Example usage
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    print(arr)
    quicksort(arr, 0, n - 1)
    print("Array ordenado:", arr)