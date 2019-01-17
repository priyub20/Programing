"""
This class functions calls the all sorting methods defined in Sorting_Modules.

Example:
    To run this file, navigate to Sorting_Module and run following command
    $ python sorting.py


TODO:
    Implementing factory method.
    Adding logging method

"""

from Sorting_Module.insertionsort import insertionSort
from Sorting_Module.mergesort import merge
from Sorting_Module.quicksort import quick_sort
from Sorting_Module.selectionsort import selectionsort
from Sorting_Module.utils import measureTime


class Sort:

    def __init__(self, arr: list):
        self.arr = arr

    def printArray(self):
        print(self.arr)

    @measureTime
    def quicksort(self):
        return quick_sort(self.arr)

    @measureTime
    def mergesort(self):
        return merge(self.arr)

    @measureTime
    def insertion(self):
        return insertionSort(self.arr)

    @measureTime
    def selection(self):
        return selectionsort(self.arr)


if __name__ == "__main__":
     # arr = Sort(list(map(int, input("Enter list\n").split())))
     arr = Sort([4, 9, -8, 7, -12, 0 , 3])
     # arr.printArray()
     print(arr.quicksort())
     print(arr.selection())
     print(arr.insertion())
     print(arr.mergesort())
