"""My quick sort."""
import timeit
from random import randint


def quick_sort(input_list):
    """Quick sort."""
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
    """Quick sort helper."""
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

if __name__ == '__main__':  # pragma: no cover
    ordered_list = [num for num in range(10)]
    t_s = timeit.timeit('quick_sort(ordered_list) ', setup='from __main__ import quick_sort, ordered_list')
    print('BestCase:\n       sorting time: ' + str(t_s) + ' seconds')

    reversed_list = ordered_list[::-1]
    t_s = timeit.timeit('quick_sort(reversed_list) ', setup='from __main__ import quick_sort, reversed_list')
    print('WroseCase:\n      sorting time: ' + str(t_s) + ' seconds')

    vals = [randint(0, 1000) for _ in range(10)]
    t_s = timeit.timeit('quick_sort(vals) ', setup='from __main__ import quick_sort, vals')
    print('RandomCase:\n     sorting time: ' + str(t_s) + ' seconds')
