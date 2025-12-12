from typing import List

def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left  = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + equal + quicksort(right)


def main():
    arr = [10, 7, 8, 9, 1, 5]
    print("Original:", arr)
    sorted_arr = quicksort(arr)
    print("Sorted:", sorted_arr)


if __name__ == "__main__":
    main()
