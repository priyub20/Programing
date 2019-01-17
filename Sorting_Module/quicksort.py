"""
Quicksort is based on Divide and Conquer method to sort elements. Quicksort uses pivot value to sort an array.
Position of pivot value decide in such a way that left side element of pivot should be less than pivot value and
right side element should be greater than pivot value.

TODO:
    adding logging function
"""


def quick_sort(arr, low: object = 0, high: object = None) -> object:
    """

    :param arr: Unsorted array
    :param low: initial index
    :param high: last index
    :return: sorted array
    """

    # Decide value for high
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    return arr


def partition(arr, low, high):
    """
    :param arr: unsorted array
    :param low: initial index of array
    :param high: last index of an array
    :return: index of pivot value
    """
    # we are deciding value of pivot based on first index
    pivot = arr[low]
    left = low + 1
    right = high
    flag = True
    while flag:
        # compare left side element
        while left <= right and arr[left] <= pivot:
            left = left + 1
        # compare right side element
        while arr[right] >= pivot and right >= left:
            right = right - 1
        # once right index crosses left, break the loop
        if left > right:
            flag = False
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
    # Move pivot value at it's desired location
    temp = arr[low]
    arr[low] = arr[right]
    arr[right] = temp
    # Return Index of Pivot value
    return right
