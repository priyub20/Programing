"""
This class sorts an array using selection sort method with O(n^2) complexity. Selection sort is simple sorting method.
The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist,
exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order),
and moving the sublist boundaries one element to the right.

TODO:
    adding logging function
"""


def selectionsort(arr: list):
    """
    :param arr: contains an unsorted list
    :return list: Returns sorted list

    """
    for i in range(0, len(arr) - 1):
        temp = arr[i]
        # scan all the list to find minimum value for ith position
        for j in range(i, len(arr)):
            # find minimum value and replace it with temp
            if temp > arr[j]:
                arr[i] = arr[j]
                arr[j] = temp
                temp = arr[i]
    return arr
