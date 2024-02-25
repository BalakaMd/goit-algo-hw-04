import timeit
import random


def merge_sort(arr):
    """
    Perform a merge sort on the input array.

    Parameters:
    arr (list): The input list to be sorted.

    Returns:
    list: The sorted list.
    """

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    """
    Merge two sorted arrays into a single sorted array.

    Parameters:
    - left: a list representing the left sorted array
    - right: a list representing the right sorted array

    Returns:
    - merged: a list representing the merged sorted array
    """
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def compare_sorting_algorithms():
    """
    Compare the performance of different sorting algorithms on arrays of various sizes.
    """
    # Array sizes to test
    sizes = [10 ** 3, 10 ** 4, 10 ** 5]
    for size in sizes:
        # Generate random array of the given size
        arr = [random.randint(0, size) for _ in range(size)]

        # Measure the time taken for merge sort, insertion sort, and timsort on the array
        merge_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=10)
        insertion_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=10)

        # Timsort is already implemented in Python as the default sorting algorithm
        timsort_time = timeit.timeit(lambda: arr.sort(), number=10)

        # Print the results for each sorting algorithm
        print(f"Array size: {size}")
        print(f"Merge sort time: {round(merge_time, 4)}")
        print(f"Insertion sort time: {round(insertion_time, 4)}")
        print(f"Timsort time: {round(timsort_time, 4)}")
        print("------------------------------")


compare_sorting_algorithms()
