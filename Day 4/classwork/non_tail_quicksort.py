from typing import List

def quicksort_iterative(arr: List[int]) -> None:
    p, r = 0, len(arr) - 1

    while p < r:
        pivot_index = (p + r) // 2
        pivot = arr[pivot_index]

        left, right = p, r
        while left <= right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        if right - p < r - left:
            if p < right:
                quicksort_iterative_sub(arr, p, right)
            p = left
        else:
            if left < r:
                quicksort_iterative_sub(arr, left, r)
            r = right


def quicksort_iterative_sub(arr: List[int], p: int, r: int) -> None:
    while p < r:
        pivot_index = (p + r) // 2
        pivot = arr[pivot_index]

        left, right = p, r
        while left <= right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        if right - p < r - left:
            if p < right:
                quicksort_iterative_sub(arr, p, right)
            p = left
        else:
            if left < r:
                quicksort_iterative_sub(arr, left, r)
            r = right


def main():
    arr = [10, 7, 8, 9, 1, 5]
    print("Original:", arr)
    quicksort_iterative(arr)
    print("Sorted:", arr)


if __name__ == "__main__":
    main()
