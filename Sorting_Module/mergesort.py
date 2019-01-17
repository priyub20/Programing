"""
 A merge sort works as follows :
 1. Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).
 2. Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist  remaining.

 """


def merge(arr: list) -> object:
    """
    :param arr: unsorted list
    :return: sorted list
    """
    if len(arr) > 1:
        # Divide list in two different list
        mid = len(arr) // 2
        # copy first half in left
        left = arr[:mid]
        # copy second half in right
        right = arr[mid:]
        merge(left)
        merge(right)
        # compare left with right
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k = k + 1
        # copy remaining left side elements in arr
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1
        # copy remaining right side elements in arr
        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1

    return arr
