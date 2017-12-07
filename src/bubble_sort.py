"""My Bubble sort."""


def bubble_sort(input_list):
    """Bubble sort."""
    if not isinstance(input_list, (list, tuple)):
        raise ValueError('input takes list/tuple only')

    if isinstance(input_list, (tuple)):
        temp = []
        for val in input_list:
            temp.append(val)
        input_list = temp

    if not all(isinstance(val, (int, float)) for val in input_list):
        raise ValueError('all items in list must be a number')
    bubble = input_list
    while True:
        changed = False
        for loc in range(len(bubble) - 1):
            if bubble[loc] > bubble[loc + 1]:
                bubble[loc + 1], bubble[loc] = bubble[loc], bubble[loc + 1]
                changed = True
        if not changed:
            return bubble

