"""My quick sort."""
import timeit
from random import randint


def quick_sort(input_list):
    """quick sort."""
    if not isinstance(input_list, (list, tuple)):
        raise ValueError('input takes list/tuple only')

    if isinstance(input_list, (tuple)):
        temp = []
        for val in input_list:
            temp.append(val)
        input_list = temp

    if not all(isinstance(val, (int, float)) for val in input_list):
        raise ValueError('all items in list must be a number')
    return _quicksort(input_list)


def _quicksort(unsorted):
    if len(unsorted) == 1 or len(unsorted) == 0:
        return unsorted
    else:
        pivot = unsorted[0]
        i = 0
        for j in range(len(unsorted) - 1):
            if unsorted[j + 1] < pivot:
                unsorted[j + 1], unsorted[i + 1] = unsorted[i + 1], unsorted[j + 1]
                i += 1
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        left = _quicksort(unsorted[:i])
        right = _quicksort(unsorted[i + 1:])
        left.append(unsorted[i])
        return left + right

