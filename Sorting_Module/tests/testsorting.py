import unittest
from Sorting_Module.sorting import Sort


class TestArray(unittest.TestCase):
    """
    This class contains all the test cases for sorting module in the terms of list elements, length of list etc.
    """

    def setUp(self):
        # Defining required variables
        self.arr = Sort([65, 23, 24, 12, 45])
        self.ContainingString = Sort([23, 43, 'string', 34, 1])
        self.ContainingIntegers = Sort([4, 9, -8, 7, -12, 0, 3])
        self.singleElement = Sort([6])
        self.sameNumbers = Sort([4, 4, 4, 4, 4, 4])

    # When list is empty
    def test_listEmpty(self):
        input = []
        self.assertTrue(not input)

    # check if list is containing any string
    def test_listContainsString(self):
        self.assertRaises(TypeError, self.ContainingString.selection)

    # check if list contains single element

    def test_singleElementinArray(self):
        self.assertTrue(len(self.singleElement.arr) == 1, msg="Single Element in array")

    # Check if all elements are same

    def test_allElementsSame(self):
        expected_output = [4, 4, 4, 4, 4, 4]
        self.assertTrue(self.sameNumbers.selection() == expected_output, msg="All list elements are same")

    # sorting if list contains signed and unsigned numbers

    def test_sorting_signedNumber(self):
        expected_output = [-12, -8, 0, 3, 4, 7, 9]
        self.assertEqual(self.ContainingIntegers.insertion(), expected_output)


if __name__ == '__main__':
    unittest.main()
