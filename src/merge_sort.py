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
    """Helper: split list."""
    if len(input_list) <= 1:
        return input_list
    else:
        mid_index = len(input_list) // 2
        left_list = _merge_sort(input_list[:mid_index])
        right_list = _merge_sort(input_list[mid_index:])
        return _merge(left_list, right_list)


def _merge(left_list, right_list):
    """Helper: sort the splitted lists."""
    if not left_list:
        return right_list
    elif not right_list:
        return left_list
    elif left_list[0] < right_list[0]:
        return left_list[0] + _merge(left_list[1:], right_list)
    return list(right_list[0]) + _merge(left_list, right_list[1:])
