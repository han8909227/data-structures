"""My merge sort."""
import timeit
from random import randint


def merge_sort(input_list):
    """Merge sort."""
    if not isinstance(input_list, (list, tuple)):
        raise ValueError('input takes list/tuple only')

    if isinstance(input_list, (tuple)):
        temp = []
        for val in input_list:
            temp.append(val)
        input_list = temp

    if not all(isinstance(val, (int, float)) for val in input_list):
        raise ValueError('all items in list must be a number')

    return _merge_sort(input_list)


def _merge_sort(input_list):
    """Helper."""
    if len(input_list) < 2:
        return input_list

    mid_idx = len(input_list) // 2
    left = merge_sort(input_list[:mid_idx])
    right = merge_sort(input_list[mid_idx:])

    return _merge(left, right)


def _merge(left, right):
    """Merger helper."""
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    while left:
        result.append(left[0])
        left = left[1:]
    while right:
        result.append(right[0])
        right = right[1:]
    return result

if __name__ == '__main__':  # pragma: no cover
    ordered_list = [num for num in range(10)]
    t_s = timeit.timeit('merge_sort(ordered_list) ', setup='from __main__ import merge_sort, ordered_list')
    print('BestCase:\n       sorting time: ' + str(t_s) + ' seconds')

    reversed_list = ordered_list[::-1]
    t_s = timeit.timeit('merge_sort(reversed_list) ', setup='from __main__ import merge_sort, reversed_list')
    print('WroseCase:\n      sorting time: ' + str(t_s) + ' seconds')

    vals = [randint(0, 1000) for _ in range(10)]
    t_s = timeit.timeit('merge_sort(vals) ', setup='from __main__ import merge_sort, vals')
    print('RandomCase:\n     sorting time: ' + str(t_s) + ' seconds')
