import unittest
from Sorting.SortModule import CallSort


class TestCalling(unittest.TestCase):
    """Testing Module

    --------Unit Testing on class CallSort-----"""

    def test_selection_sort(self):
        """Selection Sort Testing for a list and empty list"""
        list1 = [1, 2, 3, 2, 5]
        CallSort(list1).selection_sort()
        result = list1
        self.assertEqual(result, [1, 2, 2, 3, 5])
        list2 = []
        CallSort(list1).selection_sort()
        result = list2
        self.assertEqual(result, [])

    def test_insert_sort(self):
        """Insertion Sort Testing for a list and empty list"""
        list1 = [1, 2, 3, 2, 5]
        CallSort(list1).insert_sort()
        result = list1
        self.assertEqual(result, [1, 2, 2, 3, 5])
        list2 = []
        CallSort(list1).insert_sort()
        result = list2
        self.assertEqual(result, [])

    def test_merge_sort(self):
        """Merge Sort Testing for a list and empty list"""
        list1 = [1, 2, 3, 2, 5]
        CallSort(list1).merge_sort()
        result = list1
        self.assertEqual(result, [1, 2, 2, 3, 5])
        list2 = []
        CallSort(list1).merge_sort()
        result = list2
        self.assertEqual(result, [])

    def test_quick_sort(self):
        """Quick Sort Testing for a list and empty list"""
        list1 = [1, 2, 3, 2, 5]
        CallSort(list1).quick_sort()
        result = list1
        self.assertEqual(result, [1, 2, 2, 3, 5])
        list2 = []
        CallSort(list1).quick_sort()
        result = list2
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
