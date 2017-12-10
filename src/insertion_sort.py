"""My Insertion sort."""
import timeit
from random import randint


def insertion_sort(input_list):
    """Insertion sort."""
    if not isinstance(input_list, (list, tuple)):
        raise ValueError('input takes list/tuple only')

    if isinstance(input_list, (tuple)):
        temp = []
        for val in input_list:
            temp.append(val)
        input_list = temp

    if not all(isinstance(val, (int, float)) for val in input_list):
        raise ValueError('all items in list must be a number')

    for index in range(1, len(input_list)):
        curr = input_list[index]
        pos = index

        while pos > 0 and input_list[pos - 1] > curr:
            input_list[pos] = input_list[pos - 1]
            pos -= 1
        input_list[pos] = curr
    return input_list


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
