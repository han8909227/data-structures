"""My radix sort."""
import timeit
from random import randint
from que_ import Queue


def radix_sort(input_list):
    """Radix sort."""
    if not isinstance(input_list, (list, tuple)):
        raise ValueError('input takes list/tuple only')

    if isinstance(input_list, (tuple)):
        input_list = list(input_list)

    if not all(isinstance(val, (int, float)) for val in input_list):
        raise ValueError('all items in list must be a number')

    radix_list = input_list[:]  # prevent changing original list
    neg = False  # if neg value exist in list
    for num in radix_list:
        if num < 0:
            neg = True
            temp = [int(num + 10e10) for num in radix_list]
            radix_list = temp
            break

    str_inputs = [str(val) for val in radix_list]
    max_val = max(str_inputs, key=len)
    q_set = [Queue() for _ in range(10)]
    indx = 1

    for indx in range(1, len(max_val) + 1):
        _populate_sets(str_inputs, indx, q_set)
        str_inputs = _dequeue_sets(q_set)

    if neg:
        return [int(int(val) - 10e10) for val in str_inputs]
    else:
        return [int(val) for val in str_inputs]


def _populate_sets(str_inputs, indx, q_set):
    """Populate the q set with corresponding indx val of each num."""
    for num in str_inputs:
        try:
            val_at_indx = int(num[-indx])
            q_set[val_at_indx].enqueue(num)
        except IndexError:
            q_set[0].enqueue(num)


def _dequeue_sets(q_set):
    """Empty the q sets to form new list (1 idx iteration)."""
    temp_sorted = []
    for q in q_set:
        for _ in range(len(q)):
            temp_sorted.append(q.dequeue())
    return temp_sorted


if __name__ == '__main__':  # pragma: no cover
    ordered_list = [num for num in range(10)]
    t_s = timeit.timeit('radix_sort(ordered_list) ', setup='from __main__ import radix_sort, ordered_list')
    print('BestCase:\n       sorting time: ' + str(t_s) + ' seconds')

    reversed_list = ordered_list[::-1]
    t_s = timeit.timeit('radix_sort(reversed_list) ', setup='from __main__ import radix_sort, reversed_list')
    print('WroseCase:\n      sorting time: ' + str(t_s) + ' seconds')

    vals = [randint(0, 1000) for _ in range(10)]
    t_s = timeit.timeit('radix_sort(vals) ', setup='from __main__ import radix_sort, vals')
    print('RandomCase:\n     sorting time: ' + str(t_s) + ' seconds')

