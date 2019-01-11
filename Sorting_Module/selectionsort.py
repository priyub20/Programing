"""

"""


class SelectionSort():
    """
    Selection sort is simple sorting method. It divides list in two different part, sorted and unsorted list. In every Iteration
    it searches minimum element in the unsorted sub-list,
    and move to the sorted list.

    """

    def selectionsort(self, arr):
        """

        :param arr: An unsorted array
        :return: Sorted Array
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
