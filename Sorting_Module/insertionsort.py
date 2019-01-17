"""
Insertion sort always maintains a sorted sublist in the lower positions of the list.
Each new item is then “inserted” back into the previous sublist such that the sorted sublist is one item larger.

"""


def insertionSort(arr):
    """
    :param arr: unsorted array
    :return: sorted array
    """
    # start from 0th index
    i = 0
    while i < len(arr):
        j = i
        # Compare two adjacent elements
        while j > 0 and arr[j - 1] > arr[j]:
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp
            j -= 1
        i += 1
    return arr
