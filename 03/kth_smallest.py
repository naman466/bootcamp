from typing import List
import random

def partition(arr: List[int], left: int, right: int) -> int:
    pivot_index = random.randint(left, right)
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    pivot = arr[right]

    i = left
    for j in range(left, right):
        if arr[j] > pivot:  # '>' for kth largest
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def quickselect(arr: List[int], left: int, right: int, k: int) -> int:
    if left == right:
        return arr[left]

    pivot_index = partition(arr, left, right)

    if pivot_index == k:
        return arr[pivot_index]
    elif pivot_index > k:
        return quickselect(arr, left, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, right, k)

def find_kth_largest(arr: List[int], k: int) -> int:
    return quickselect(arr, 0, len(arr) - 1, k - 1)

arr = [3, 2, 1, 5, 6, 4]
k = 2
print(f"{k}th largest:", find_kth_largest(arr, k))
