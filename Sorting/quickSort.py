"""------------Quick Sorting--------------------

Attributes::
  un_Sorted_List (list) :: it is initial declaration .In this we will store the input string.
  sorted_List (list)   ::  it is also initial declaration but in this after all the process
  elements will be stored in sorted manner

Todo::
    Using more sorting algorithm we have to create package with folder of all the module

"""


def quick_sort(un_sorted):
    """This function is calling the main algorithm to be applied on the list and it is passing
    the list arguments to algorithm

     Args:
        an unsorted list data type [list]
    Return:
        A printed sorted list"""
    length = len(un_sorted)
    if length == 0:
        print("Empty List")
        return
    quick(un_sorted, 0, length-1)
    return un_sorted


def partition(un_sorted, low, high):
    """It will return the partitioning
    index from where we have to divide
    the list"""
    p_index = low
    # Pivot is the last element of the list
    pivot = un_sorted[high]
    for i in range(low, high):
        if un_sorted[i] <= pivot:
            """Swapping with pivot
                       to make all smaller than pivot   in 
                       left side of pivot and bigger in right
               side of pivot
            """
            un_sorted[p_index], un_sorted[i] = un_sorted[i], un_sorted[p_index]
            p_index = p_index + 1

    """This is swapping to place pivot element on its
        place in order to make sublist/list sorted"""
    un_sorted[p_index], un_sorted[high] = un_sorted[high], un_sorted[p_index]
    return p_index


def quick(un_sorted, low, high):
    if low < high:
        p_index = partition(un_sorted, low, high)
        quick(un_sorted, low, p_index - 1)
        quick(un_sorted, p_index+1, high)


if __name__ == '__main__':
    """It will be called when it will not be imported as module"""
    print("Enter element with whitespace:: ")
    un_sorted_list1 = list(map(int, input().split()))
    print("Unsorted List is : ", un_sorted_list1)
    quick_sort(un_sorted_list1)
