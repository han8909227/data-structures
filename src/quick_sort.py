"""My quick sort."""
import timeit
from random import randint


def quick_sort(input_list):
    """Quick sort."""
    if not isinstance(input_list, (list, tuple)):
        raise ValueError('input takes list/tuple only')

    if isinstance(input_list, (tuple)):
        input_list = list(input_list)

    if not all(isinstance(val, (int, float)) for val in input_list):
        raise ValueError('all items in list must be a number')
    quick_list = input_list[:]
    return _quicksort(quick_list)


def _quicksort(unsorted):
    """Quick sort helper."""
    if len(unsorted) == 1 or len(unsorted) == 0:
        return unsorted
    else:
        pivot = unsorted[0]
        swap_at = 0
        for idx in range(len(unsorted) - 1):
            if unsorted[idx + 1] < pivot:
                unsorted[idx + 1], unsorted[swap_at + 1] = unsorted[swap_at + 1], unsorted[idx + 1]
                swap_at += 1
        unsorted[0], unsorted[swap_at] = unsorted[swap_at], unsorted[0]
        left = _quicksort(unsorted[:swap_at])
        right = _quicksort(unsorted[swap_at + 1:])
        left.append(unsorted[swap_at])
        return left + right

if __name__ == '__main__':  # pragma: no cover
    ordered_list = [num for num in range(100)]
    t_s = timeit.timeit('quick_sort(ordered_list) ', setup='from __main__ import quick_sort, ordered_list')
    print('BestCase:\n       sorting time: ' + str(t_s) + ' seconds')

    reversed_list = ordered_list[::-1]
    t_s = timeit.timeit('quick_sort(reversed_list) ', setup='from __main__ import quick_sort, reversed_list')
    print('WroseCase:\n      sorting time: ' + str(t_s) + ' seconds')

    vals = [randint(0, 1000) for _ in range(100)]
    t_s = timeit.timeit('quick_sort(vals) ', setup='from __main__ import quick_sort, vals')
    print('RandomCase:\n     sorting time: ' + str(t_s) + ' seconds')
