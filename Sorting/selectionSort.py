"""------------Selection Sorting-----------------

Attributes::
  un_Sorted_list (list) :: it is initial declaration .In this we will store the input string.
  sorted_list (list)   ::  it is also initial declaration but in this after all the process
  elements will be stored in sorted manner

Todo::
    Using more sorting algorithm we have to create package with folder of all the module

"""


def selection_sort(un_sorted_list):
    """This is the main algorithm of module .
    It  will be called by module when we import
    and it will be called by main when we run the code as a normal


    Args:
        an unsorted list data type [list]
    Return:
        A printed sorted list
    """

    length = len(un_sorted_list)
    if length == 0:
        print("Empty List")
        # If length is 0 then return and Empty string
        return
    for i in range(0, length-1):
        for j in range(i+1, length):
            if un_sorted_list[j] < un_sorted_list[i]:
                un_sorted_list[i], un_sorted_list[j] = un_sorted_list[j], un_sorted_list[i]

    return un_sorted_list


if __name__ == '__main__':
    """It will be called when it will not be imported as module"""
    print("Enter element with whitespace:: ")
    un_sorted_list1 = list(map(int, input().split()))
    print("Unsorted List is : ", un_sorted_list1)
    selection_sort(un_sorted_list1)
