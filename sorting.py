#Sorting

def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    # the outter forloop, we want to repeat the same # of times as the len of our list. one forloop to
        # wrap the whole thing around.
    for j in range(len(lst)):
        # the inner forloop, we want to iterate through the whole list and stop one before the end
            # since there is no next to # to compare to.
        for i in range(len(lst)-1):
            if lst[i] > lst[i + 1]:
                # this is how you swap in python 
                lst[i],lst[i + 1] = lst[i + 1], lst[i]
    return lst            



def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """
    
    new_list = []
    while list1 != [] or list2 != []:
        # test if either one of these lists are empty, continue with the other.
        if list1 == []:
            new_list.append(list2[0])
            list2.pop(0)
        elif list2 == []:
            new_list.append(list1[0])
            list1.pop(0)


        # if none of the lists are empty then compare the first, pop it and append to new_list.
        elif list1[0] < list2[0]:
            new_list.append(list1[0])
            list1.pop(0)
        else:
            new_list.append(list2[0])
            list2.pop(0)
    return new_list



##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    if len(lst) < 2:
        return lst
    
    mid = int(len(lst) / 2)
    left = lst[:mid]
    right = lst[mid:]
    # when you have to do something over again and you're using recursion, call the funct.
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    # funct. call to merge two sorted lists
    new_list = merge_lists(sorted_left, sorted_right)
    return new_list




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print