"""My Bubble sort."""
import timeit
from random import randint


def bubble_sort(input_list):
    """Bubble sort."""
    if not isinstance(input_list, (list, tuple)):
        raise ValueError('input takes list/tuple only')

    if isinstance(input_list, (tuple)):
        input_list = list(input_list)

    if not all(isinstance(val, (int, float)) for val in input_list):
        raise ValueError('all items in list must be a number')
    bubble = input_list[:]
    while True:
        changed = False
        for loc in range(len(bubble) - 1):
            if bubble[loc] > bubble[loc + 1]:
                bubble[loc + 1], bubble[loc] = bubble[loc], bubble[loc + 1]
                changed = True
        if not changed:
            return bubble

if __name__ == '__main__':  # pragma: no cover
    ordered_list = [num for num in range(10)]
    t_s = timeit.timeit('bubble_sort(ordered_list) ', setup='from __main__ import bubble_sort, ordered_list')
    print('BestCase:\n       sorting time: ' + str(t_s) + ' seconds')

    reversed_list = ordered_list[::-1]
    t_s = timeit.timeit('bubble_sort(reversed_list) ', setup='from __main__ import bubble_sort, reversed_list')
    print('WroseCase:\n      sorting time: ' + str(t_s) + ' seconds')

    vals = [randint(0, 1000) for _ in range(10)]
    t_s = timeit.timeit('bubble_sort(vals) ', setup='from __main__ import bubble_sort, vals')
    print('RandomCase:\n     sorting time: ' + str(t_s) + ' seconds')
