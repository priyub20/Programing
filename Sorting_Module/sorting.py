from Sorting_Module.quicksort import QuickSort
from Sorting_Module.mergesort import MergeSort
from Sorting_Module.insertionsort import InsertionSort
from Sorting_Module.selectionsort import SelectionSort


class Sort:
    arr = []
    def __init__(self, arr: object) -> object:
        self.arr = arr

    def printArray(self) -> object:
        print(self.arr)

    def quicksort(self):
        quick = QuickSort()
        return quick.quick_sort(self.arr)

    def mergesort(self):
        merge = MergeSort()
        return merge.merge(self.arr)

    def insertion(self):
        insert = InsertionSort()
        return insert.insertionSort(self.arr)

    def selection(self):
        select = SelectionSort()
        return select.selectionsort(self.arr)
