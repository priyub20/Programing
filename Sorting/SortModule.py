""""---------Calling Module----------------

Actually it calls for every module stored in  a package and
return the list accordingly
How to call class
1. from Sorting.SortModule import CallSort
2. list1 = [1, 4, 3, 2, 6, 9]
3. object1 = CallSort(list1)
4. object1.selection_sort()

"""
import selectionSort
import mergeSort
import insertionSort
import quickSort
import time


def timeit(sorting_function):
    """------------Decorator Function-------------

    It will call the sorting module to be calculated execution time of module

    Args:
        1.Sorting Function name
    Return:
        1.timed function
    """

    def timed(unsorted_list):
        """It will calculate time differences between start time of function execution and
        end time of function execution

        Args:
            1.Unsorted List
        Return:
            1.Sorted List
        """
        start_time = time.perf_counter()
        result = sorting_function(unsorted_list)
        end_time = time.perf_counter()
        print('Module Name :::  %r    taking  %f sec' % (sorting_function.__name__, end_time-start_time))
        return result

    return timed


class CallSort:
    def __init__(self, unsorted_list2):
        self.list1 = unsorted_list2

    @timeit
    def selection_sort(self):
        """This module will be called for Selection Sorting
        Args:
            1.Unsorted List
        Return:
            1.Sorted List
        """
        sorted_list = selectionSort.selection_sort(self.list1)
        return sorted_list

    @timeit
    def insert_sort(self):
        """This module will be called for Insertion Sorting
            Args:
                1.Unsorted List
            Return:
                1.Sorted List
        """
        sorted_list = insertionSort.insert_sort(self.list1)
        return sorted_list

    @timeit
    def merge_sort(self):
        """This module will be called for Merge Sorting
            Args:
                1.Unsorted List
            Return:
                1.Sorted List
        """
        sorted_list = mergeSort.merge_sort(self.list1)
        return sorted_list

    @timeit
    def quick_sort(self):
        """This module will be called for quick Sorting
            Args:
                1.Unsorted List
            Return:
                1.Sorted List
        """
        sorted_list = quickSort.quick_sort(self.list1)
        return sorted_list


if __name__ == '__main__':
    unsorted_list1 = [1, 3, 2, 4, 7, 9]
    obj = CallSort(unsorted_list1)
    sorted_list1 = obj.selection_sort()
    print(sorted_list1)
