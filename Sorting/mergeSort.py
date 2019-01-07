"""------------Quick Sorting--------------------

Attributes::
  un_Sorted_List (list) :: it is initial declaration .In this we will store the input string.
  sorted_List (list)   ::  it is also initial declaration but in this after all the process
  elements will be stored in sorted manner

Todo::
    Using more sorting algorithm we have to create package with folder of all the module

"""


def merge_sort(un_sorted_list):
    """This function is calling the main algorithm to be applied on the list and it is passing
        the list arguments to algorithm.
         Args:
            an unsorted list data type [list]
        Return:
            A printed sorted list"""
    length = len(un_sorted_list)
    if length == 0:
        print("Empty List")
        return
    merge_sort_algorithm(un_sorted_list, 0, length)
    return un_sorted_list


def merge(un_sorted, l, m, r):
    """Sublist
    Args:
        1. un_sorted_list
        2. low index
        3. middle index
    Return:
        a sorted merged list
        """
    list1 = un_sorted[l:m]
    # First half sublist
    list2 = un_sorted[m:r]
    # Index of merged sort list
    k = l
    # index of left sub list
    i = 0
    # index of right sub list
    j = 0
    # If there is elements in both the sublist
    while l + i < m and m + j < r:
        if list1[i] <= list2[j]:
            un_sorted[k] = list1[i]
            i = i + 1
        else:
            un_sorted[k] = list2[j]
            j = j + 1
        k = k + 1
    """If Elements are left in only left sublist or right sublist"""
    if l + i < m:
        while k < r:
            un_sorted[k] = list1[i]
            i = i + 1
            k = k + 1

    else:
        while k < r:
            un_sorted[k] = list2[j]
            j = j + 1
            k = k + 1


def merge_sort_algorithm(un_sorted, l, r):
    """It is dividing the list in two equal part
    Args:
        1.un_sorted_list
        2.index of element from where list to be divided
        3.index of element till where list to be divided
    Return:
        Divided list
        """
    if r - l > 1:
        # calculating index of middle index
        m = (l + r) // 2
        merge_sort_algorithm(un_sorted, l, m)
        merge_sort_algorithm(un_sorted, m, r)
        merge(un_sorted, l, m, r)


if __name__ == '__main__':
    print("Enter element with whitespace")
    un_sorted_list1 = list(map(int, input().split()))
    print("Unsorted List:: ")
    merge_sort(un_sorted_list1)
