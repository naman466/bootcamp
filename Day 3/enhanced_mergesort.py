# Enhanced merge sort for counting inversions in O(nlogn) time 
from typing import List

def merge_and_count(arr: List[int]) -> int:
    if len(arr) <= 1:
        return 0
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    inv_left = merge_and_count(left)
    inv_right = merge_and_count(right)

    inv_split = merge(arr, left, right)

    return inv_left + inv_right + inv_split


def merge(arr: List[int], left: List[int], right: List[int]) -> int:
    i = j = k = 0
    inversions = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            inversions += (len(left) - i)
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return inversions


def main():
    arr = [5, 3, 2, 4, 1]
    print("Original array:", arr)
    inv_count = merge_and_count(arr)
    print("Sorted array:", arr)
    print("Total inversions:", inv_count)


if __name__ == "__main__":
    main()
