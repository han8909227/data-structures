"""My Insertion sort."""
import timeit
from random import randint


def insertion_sort(input_list):
    """Insertion sort."""
    if not isinstance(input_list, (list, tuple)):
        raise ValueError('input takes list/tuple only')

    if isinstance(input_list, (tuple)):
        input_list = list(input_list)

    if not all(isinstance(val, (int, float)) for val in input_list):
        raise ValueError('all items in list must be a number')

    insertion_list = input_list[:]
    for index in range(1, len(insertion_list)):
        curr = insertion_list[index]
        pos = index

        while pos > 0 and insertion_list[pos - 1] > curr:
            insertion_list[pos] = insertion_list[pos - 1]
            pos -= 1
        insertion_list[pos] = curr
    return insertion_list


if __name__ == '__main__':  # pragma: no cover
    ordered_list = [num for num in range(10)]
    t_s = timeit.timeit('insertion_sort(ordered_list) ', setup='from __main__ import insertion_sort, ordered_list')
    print('BestCase:\n       sorting time: ' + str(t_s) + ' seconds')

    reversed_list = ordered_list[::-1]
    t_s = timeit.timeit('insertion_sort(reversed_list) ', setup='from __main__ import insertion_sort, reversed_list')
    print('WroseCase:\n      sorting time: ' + str(t_s) + ' seconds')

    vals = [randint(0, 1000) for _ in range(10)]
    t_s = timeit.timeit('insertion_sort(vals) ', setup='from __main__ import insertion_sort, vals')
    print('RandomCase:\n     sorting time: ' + str(t_s) + ' seconds')
